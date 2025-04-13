import qrcode

def MyQr(link, filename):
    qr = qrcode.QRCode(box_size= 30, border= 2)

    try:
        qr.add_data(link)
        qr_img = qr.make_image(fill_color = 'black', back_color = 'white')
        qr_img.save(filename)
        print("QR Created!")

    except Exception as a:
        print(f"error raised as {a}")

def MyQr_edit(link, filename, size, padd, fg, bg):
    qr = qrcode.QRCode(box_size= size, border= padd)

    try:
        qr.add_data(link)
        qr_img = qr.make_image(fill_color = fg, back_color = bg)
        qr_img.save(filename)

    except Exception as a:
        print(f"error raised as {a}")

Link = input("enter Link: ")
File = input("Enter filename: ")
Filename = File+'.png'

MyQr(link=Link, filename=Filename)


'''
Size = int(input("Enter Size: "))
Padd = int(input("Enter Padd: "))
Fg = input("Enter Color: ")
Bg = input("Enter BG: ")

MyQr_edit(link=Link, filename=Filename, padd=Padd, size=Size, fg=Fg, bg=Bg)
'''
