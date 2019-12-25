from .Map import Map
from .Tenant import Tenant
class Project(Map):
    def __init__(self, q, body):
        self.q = q
        for key in body:
            if key == 'tenant':
                self[key] = Tenant(q, body[key])
            else:
                self[key] = body[key]
