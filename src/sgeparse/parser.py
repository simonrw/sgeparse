import xml.etree.ElementTree as ET
try:
    import io
except ImportError:
    import StringIO as io
from datetime import datetime


class JobsParser(object):

    def __init__(self, data):
        self.data = data
        self.tree = ET.fromstring(self.data)
        self.jobs = self.parse_jobs()

    def parse_jobs(self):
        out = []
        for job in self.tree.iter('job_list'):
            out.append({
                'job_number': int(job[0].text),
                'priority': float(job[1].text),
                'name': job[2].text,
                'owner': job[3].text,
                'state': job[4].text,
                'start_time': datetime.strptime(job[5].text, '%Y-%m-%dT%H:%M:%S'),
                'queue': job[6].text.split('@')[0],
                'host': job[6].text.split('@')[1],
                'slots': int(job[7].text),
            })
        return out

    @property
    def njobs(self):
        return len(self.jobs)
