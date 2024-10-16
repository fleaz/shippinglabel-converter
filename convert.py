#! /usr/bin/env python3

from pypdf import PdfWriter, PdfReader, Transformation
from pypdf.generic import RectangleObject

def convert_dhl(id):
    with open(f"./uploads/{id}.pdf", "rb") as fh:
        reader = PdfReader(fh)
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

        with open(f"./downloads/{id}.pdf", "wb") as fh:
            writer.write(fh)
