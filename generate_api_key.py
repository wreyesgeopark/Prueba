import secrets
import string

def generate_api_key(prefix='x-api-key-'):
    # Longitud total de 48 caracteres (sin contar el prefijo)
    length = 48
    
    # Caracteres permitidos (letras, números y algunos símbolos seguros)
    alphabet = string.ascii_letters + string.digits + '_-'
    
    # Generar la parte aleatoria de la clave
    random_part = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    # Combinar el prefijo con la parte aleatoria
    api_key = f"{prefix}{random_part}"
    
    return api_key

if __name__ == "__main__":
    # Generar y mostrar la clave
    api_key = generate_api_key()
    print("\nAPI Key generada:")
    print("=" * 80)
    print(api_key)
    print("=" * 80)
    print("\nLongitud:", len(api_key))
    print("Esta clave es segura y única. Guárdala en un lugar seguro.") 