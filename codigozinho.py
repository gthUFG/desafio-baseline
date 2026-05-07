from dotenv import load_dotenv
import os

load_dotenv("config.env")
import os

x = int(input("Fala um ponto x:"))
y = int(input("Fala um ponto y:"))

print(f"Que bacana! O seu ponto é o ({x},{y})")
print(f"A distância dele para o ponto registrado no ambiente é: ", end="")

env_x = int(os.getenv("PONTO_X"))
env_y = int(os.getenv("PONTO_Y"))

print(((x-env_x)**2 + (y-env_y)**2)**(1/2))