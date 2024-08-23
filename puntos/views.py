from django.shortcuts import render
import csv
import requests

# URL del CSV publicado
CSV_URL = 'https://docs.google.com/spreadsheets/d/1XQF9Q51Yth5IgFbB-7n5BweFDyFi9qwkUrcSqvSL4sI/pub?gid=0&single=true&output=csv'

def index1(request):
    if request.method == "POST":
        dni = request.POST.get("dni")
        # Lógica de búsqueda de puntos y nombre en la base de datos o Google Sheets
        resultado = search_in_csv(dni)  # Supongamos que esta es tu función de búsqueda
        if resultado:
            nombre = resultado['nombre']
            puntos = resultado['puntos']
            context = {'nombre': nombre, 'puntos': puntos}
        else:
            context = {'error': 'No se encontraron resultados para el DNI ingresado.'}
        return render(request, 'puntos/index.html', context)
    return render(request, 'puntos/index.html')


def index(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')

        if 'qr_image' in request.FILES:
            qr_image = request.FILES['qr_image']
            dni = scan_qr_code(qr_image)

        result = search_in_csv(dni)
        if result:
            context = {'nombre': result[1], 'puntos': result[2]}
        else:
            context = {'error': "DNI no encontrado."}
        
        return render(request, 'puntos/index.html', context)

    return render(request, 'puntos/index.html')


def search_in_csv(dni):
    response = requests.get(CSV_URL)
    response.encoding = 'utf-8'  # Asegúrate de que se maneje la codificación correctamente

    decoded_content = response.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    for row in cr:
        if row[0] == dni:
            return row
    return None

def scan_qr_code():
    return None