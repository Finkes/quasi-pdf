Syntax:

python quasipdf.py ( <document.pdf> <pages> )* <output.pdf>


example: 

python quasipdf.py document1.pdf 0 document2.pdf 1,4,5,6,8 document3.pdf 1-2 output.pdf

The example will include all pages of document1.pdf, pages 1,4,5,6,8 of document2.pdf and pages 1 - 2 of document3.pdf. The name of the generated file will be output.pdf

There are 3 ways to specify the pages you want to add in the new document:
1. range e.g.:   1-5
2. list e.g.:  1,4,5,7,23,12
3. all pages : 0

