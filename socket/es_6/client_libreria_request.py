import requests, sys

if len(sys.argv) < 2:
    print("Errore negli argomenti <url>")
    print("Esempio: $ python3 client_libreria_request.py http://libero.it")
    exit()

response = requests.get(sys.argv[1])

print(response.headers)
