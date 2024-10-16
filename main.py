#! /usr/bin/env python3

from pypdf import PdfWriter, PdfReader, Transformation
from pypdf.generic import RectangleObject

with open("input.pdf", "rb") as in_f:
    reader = PdfReader(in_f)
    writer = PdfWriter()

    numPages = len(reader.pages)
    if numPages != 1:
        exit(1)

    page = reader.pages[0].rotate(90)
    page = reader.pages[0]

    left = 20
    bottom = 450
    right = 570
    # calculate last value to get a 3:2 rectangle
    top = bottom+((right-left)/3)*2

    page.mediabox = RectangleObject((left, bottom,right,top))
    writer.add_page(page)

    with open("out.pdf", "wb") as fh:
        writer.write(fh)
