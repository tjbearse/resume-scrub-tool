class ResumeScrubber(object):
    def __init__(self, resumes):
        self.resumes = resumes

    def __iter__(self):
        return self.resumes.__iter__()

class Resume(object):
    def open(self):
        pass
    def label(self, label):
        pass
