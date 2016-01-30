import glob

from resumeScrubber import Resume, ResumeScrubber


class DirResumeScrubber(ResumeScrubber):
    def __init__(self, fileGlob):
        resumes = [Resume(path) for path in glob.glob(fileGlob)]
        super(DirResumeScrubber, self).__init__(resumes)

