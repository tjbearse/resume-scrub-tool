import csv
import os

from resumeScrubber import ResumeScrubber, Resume
import uicomponents as ui

class CsvResumeScrubber(ResumeScrubber):
    def __init__(self, file):
        self.file = file
        with open(file, 'rb') as csvfile:
            self.csvData = list(csv.reader(csvfile))

        with open(file, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.csvData)

        print('which is the resume?')
        self.resumeCol = ui.getChoice(self.csvData[0], range(len(self.csvData[0])))

        print('where do labels go?')
        labelCol = ui.getChoice(self.csvData[0] + ['[ new ]'], range(len(self.csvData[0]) + 1))
        self.labelCol = labelCol

        print('is there a header row?')
        hasHeader = ui.getChoice(['yes', 'no'], [True, False])
        if(hasHeader):
            if(not self.csvData[0][labelCol]):
                self.csvData[0][labelCol] = 'label'

        resumes = [
                ResumeFromCsv(
                    row,
                    self.resumeCol,
                    labelCol,
                    self.save
                ) for row in self.csvData[hasHeader:]
                    if(labelCol == len(row) or not row[labelCol])
            ]
        super(CsvResumeScrubber, self).__init__(resumes)

    def save(self):
        with open(self.file, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.csvData)

class ResumeFromCsv(Resume):
    def __init__(self, row, fileInd, labelInd, save):
        self.row = row
        self.save = save
        self.labelCol = labelInd
        super(ResumeFromCsv, self).__init__(row[fileInd])

    def label(self, label):
        if(self.labelCol == len(self.row)):
            self.row.append(label)
        else:
            self.row[self.labelCol] = label
        self.save()
