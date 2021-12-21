Packages used:
Pillow package - Python Imaging Library (expansion of PIL) is the de facto image processing package for Python 
language. It incorporates lightweight image processing tools that aids in editing, creating and saving images. 
Support for Python Imaging Library got discontinued in 2011, but a project named pillow forked the original PIL 
project and added Python3.x support to it. Pillow was announced as a replacement for PIL for future usage. Pillow 
supports a large number of image file formats including BMP, PNG, JPEG, and TIFF. The library encourages adding 
support for newer formats in the library by creating new file decoders. This module is not preloaded with Python. 
So to install it execute the following command in the command-line: 
 -> pip install pillow
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” 
the text embedded in images.

Python-tesseract - It is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation 
script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, 
including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print 
the recognized text instead of writing it to a file.

OS - The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s
standard utility modules. This module provides a portable way of using operating system-dependent functionality. 
The *os* and *os.path* modules include many functions to interact with the file system.

OpenCV - Python is a library of Python bindings designed to solve computer vision problems.
cv2.imread() method loads an image from the specified file. If the image cannot be read (because of missing file, 
improper permissions, unsupported or invalid format) then this method returns an empty matrix.

-------------------------------------------------------------------------------------------------------------------

There are two files,
1. Cropping and margin making
2. ImgToText

In 1st file it will crop the table image according to set by manually setting the margins. In the second file it 
will use tesseract package to convert that image into the text and will give the output.