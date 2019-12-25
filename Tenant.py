from .Map import Map
class Tenant(Map):
    def __init__(self, q, body):
        self.q = q
        for key in body:
            self[key] = body[key]