import qrcode
from tkinter import filedialog
import time
valid_endings = (".com", ".org", ".co.uk", ".net", ".gov", ".app")
cool_art = """
░██████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗
██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║██╗██║██████╔╝██║░░╚═╝██║░░██║██║░░██║█████╗░░
╚██████╔╝██╔══██╗██║░░██╗██║░░██║██║░░██║██╔══╝░░
░╚═██╔═╝░██║░░██║╚█████╔╝╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═════╝░╚══════╝
"""
print(cool_art)
url = input("enter the url:").strip()
while not url.startswith("https://") or url.endswith(valid_endings):
    print("invaild url")
    url = input("enter the url:").strip()
else:
    file_path = filedialog.asksaveasfilename(
    title="Save QR Code",
    defaultextension=".png",
    filetypes=[("PNG Images", "*.png")]
)
    if not file_path:
        print("Save cancelled")
        exit()
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make(fit=True)
    print("generating image...")
    time.sleep(0.50)
    img = qr.make_image()
    img.save(file_path)
    print(f"done! saved at {file_path}")
    input("\n")