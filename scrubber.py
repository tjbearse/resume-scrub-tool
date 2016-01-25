#!/usr/bin/env python

from dirScrubber import DirResumeScrubber
import uicomponents as ui

# find list of files

# saved data
    # what are my lables
        # rating 1-3, fulltime/intern, watchlist
    # flag/skip
    # LATER: name, email, grad year (watch on copy buffer)

# ui picking choices

# saving the data
    # move file X
    # write to csv column

# get choices
labels = [
    'one Fulltime',
    'two Fulltime',
    'three Fulltime',
    'one Intern',
    'two Intern',
    'three Intern',
    'flag',
    'waitlist'
]


#TODO get file glob
fileGlob = 'test/*.txt'
scrubber = DirResumeScrubber(fileGlob)
for resume in scrubber:
    resume.open()
    choice = ui.getChoice(labels)
    resume.label(choice.replace(' ', ''))
