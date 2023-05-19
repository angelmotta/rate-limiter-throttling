import time

class SlidingWindowRateLimiter:
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.timestamp_queue = []

    def allow_request(self):
        current_timestamp = time.time()

        # Remove expired timestamps from the queue
        while self.timestamp_queue and self.timestamp_queue[0] <= current_timestamp - self.window_size:
            self.timestamp_queue.pop(0)

        # Verify if number of timestamps in the queue exceeds the limit
        if len(self.timestamp_queue) < self.limit:
            self.timestamp_queue.append(current_timestamp)
            return True

        return False
