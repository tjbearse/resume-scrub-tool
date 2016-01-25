#!/usr/bin/env python

from dirScrubber import DirResumeScrubber
import uicomponents as ui
import sys

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

print('What is the resume list format?')
format = ui.getChoice(['csv', 'file glob'])

scrubber = None
if(format == 'csv'):
    print('this method has not been implemented yet')
    quit()
    file = raw_input('enter file name')
elif(format == 'file glob'):
    glob = raw_input('enter file glob:\n')
    scrubber = DirResumeScrubber(glob)

for resume in scrubber:
    resume.open()
    choice = ui.getChoice(labels)
    resume.label(choice.replace(' ', ''))
