import string
from langdetect import detect

LETRAS = string.ascii_lowercase
NUMEROS = string.digits

def algoritmo_cesar(texto, clave, direccion="izquierda"):
    resultado = ""

    for caracter in texto:
        
        if caracter in LETRAS:
            indice = LETRAS.index(caracter)
            
            if direccion == "izquierda":
                nuevo_indice = (indice - clave) % len(LETRAS)
            else:
                nuevo_indice = (indice + clave) % len(LETRAS)
            
            resultado += LETRAS[nuevo_indice]

        elif caracter in NUMEROS:
            indice = NUMEROS.index(caracter)
            
            if direccion == "izquierda":
                nuevo_indice = (indice - clave) % len(NUMEROS)
            else:
                nuevo_indice = (indice + clave) % len(NUMEROS)
            
            resultado += NUMEROS[nuevo_indice]

        else:
            resultado += caracter

    return resultado


def fuerza_bruta(texto_cifrado):
    print("\nIntentando fuerza bruta...\n")
    
    for clave in range(max(len(LETRAS), len(NUMEROS))):
        
        texto_izq = algoritmo_cesar(texto_cifrado, clave, "izquierda")
        texto_der = algoritmo_cesar(texto_cifrado, clave, "derecha")

        try:
            if detect(texto_izq) == "es":
                print("DESCIFRADO (Izquierda)")
                print(f"Texto: {texto_izq}")
                print(f"Clave: {clave}")
                return

            if detect(texto_der) == "es":
                print("DESCIFRADO (Derecha)")
                print(f"Texto: {texto_der}")
                print(f"Clave: {clave}")
                return
        except:
            pass

    print("No se detectó texto en español.")


if __name__ == "__main__":
    texto_cifrado = input("Introduce el texto cifrado: ").lower()
    fuerza_bruta(texto_cifrado)
