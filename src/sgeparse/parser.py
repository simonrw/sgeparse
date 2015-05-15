class JobsParser(object):

    def __init__(self, data):
        self.data = data

    @property
    def njobs(self):
        return 10

    @property
    def jobs(self):
        return iter([{'owner': 'sw'}])
