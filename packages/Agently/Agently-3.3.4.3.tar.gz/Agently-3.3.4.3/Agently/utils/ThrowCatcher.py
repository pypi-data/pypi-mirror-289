import threading
import asyncio

class ThrowCatcher(object):
    def __init__(self):
        self.queue = asyncio.Queue()
    
    def throw(self, event: str, data:any=None):
        self.queue.put({
            "event": event,
            "data": data,
        })
    
    def _catch(self):
        while True:
            self.queue.get()