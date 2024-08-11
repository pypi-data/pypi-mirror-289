import os
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, image_path, product_id, product_name, amount_purchased, price_per_unit,
             total_price):
    """
    This function converts Excel files into PDF invoices.
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        # Removes the directory extension name.
        filename = Path(filepath).stem
        invoice_nr, date = filename.split('-')

        pdf.set_font(family='Times', style='B', size=16)
        pdf.cell(w=50, h=8, txt=f"Invoice Nr.{invoice_nr}", ln=1)

        pdf.set_font(family='Times', style='B', size=16)
        pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

        df = pd.read_excel(filepath)

        # Add a header.
        columns = df.columns
        columns = [item.replace('_', ' ').title() for item in columns]
        pdf.set_font(family='Times', style='B', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=columns[0], border=1)
        pdf.cell(w=55, h=8, txt=columns[1], border=1)
        pdf.cell(w=40, h=8, txt=columns[2], border=1)
        pdf.cell(w=30, h=8, txt=columns[3], border=1)
        pdf.cell(w=40, h=8, txt=columns[4], border=1, ln=1)

        # Add rows to the table.
        for index, row in df.iterrows():
            pdf.set_font(family='Times', style='B', size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=55, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=40, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=40, h=8, txt=str(row[total_price]), border=1, ln=1)

        total_sum = df[total_price].sum()
        pdf.set_font(family='Times', style='B', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=55, h=8, txt="", border=1)
        pdf.cell(w=40, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=40, h=8, txt=str(total_sum), border=1, ln=1)

        # Add total sum sentence.
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=55, h=12, txt=f"The total Price is {total_sum}", ln=1)

        # Add company name and logo.
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=28, h=8, txt="PythonHow")
        pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")


