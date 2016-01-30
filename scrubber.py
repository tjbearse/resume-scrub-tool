#!/usr/bin/env python

from dirScrubber import DirResumeScrubber
from csvScrubber import CsvResumeScrubber
import uicomponents as ui
import sys

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
print('\n')

scrubber = None
if(format == 'csv'):
    file = sys.argv[1]
    if(not file):
        file = raw_input('enter file name:\n')
    scrubber = CsvResumeScrubber(file)
elif(format == 'file glob'):
    glob = sys.argv[1]
    if(not glob):
        glob = raw_input('enter glob:\n')
    scrubber = DirResumeScrubber(glob)

for resume in scrubber:
    resume.open()
    choice = ui.getChoice(labels)
    resume.label(choice.replace(' ', ''))
