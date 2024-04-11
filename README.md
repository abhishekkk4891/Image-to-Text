# Image-to-Text
This application extracts text from image and saves it in a text file

Input Image – First the image is loaded with the help for PLI(python image library). 
The PIL supports a vide range of image formats like .jpg, .png, .jpeg etc. we have to 
choose the path of the image from the dialog box.

Preprocessing – The image is pre-processed so that detection of the text in the image 
becomes easier. There are three steps for pre-process :-
1. Rescaling
2. Binarization 
3. Noise removal

1. Rescaling : OCR works best on 300 ppi(pixels per inch) or more. So if your 
image size is less than 300 ppi consider rescaling it to get your image ready for 
tesseract.

3. Binarization : Computers see images as array of pixel values as you know. And 
it will be better for our buddy tesseract to see and distinguish if there are only 
two colors either black and white. So he won’t get confused. So binarization is 
the process of converting the image to two binaries which will help tesseract to 
identify text easily but given a condition that it may fails if your image contrast 
is low or with dark background

5. Noise Removal : Noise are the grains present in the image. Noise in images 
make computers hard to work on. So there are many methods for noise removal.

Tesseract OCR engine - Tesseract tests the text lines to determine whether they are 
fixed pitch. Where it finds fixed pitch text, Tesseract chops the words into characters 
using the pitch, and disables the chopper and associator on these words for the word 
recognition step.

Post Process - Optical Character Recognition (OCR) Post Processing involves data 
cleaning steps for documents that were digitized, such as a book or a newspaper 
article. One step in this process is the identification and correction of spelling and 
grammar errors generated due to the flaws in the OCR system.

Text Output – The text which is extracted from the image is in the form of string. 

Saved text – The output text in form of string is then saved to a new file.
New file is created by opening a new file in write mode at the same location form 
where the image was imported.
