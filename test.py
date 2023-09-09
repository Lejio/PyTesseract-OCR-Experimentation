from PIL import Image
import pytesseract
import cv2

# Image pre-processing.
image = cv2.imread('./high_image_noise_sample.jpg')
# image = cv2.imread('./low_image_noise_sample.jpg')

# Changing the size of the image to a more favoriable size for OCR.
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# Graying out the image.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform tesseract OCR.
text = pytesseract.image_to_string(gray, config ='--psm 6')

print(text)

#######################################
# RESULTS ---
#######################################
# 
# The OCR returns pretty accurate 
# image-to-text, however, even with the
# low_image_noise_sample plus the cv2 
# image pre-processing it still c
# ontains some noticeable errors.
#######################################