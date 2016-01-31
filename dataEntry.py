#!/usr/bin/env python

from dirScrubber import DirResumeScrubber
from csvScrubber import CsvResumeScrubber
import uicomponents as ui
import sys
import csv
import os
import Tkinter as Tk, tkFileDialog, Tkconstants

attrs = [
    'name',
    'email',
    'grad year',
    'school'
]

class DataEntryUI(Tk.Frame):

    def __init__(self, root):
        Tk.Frame.__init__(self, root)
        Tk.Button(self, text='set directory', command=self.changeDir).pack()
        self.lblDirectory = Tk.Label(self)
        self.lblDirectory.pack()
        self.btnGetNext = Tk.Button(self, text='get next', state=Tk.DISABLED, command=self.getNext)
        self.btnGetNext.pack()

        self.entries = {attr: Tk.Entry(self, state=Tk.DISABLED) for attr in attrs}
        for attr in attrs:
            Tk.Label(self, text='{}:'.format(attr)).pack()
            self.entries[attr].pack()

    def changeDir(self):
        # get dir
        dir = tkFileDialog.askdirectory(mustexist=True)

        scrubber = DirResumeScrubber(os.path.join(dir, '*.*'))

        self.csvPath = os.path.join(dir, 'candidates.csv')
        fileExists = os.path.isfile(self.csvPath)

        excludeList = []
        if(fileExists):
            with open(self.csvPath, 'rb') as csvfile:
                reader = csv.DictReader(csvfile)
                excludeList = [row['resume'] for row in reader if 'resume' in row.keys()]
        else:
            with open(self.csvPath, 'ab') as csvfile:
                writer = csv.DictWriter(csvfile, attrs + ['resume'])
                writer.writeheader()
        self.resumeIter = (r for r in scrubber if r not in excludeList)
        self.lblDirectory.config(text=dir)
        self.btnGetNext.config(state=Tk.NORMAL)

    def getNext(self):
        self.btnGetNext.config(state=Tk.DISABLED)
        resume = self.resumeIter.next()
        # all out check
        self.curRes = resume.getFile()
        #TODO turn into rel path ^

        resume.open()
        # entries ui
        done = False
        for attr in attrs:
            self.entries[attr].config(disabledbackground='yellow')
            self.update_idletasks()
            val = ui.getClipboardChange() # this is blocking which sucks
            self.entries[attr].config(state=Tk.NORMAL)
            self.entries[attr].delete(0, Tk.END)
            self.entries[attr].insert(0, val)
            self.entries[attr].config(state=Tk.DISABLED, bg='white', disabledbackground='')
            self.update_idletasks()
        self.fieldsUpdated()

    def fieldsUpdated(self):
        for attr, entry in self.entries.iteritems():
            entry.config(state=Tk.NORMAL)
        self.btnGetNext.config(state=Tk.NORMAL, command=self.saveAndNext)

    def saveAndNext(self):
        row = {'resume': self.curRes}
        for attr, e in self.entries.iteritems():
            row[attr] = e.get()
            e.delete(0, Tk.END)
            e.config(state=Tk.DISABLED)
        with open(self.csvPath, 'ab') as csvfile:
            writer = csv.DictWriter(csvfile, attrs + ['resume'])
            writer.writerow(row)
        self.getNext()

if __name__=='__main__':
    root = Tk.Tk()
    DataEntryUI(root).pack()
    root.mainloop()
