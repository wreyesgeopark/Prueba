import requests

try:
    # Headers con la API key
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': 'x-api-key-WivKXD5Rfw5iYqijpDSqm_4EL6pMcc3QXeR9ZBuPyWE9wtwI'
    }

    # Hacer la solicitud POST
    response = requests.post(
        'https://prueba-8-l5ut.onrender.com/api/test-gpt',
        headers=headers,
        json={'message': 'Hola, ¿cómo estás?'}
    )
    
    # Imprimir información detallada de la respuesta
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response Body: {response.text}")

except Exception as e:
    print(f"Error: {str(e)}") 