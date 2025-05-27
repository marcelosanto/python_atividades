import requests
from PIL import Image
from io import BytesIO

ASCII_CHARS = "@%#*+=-:.FlLF1 "


def redimensionar(imagem, nova_largura=50):
    largura, altura = imagem.size
    proporcao = altura / largura
    nova_altura = int(nova_largura * proporcao * 0.55)
    return imagem.resize((nova_largura, nova_altura))


def converter_ascii(imagem):
    imagem = imagem.convert("L")
    pixels = imagem.getdata()
    ascii_str = "".join(
        ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels)
    return ascii_str


def imagem_url_para_ascii(url, largura=50):
    try:
        response = requests.get(url)
        response.raise_for_status()
        imagem = Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Erro ao obter a imagem: {e}")
        return

    imagem = redimensionar(imagem, largura)
    ascii_str = converter_ascii(imagem)

    ascii_img = "\n".join(
        ascii_str[i:i+imagem.width] for i in range(0, len(ascii_str), imagem.width)
    )
    print(ascii_img)
