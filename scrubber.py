#!/usr/bin/env python

from dirScrubber import DirResumeScrubber

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

#TODO get file glob
fileGlob = 'test/*.txt'

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

def getChoice(labels):
    while True:
        for i, label in enumerate(labels):
            print("{0}) {1}".format(i, label))
        print("q) quit\n")
        choice = raw_input()
        try:
            if(choice[0] == 'q'):
                quit()
            return labels[int(choice)]
        except SystemExit:
            raise
        except:
            print('oops! try again')

scrubber = DirResumeScrubber(fileGlob)
for resume in scrubber:
    resume.open()
    choice = getChoice(labels)
    resume.label(choice.replace(' ', ''))
