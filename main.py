import fitz
import pandas as pd
import re
from pdf2image import convert_from_path


class Main():

    def __init__(self, docpath):
        self.docpath = docpath

    def read_standard_pdf(self):
        doc = fitz.open(self.docpath)
        pagecount = doc.page_count
        data = pd.DataFrame()
        page_data = []
        for page_no in range(pagecount):
            page_no = int(float(page_no))
            page = doc[page_no]
            blocks = page.get_text("dict")["blocks"]
            if len(blocks) == 1:
                continue

            for b in blocks:
                block_text = []
                block_data = []
                if b["type"] == 0:
                    for l in b["lines"]:
                        for s in l["spans"]:
                            block_text.append(s["text"])
                    block_text = "\n".join([val for val in block_text])
                    if len(re.sub(r"\W","", block_text)) <= 0:
                        continue
                    for val in b["bbox"]:
                        block_data.append(val)
                    block_data.append(block_text)
                page_data.append(block_data)
        return page_data

    def get_document_type(self):
        total_page_area = 0.0
        total_text_area = 0.0
        doc = fitz.open(self.docpath)
        page_type = []
        for page_num, page in enumerate(doc):
            if not pd.DataFrame(page.get_fonts()).empty:
                total_page_area = total_page_area + abs(page.rect)
                text_area = 0.0
                for b in page.get_text_blocks():
                    if len(str(b[4]).encode("ascii", "ignore").strip()) > 0:
                        r = fitz.Rect(b[:4])
                        text_area = text_area + abs(r)
                    else:
                        continue
                total_text_area = total_text_area + text_area
                text_prec = total_text_area / total_page_area
                if text_prec < 0.01:
                    page_type.append("image")
                else:
                    page_type.append("text")
            else:
                page_type.append("image")
        if page_type.count("image") >= page_type.count("text"):
            return "image"
        else:
            return "text"


    def read_image(self):
        pass








