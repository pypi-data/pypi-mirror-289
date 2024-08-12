from setuptools import setup, find_packages

setup(
    name="document-converter",  # Replace with your package name
    version="0.1.0",  # Initial release version
    packages=find_packages(),
    install_requires=[
        "pdf2image>=1.16.0",
        "opencv-python>=4.5.0",
        "pytesseract>=0.3.10",
        "Pillow>=8.0.0",
        "numpy>=1.21.0",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    entry_points={
        'console_scripts': [
            'document-converter=document_converter.document_converter:main',  # Optional: if you want a CLI tool
        ],
    },
    description="A package to convert various document types to plain text.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/document-converter",  # Replace with your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
