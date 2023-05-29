import qrcode

#URL currículo no github
curriculo_url = "https://github.com/brukorczak/curriculo/blob/main/CV_Bruna_Korczak.pdf"

#Criando o QR code com a URL do currículo
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(curriculo_url)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

#Salvando img do QR code
img.save('C:/Users/Bruna/OneDrive/Documentos/brubs/qrimg/myqrcode.png')