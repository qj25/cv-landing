import qrcode

# Replace with your GitHub Pages URL
url = "https://qj25.github.io/cv-landing"

# Create QR (recommended: box_size=10 for good print quality)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("cv_qr.png")
print("Saved cv_qr.png — points to:", url)

