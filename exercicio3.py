from PIL import Image

imagemOriginal = Image.open('imagens/natureza_original.jpg')

matriz = imagemOriginal.load()

for y in range(imagemOriginal.size[0]):
    for x in range(imagemOriginal.size[1]):
        r = matriz [y,x][0]
        g = matriz [y,x][1]
        b = matriz [y,x][2]
        pixel = int((r + g + b) / 3)
        matriz [y,x] = (pixel, pixel, pixel)

imagemOriginal.save('imagens/natureza_cinza.jpg')





