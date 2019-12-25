from .Map import Map
from .TestSuiteAssignment import TestSuiteAssignment
class TestPhase(Map):
    def __init__(self, q, body):
        self.q = q
        for key in body:
            if key == 'test_suite_assignments':
                self[key] = []
                for t in body[key]:
                    self[key].append(TestSuiteAssignment(q, self, t))
            elif key == 'created_at' or key == 'updated_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]