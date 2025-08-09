from typing import Any, Dict
import time

class SimpleCache:
    def __init__(self, ttl: int = 300):
        self.ttl = ttl
        self.store: Dict[str, Any] = {}

    def set(self, key: str, value: Any):
        self.store[key] = (value, time.time())

    def get(self, key: str):
        if key not in self.store:
            return None
        value, timestamp = self.store[key]
        if (time.time() - timestamp) > self.ttl:
            del self.store[key]
            return None
        return value
