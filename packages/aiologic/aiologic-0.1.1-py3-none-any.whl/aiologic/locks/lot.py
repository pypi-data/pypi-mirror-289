#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Ilya Egorov <0x42005e1f@gmail.com>
# SPDX-License-Identifier: ISC

__all__ = (
    'ParkingLot',
)

from weakref import ref
from itertools import repeat
from collections import deque

from aiologic.lowlevel import Flag, TaskEvent, ThreadEvent, checkpoint


class ParkingToken:
    __slots__ = (
        '__weakref__',
        'lot',
        'done',
        'event',
    )
    
    @staticmethod
    def __new__(cls, /, lot):
        self = super(ParkingToken, cls).__new__(cls)
        
        self.lot = lot
        
        self.done = Flag()
        
        return self
    
    @classmethod
    def __init_subclass__(cls, /, **kwargs):
        raise TypeError("type 'ParkingToken' is not an acceptable base type")
    
    def __reduce__(self, /):
        raise TypeError(f"cannot reduce {self!r}")
    
    async def __aenter__(self, /):
        self.event = event = TaskEvent()
        
        self.lot.waiters.append(ref(self))
        self.lot.unpark(0)
        
        return event
    
    async def __aexit__(self, /, exc_type, exc_value, traceback):
        if self.done.set(None):
            try:
                self.lot.waiters.remove(ref(self))
            except ValueError:
                pass
        elif exc_value is not None:
            self.lot.unpark(exact=self.done.get())
        else:
            self.event.set()
    
    def __enter__(self, /):
        self.event = event = ThreadEvent()
        
        self.lot.waiters.append(ref(self))
        self.lot.unpark(0)
        
        return event
    
    def __exit__(self, /, exc_type, exc_value, traceback):
        if self.done.set(None):
            try:
                self.lot.waiters.remove(ref(self))
            except ValueError:
                pass
        elif exc_value is not None:
            self.lot.unpark(exact=self.done.get())
        else:
            self.event.set()


class ParkingLot:
    __slots__ = (
        'waiters', 'tickets',
    )
    
    @staticmethod
    def __new__(cls, /):
        self = super(ParkingLot, cls).__new__(cls)
        
        self.waiters = deque()
        self.tickets = []
        
        return self
    
    def __repr__(self, /):
        return 'ParkingLot()'
    
    def park(self, /):
        return ParkingToken(self)
    
    async def park_as_task(self, /, *, exact=None):
        if tickets := self.tickets:
            try:
                success = tickets.pop()
            except IndexError:
                success = False
        else:
            success = False
        
        if not success:
            if exact is None:
                token = ParkingToken(self)
                
                async with token as event:
                    success = await event
                
                if not success and event.is_set():
                    self.unpark(exact=token.done.get())
            else:
                token = (event := TaskEvent(), is_unset := [True])
                
                self.waiters.append(token)
                self.unpark(0)
                
                try:
                    success = await event
                finally:
                    if not success:
                        if is_unset:
                            try:
                                is_unset.pop()
                            except IndexError:
                                self.unpark(exact=exact)
                            else:
                                try:
                                    self.waiters.remove(token)
                                except ValueError:
                                    pass
                        else:
                            self.unpark(exact=exact)
        else:
            await checkpoint()
        
        return success
    
    def park_as_thread(self, /, *, blocking=True, timeout=None, exact=None):
        if tickets := self.tickets:
            try:
                success = tickets.pop()
            except IndexError:
                success = False
        else:
            success = False
        
        if not success and blocking:
            if exact is None:
                token = ParkingToken(self)
                
                with token as event:
                    success = event.wait(timeout)
                
                if not success and event.is_set():
                    self.unpark(exact=token.done.get())
            else:
                token = (event := ThreadEvent(), is_unset := [True])
                
                self.waiters.append(token)
                self.unpark(0)
                
                try:
                    success = event.wait(timeout)
                finally:
                    if not success:
                        if is_unset:
                            try:
                                is_unset.pop()
                            except IndexError:
                                self.unpark(exact=exact)
                            else:
                                try:
                                    self.waiters.remove(token)
                                except ValueError:
                                    pass
                        else:
                            self.unpark(exact=exact)
        
        return success
    
    def park_nowait(self, /):
        if tickets := self.tickets:
            try:
                success = tickets.pop()
            except IndexError:
                success = False
        else:
            success = False
        
        return success
    
    def unpark(self, /, count=1, *, exact=False):
        waiters = self.waiters
        tickets = self.tickets
        
        pending = 0
        unparked = 0
        
        while waiters:
            if not pending:
                if tickets:
                    try:
                        tickets.pop()
                    except IndexError:
                        if unparked == count:
                            break
                    else:
                        pending += 1
                else:
                    if unparked == count:
                        break
            
            try:
                maybe_token = waiters.popleft()
            except IndexError:
                pass
            else:
                if callable(maybe_token):
                    if (token := maybe_token()) is not None:
                        if token.done.set(pending or exact):
                            token.event.set()
                            
                            if pending:
                                pending -= 1
                            else:
                                unparked += 1
                else:
                    event, is_unset = maybe_token
                    
                    if is_unset:
                        try:
                            is_unset.pop()
                        except IndexError:
                            pass
                        else:
                            event.set()
                            
                            if pending:
                                pending -= 1
                            else:
                                unparked += 1
        else:
            if exact:
                pending += count - unparked
            
            if pending == 1:
                tickets.append(True)
            elif pending:
                tickets.extend(repeat(True, pending))
        
        return unparked
    
    def unpark_all(self, /):
        waiters = self.waiters
        tickets = self.tickets
        
        pending = 0
        unparked = 0
        
        while waiters:
            if not pending:
                if tickets:
                    try:
                        tickets.pop()
                    except IndexError:
                        pass
                    else:
                        pending += 1
            
            try:
                maybe_token = waiters.popleft()
            except IndexError:
                pass
            else:
                if callable(maybe_token):
                    if (token := maybe_token()) is not None:
                        if token.done.set(pending):
                            token.event.set()
                            
                            if pending:
                                pending -= 1
                            else:
                                unparked += 1
                else:
                    event, is_unset = maybe_token
                    
                    if is_unset:
                        try:
                            is_unset.pop()
                        except IndexError:
                            pass
                        else:
                            event.set()
                            
                            if pending:
                                pending -= 1
                            else:
                                unparked += 1
        else:
            if pending == 1:
                tickets.append(True)
            elif pending:
                tickets.extend(repeat(True, pending))
        
        return unparked
