import time

class Throttle:
    def __init__(self, maxReq=100, waitTimeToReset=120):
        self.maxReq = maxReq                                        # Max number of requests (100 requests per 2 minutes)
        self.waitTimeToReset = waitTimeToReset          # Throttle time in seconds
        self.counter = 0                                                    # Counter for number of requests
        self.lastTimeReq = None
    
    def isAllowed(self):
        if self.counter < self.maxReq:
            self.counter += 1
            self.lastTimeReq = time.time()
            return True
        else:
            if time.time() - self.lastTimeReq > self.waitTimeToReset:
                self.counter = 0
                return True
            return False
