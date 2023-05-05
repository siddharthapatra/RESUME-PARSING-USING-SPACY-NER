### Resume Parser Application using Natural Language Processing (Spacy NER)
 
In the fast-paced and ever-evolving job market of today, the recruitment process has become increasingly intricate and demanding for recruiters and HR professionals. Countless resumes flood the recruitment pipeline, creating a tedious and time-consuming task to identify the most qualified candidates for a position. To combat this challenge, we embarked on a mission to create a resume parser application that harnesses the power of Natural Language Processing (NLP) and, more specifically, Spacy's Named Entity Recognition (NER) technology to autonomously extract essential entities such as name, location, experience, and skills from a resume.

This project report aims to take you through the intricate and elaborate development process of our innovative resume parser application, starting from the preliminary data preparation to the final model deployment. We delve into the highly technical aspects of implementing Spacy's NER technology and share our in-depth experiences of overcoming various challenges along the way.

### Resume Parsing in Python Project Objective
The implementation of natural language processing (NLP) techniques in Python has revolutionized the way resumes are processed. This project uses the popular Python library SpaCy to build a resume parser that employs tokenization, lemmatization, parts of speech tagging, and optical character recognition (OCR) to extract textual data from resumes submitted in PDF format. The parser aims to require minimal human intervention in extracting crucial information from resumes, such as an applicant's work experience, name, geographical location, and more. This NLP project is a great opportunity for beginners to explore exciting concepts in the field.

The resume parser application system built here can handle millions of resumes and parse the necessary fields. It uses the SpaCy library for OCR and text classification. To accomplish this, the model is first trained with the dataset of resumes, which contains fields like location, designation, name, years of experience, college, degree, graduation year, companies worked at, and email address. Once the model is trained, the application can pick out the values of these fields from new resumes.


### NLP Tools and Techniques You Will Master in this SpaCy Resume Parser Project

Here are some of the concepts you will learn when building this python resume parser application system:

**Tokenization** is the process of splitting textual data into tokens, which can either be words or characters, depending on the problem being solved. It is usually the first step in any NLP project and helps in further steps of the pipeline, which typically involves evaluating the weights of all the words depending on their significance in the corpus.

**Lemmatization** is used to convert all words into their root form, called 'lemma,' to decode the semantics of the text. The form of the verb used does not have a significant impact, so converting all the words into their root form helps to simplify the process.

**Parts-of-Speech Tagging** helps to understand the context of the text. It is used to distinguish between words that have multiple meanings, like 'Apple,' which can be used as a proper noun or a common noun.

**Stopwords elimination** involves deleting words like 'a,' 'the,' 'am,' 'is,' etc., that do not add meaning to a sentence. This step saves processing power and time, especially in cases where resumes are submitted with long paragraphs containing many stopwords.

**SpaCy** is a popular library used in many NLP-based projects by data scientists as it offers quick implementation of various techniques mentioned above. It also supports the implementation of rule-based matching, shallow parsing, dependency parsing, and more.

**OCR using TIKA** involves converting images into text to extract meaningful information. In this project, Apache Tika, an open-source library, is used to implement OCR.

**The machine learning pipeline** is used to build a model that can pull out relevant fields like location, name, etc., from different resumes of different formats. Neural networks using the SpaCy library are employed to accomplish this.

**Scaling up the Resume Parser in Python!**
The project also teaches you how to scale up the resume parser in Python for large-scale resumes. A production-ready model for resume parsing is built that can analyze millions of resumes using GCP Model Deployment using Streamlit for Resume Parsing. Before deploying the model for large-scale resumes, it is important to tag them and make the model learn any new entities that might have been added.
