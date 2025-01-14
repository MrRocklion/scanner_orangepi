import serial
import time
import requests
import json

port = "/dev/ttyACM0"
baudrate = 9600 
timeout = 1 
url = "http://192.168.3.92:5000/api/qr_validator"
headers = {
    'Content-Type': 'application/json'
}
def make_petition(_data):
    try:
        response = requests.post(url, headers=headers, data=json.dumps(_data))
        if response.status_code == 200:
            response_data = response.json()
            authorization = response_data.get("authorization", False)
            if authorization:
                print("INGRESA")
            else:
                print("USUARIO NO PERTENECE")
            print("Authorization:", authorization)
        else:
            print("Error en la solicitud:", response.status_code)
            print("Detalles:", response.text)  
    except requests.RequestException as e:
        print("Error al realizar la petición:", e)
try:
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print(f"Escuchando en {port} a {baudrate} baudios. Presiona Ctrl+C para salir.")
        while True:
            if ser.in_waiting: 
                data = ser.readline().decode('utf-8', errors='ignore').strip()
                result_list = data.split("|")
                print({"qr debug >> "+data})
                current_timestamp = int(time.time() * 1000)
                if len(result_list) == 4:
                    if current_timestamp <= int(result_list[3]):
                        query_data = {
                            'user_id':result_list[0],
                            'tenant_id':result_list[1],
                            'iat':result_list[2],
                            'exp':result_list[3]
                        }
                        make_petition(query_data)
                    else:
                        print("CODIGO EXPIRADO")
                        
                elif len(result_list) == 3:
                    if current_timestamp <= int(result_list[2]):
                        query_data = {
                            'user_id':result_list[0],
                            'tenant_id':result_list[1],
                            'exp':result_list[2]
                        }
                        make_petition(query_data)
                    else:
                        print("CODIGO EXPIRADO")
                    pass
                else:
                    print("BAD QR CODE")




except serial.SerialException as e:
    print(f"Error al acceder al puerto {port}: {e}")
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
