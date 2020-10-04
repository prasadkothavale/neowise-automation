import pytesseract


def process_image(image):
    data = []
    lines = pytesseract.image_to_boxes(image).splitlines()
    for line in lines:
        data.append(line.split())

    text = ''
    for char in data:
        text += char[0]

    print(text)
