from PIL import Image, ImageFilter

imagemOriginal = Image.open('imagens/fachada_casa.png')


kernel1 = ImageFilter.Kernel((3,3), (1, 0, -1, 0, 0, 0, -1, 0, 1), 1, 0)
kernel2 = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1, 0)
kernel3 = ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)


filtro1 = imagemOriginal.filter(kernel1)
filtro2 = imagemOriginal.filter(kernel2)
filtro3 = imagemOriginal.filter(kernel3)


filtro1.save('imagens/fachada_casa_filtro_1.png')
filtro2.save('imagens/fachada_casa_filtro_2.png')
filtro3.save('imagens/fachada_casa_filtro_3.png')