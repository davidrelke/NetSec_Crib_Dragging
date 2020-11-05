from typing import List

class IterationMessage:
    message_1: List[str]
    message_2: List[str]
    iteration: int
    
    def __init__(self, message_1, message_2, iteration): 
        self.message_1 = message_1
        self.message_2 = message_2
        self.iteration = iteration