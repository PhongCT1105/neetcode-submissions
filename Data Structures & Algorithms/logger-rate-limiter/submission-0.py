class Logger:

    def __init__(self):
        self.hash_map = {}        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hash_map:
            if self.hash_map[message] <= timestamp:
                self.hash_map[message] += 10
                return True
            else:
                return False
        else:
            self.hash_map[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
