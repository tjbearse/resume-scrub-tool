import subprocess
import os

class ResumeScrubber(object):
    def __init__(self, resumes):
        self.resumes = resumes

    def __iter__(self):
        return self.resumes.__iter__()

class Resume(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def getFile(self):
        return self.filepath

    def open(self):
        print(self.filepath)
        cmd = 'open {0}'.format(self.filepath)
        print(cmd)
        subprocess.Popen(cmd.split(' '))

    def label(self, label):
        dir = os.path.join(os.path.dirname(self.filepath), label)
        if not os.path.exists(dir):
            os.makedirs(dir)
        newFile = os.path.join(dir, os.path.basename(self.filepath))
        os.rename(self.filepath, newFile)

