import json
import datetime
from .Project import Project
from .TestSuite import TestSuite
from .TestPhase import TestPhase
import urllib.request

class QualityForward:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://cloud.veriserve.co.jp/"
    def get_current_project(self):
        url = f'{self.url}/api/v2/current_project?api_key={self.api_key}'
        body = self.get_json(url)
        return Project(self, body)
    def get_test_phases(self):
        url = f'{self.url}/api/v2/test_phases?api_key={self.api_key}'
        body = self.get_json(url)
        test_phases = []
        for test_phase in body['test_phases']:
            test_phases.append(TestPhase(self, test_phase))
        return test_phases
    def get_test_suites(self):
        url = f'{self.url}/api/v2/test_suites.json?api_key={self.api_key}'
        body = self.get_json(url)
        test_suites = []
        for test_suite in body['test_suites']:
            test_suites.append(TestSuite(self, test_suite))
        return test_suites
    def get_json(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        return body
    def to_date(self, str):
        return datetime.datetime.strptime(str, '%Y-%m-%dT%H:%M:%S.%f%z')
