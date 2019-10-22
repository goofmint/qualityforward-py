import json
from .Project import Project
import urllib.request

class QualityForward:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://cloud.veriserve.co.jp/"
    def get_current_project(self):
        url = f'{self.url}/api/v2/current_project?api_key={self.api_key}'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        return Project(self, body)