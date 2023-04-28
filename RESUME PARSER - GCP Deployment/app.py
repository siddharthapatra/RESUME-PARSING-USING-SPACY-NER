# Import necessary libraries
import streamlit as st
import docx2txt
# from tika import parser
import os
import spacy
import pandas as pd
# import docx2txt
# from PIL import Image 
# from PyPDF2 import PdfFileReader
import pdfplumber
# from pathlib import Path

# def read_pdf(file):
# 	pdfReader = PdfFileReader(file)
# 	count = pdfReader.numPages
# 	all_page_text = ""
# 	for i in range(count):
# 		page = pdfReader.getPage(i)
# 		all_page_text += page.extractText()
# 	return all_page_text

# Define function to extract named entities from resume text
def pred(text):
    output={}
    nlp=spacy.load("model")
    text=text.replace('\n',' ')
    doc = nlp(text)
    # Loop through each named entity in the text
    for ent in doc.ents:
        # Print out the label and text of each entity
        print(f'{ent.label_.upper():{30}}-{ent.text}')
        # Add the entity to the output dictionary
        output[ent.label_.upper()]=ent.text
    return output

# Define Streamlit app
st.title("Resume Parser with Spacy")
st.subheader("Upload your resume here!")

# Allow users to upload a file and specify the allowed file types
uploaded_file = st.file_uploader("Upload Files",type=['pdf','docx'])

# If the user has uploaded a file
if uploaded_file is not None:
    # If the user clicks the "Process" button
    if st.button("Process"):
        # If the uploaded file is a PDF
        if uploaded_file.type=='application/pdf':
            # Record details of the uploaded file
            file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
            # Open the PDF using pdfplumber
            with pdfplumber.open(uploaded_file) as pdf:
                ext_txt = str()
                # Loop through each page in the PDF and extract the text
                for i in range(len(pdf.pages)):
                    page = pdf.pages[0]
                    ext_txt += page.extract_text()
                # Use the "pred" function to extract named entities from the text
                op = pred(ext_txt)
                # Display the extracted entities to the user
                st.write(op)
        # If the uploaded file is a DOCX
        if uploaded_file.type=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            # Record details of the uploaded file
            file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
            # Use the docx2txt library to extract the raw text from the file
            raw_text = docx2txt.process(uploaded_file)
            # Use the "pred" function to extract named entities from the text
            op = pred(raw_text)
            # Display the extracted entities to the user
            st.write(op)
