from .Map import Map
from .User import User

class TestResult(Map):
    def __init__(self, test_cycle, q, body):
        self.q = q
        self.test_cycle = test_cycle
        for key in body:
            if key == 'user':
                self[key] = User(q, body[key])
            else:
                self[key] = body[key]