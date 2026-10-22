import qrcode
import json
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'data.json')
with open(json_path, 'r') as f:
    data = json.load(f)
cool_art = """

░██████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗
██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║██╗██║██████╔╝██║░░╚═╝██║░░██║██║░░██║█████╗░░
╚██████╔╝██╔══██╗██║░░██╗██║░░██║██║░░██║██╔══╝░░
░╚═██╔═╝░██║░░██║╚█████╔╝╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═════╝░╚══════╝
"""
print(cool_art)
if data['users-path'] is not None:
    print("file path found")
    file_path = data['users-path']
else:
    #be mindful of clashing file names
    print("make sure you type in the full file path including the file type")
    print("note this will save for next time")
    file_path = input("were do you want to save the QRcode:")
    while not file_path.endswith('.png'):
        os.system("cls")
        print("file must end with .png")
        file_path = input("were do you want to save the QRcode:")
    data['users-path'] = file_path
url = input("enter the url:").strip()
os.system("cls")
qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save(file_path)
print(f"QRcode generated at {file_path}")
with open( json_path, 'w') as f:
    json.dump(data, f, indent=4)
print("file path saved for next time")
input("\npress enter to exit")
input("\n")