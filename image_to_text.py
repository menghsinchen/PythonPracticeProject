from PIL import Image
import pytesseract

# languages
class language():
    def __init__(self, name, dict = {}) -> None:
        self.name = name
        self.dict = dict

# english
EN = language("eng")

# traditonal chinese
TW = language("chi_tra", {
        "\n":"",
        " ":"",
        ",":"，",
        "(":"（",
        ")":"）",
        "——":"——",
        ":":"：",
        ";":"；",
        "?":"？",
    }) 

# simplified chinese
CN = language("chi_sim", {
        " ":"",
        "“":'"',
        "”":'"',
        ":":"：",
        ";":"；",
        "?":"？",
        "!":"！",
        "\n\n":"[changeline]",
        "\n":"",
        "[changeline]":"\n\n"
    })


def image_to_text(image_path: str, text_lang: language) -> str:
    """
    imput an image and output a text string by pytessseract
    """
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=text_lang.name)
    return text

def replace_string(mystring: str, text_lang: language) -> str:
    """
    replace original string with the setting of the language
    """
    for before, after in text_lang.dict.items():
        mystring = mystring.replace(before, after)
    return mystring

def image_to_text_replaced(image_path: str, text_lang: language) -> str:
    """
    image to text and then replace
    """
    return replace_string(image_to_text(image_path, text_lang), text_lang)

def save_text_to_file(text: str, output_path: str) -> None:
    """
    save text to file
    """
    f = open(output_path, 'w', encoding="utf-8")
    f.write(text)
    f.close()


image_path = "C:/Users/menghsinchen/Downloads/2023-08-02 23 51 29 (10).png"
output_path = "C:/Users/menghsinchen/Downloads/output.txt"

# text = image_to_text_replaced(r"C:\Users\menghsinchen\Downloads\helloworld.png", EN)
# text = image_to_text_replaced(r"C:\Users\menghsinchen\Downloads\2023-08-02 23 51 29 (10).png", TW)
text = image_to_text_replaced(image_path, TW)
# print(text)
save_text_to_file(text, output_path)