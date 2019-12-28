import time

class Timer:
    def __init__(self):
        self.runTime = time.time()
    
    def __enter__(self):
        self.runTime = time.time()
        return self
    
    def __exit__(self, exec_type, exec_value, exec_tb):
        self.runTime = (self.runTime - time.time())
    
    def print(self):
        print(self.runTime)