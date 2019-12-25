from .Map import Map
from .User import User

class TestSuiteVersion(Map):
    def __init__(self, q, test_suite, body):
        self.q = q
        self.test_suite = test_suite
        for key in body:
            if key == 'user':
                self[key] = User(q, body[key])
            elif key == 'created_at' or key == 'updated_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]
