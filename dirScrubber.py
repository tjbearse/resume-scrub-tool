import os
import subprocess
import glob

from resumeScrubber import Resume, ResumeScrubber


class DirResumeScrubber(ResumeScrubber):
    def __init__(self, fileGlob):
        resumes = [ResumeFile(path) for path in glob.glob(fileGlob)]
        super(DirResumeScrubber, self).__init__(resumes)

class ResumeFile(Resume):
    def __init__(self, filepath):
        self.filepath = filepath

    def open(self):
        cmd = 'open {0}'.format(self.filepath)
        print(cmd)
        subprocess.Popen(cmd.split(' '))

    def label(self, label):
        dir = os.path.join(os.path.dirname(self.filepath), label)
        if not os.path.exists(dir):
            os.makedirs(dir)
        newFile = os.path.join(dir, os.path.basename(self.filepath))
        os.rename(self.filepath, newFile)
