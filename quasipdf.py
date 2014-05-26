#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyPdf import PdfFileWriter, PdfFileReader
import sys



def main():

    print sys.argv

    currentFileName = ''
    outputFileWriter = PdfFileWriter()
    



    for i, item in enumerate(sys.argv):
        print item

        if i == 0:
            continue

        elif i == len(sys.argv)-1:
            outputFileName = item

        elif i%2 != 0:
            if '.pdf' in item:
                currentFile = item
                inputFileReader = PdfFileReader(file(item, "rb"))
            else:
                print "error! file expected" 
                sys.exit(1)
        else:
            if '-' in item: #range
                start, end = item.split('-')
                start, end = int(start), int(end)

                for i in range(start,end+1):
                    outputFileWriter.addPage(inputFileReader.getPage(i-1))

            elif ',' in item: #selection
                pageList = [int(page) for page in item.split(',')]

                for i in pageList:
                     outputFileWriter.addPage(inputFileReader.getPage(int(i-1)))

            elif item == '0': #all pages
                for i in range(inputFileReader.getNumPages()):
                    outputFileWriter.addPage(inputFileReader.getPage(i))

            elif item.isdigit():
                outputFileWriter.addPage(inputFileReader.getPage(int(item)-1))

            else:
                print "error! range, selection or 0 expected"
                sys.exit(1)
            
           

    outputStream = file(outputFileName, "wb")
    outputFileWriter.write(outputStream)



    print "output has %s pages" % outputFileWriter.getNumPages()

    return


if __name__ == "__main__":
    main()