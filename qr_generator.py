import qrcode
import os

# Lista de códigos QR
codes = ["ce90e029", "ae82837d", "fd14ffeb", "7f6a6c68", "4480d177",
         "19b2e55f", "02df6448", "4464b6e9", "80dbdbda", "5af20413"]

# Crear la carpeta 'examples' si no existe
output_folder = "examples"
os.makedirs(output_folder, exist_ok=True)

# Generar y guardar los códigos QR en la carpeta 'examples'
for code in codes:
    img = qrcode.make(code)
    file_path = os.path.join(output_folder, f"{code}.png")
    with open(file_path, "wb") as f:
        img.save(f)

print(f"Códigos QR guardados en la carpeta '{output_folder}'")