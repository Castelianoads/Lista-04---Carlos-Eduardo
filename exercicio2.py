from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/natureza_original.jpg')


kernel1 = ImageFilter.Kernel((3,3), (0, -1, 0, -1, 5, -1, 0, -1, 0), 1, 0)
kernel2 = ImageFilter.Kernel((3, 3), (1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9), 1, 0)

filtro1 = imagemOriginal.filter(kernel1)
filtro2 = imagemOriginal.filter(kernel2)

filtro1.save('imagens/natureza_filtro_sharpen.jpg')
filtro2.save('imagens/natureza_filtro_sharpen_mediana.jpg')