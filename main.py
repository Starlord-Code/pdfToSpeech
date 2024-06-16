# This Python code snippet is using the `PyPDF2` library to read a PDF file named
# "python-basics-sample-chapters.pdf" and then using the `pyttsx3` library to convert the extracted
# text from the PDF into speech.
# `import pyttsx3` is importing the `pyttsx3` library in Python, which is a text-to-speech conversion
# library that allows you to convert text into spoken words using different speech engines.
import pyttsx3
import PyPDF2



# `pdfreader = PyPDF2.PdfReader(open("python-basics-sample-chapters.pdf", "rb"))` is creating a
# PdfReader object using PyPDF2 library to read the PDF file named "python-basics-sample-chapters.pdf"
# in binary mode ("rb").
pdfreader = PyPDF2.PdfReader(open("python-basics-sample-chapters.pdf", "rb"))

speaker = pyttsx3.init()


# This part of the code snippet is iterating through each page of the PDF file using a for loop. For
# each page, it extracts the text content using `pdfreader.pages[page_num].extract_text()`, then it
# cleans up the extracted text by removing leading and trailing whitespaces and replacing newline
# characters with spaces.
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

# The code snippet you provided is using the `pyttsx3` library in Python for text-to-speech
# conversion.

speaker.save_to_file(clean_text, 'python_story.mp3')

speaker.runAndWait()

speaker.stop()