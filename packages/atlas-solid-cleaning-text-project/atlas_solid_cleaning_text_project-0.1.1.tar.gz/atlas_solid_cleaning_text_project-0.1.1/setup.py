from setuptools import setup, find_packages

setup(
    name="atlas_solid_cleaning_text_project",
    version="0.1.1",
    packages=find_packages(include=['scripts']),
    # install_requires=[
    #     "spacy",
    #     "elevenlabs",
    #     "pdfplumber",
    #     "openai",
    #     "regex",
    #     "num2words",
    # ],
    author="Str8-Up",
    # author_email="software@kampusmedia.ca",
    description="Processes PDF files through various scripts to extract, clean, format and export text from a PDF file",
    # long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    # url="https://github.com/Atlas-dev-project/clean_text",
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
)
