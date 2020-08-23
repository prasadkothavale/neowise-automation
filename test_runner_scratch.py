import pytesseract


def process_image(image):
    data = pytesseract.image_to_boxes(image)
    print(data)
