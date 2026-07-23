"""
Problem Statement

Write a program to manipulate PDF files using PyPDF2.

Your program should be able to merge multiple PDF files into a single PDF.

You are welcome to add more functionalities.
"""

from PyPDF2 import PdfMerger


def merge_pdfs(pdf_list, output_file):
    try:
        merger = PdfMerger()

        for pdf in pdf_list:
            merger.append(pdf)

        merger.write(output_file)
        merger.close()

        print(f"\n✅ PDFs merged successfully!")
        print(f"📄 Output File: {output_file}")

    except FileNotFoundError:
        print("❌ One or more PDF files were not found.")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":

    num = int(input("Enter the number of PDF files to merge: "))

    pdf_files = []

    for i in range(num):
        pdf = input(f"Enter path of PDF {i + 1}: ").strip()
        pdf_files.append(pdf)

    output = input("Enter output PDF name (with .pdf): ").strip()

    merge_pdfs(pdf_files, output)