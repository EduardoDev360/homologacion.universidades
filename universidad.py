import csv
import json

# Leer el archivo CSV
with open('instituciones_educativas.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# Leer el archivo JSON de universidades
with open('universidades.json', encoding='utf-8') as f:
    universidades = json.load(f)

# Definir diccionario de sinónimos de universidades
sinonimos = {}

# Buscar sinónimos de universidades en el archivo JSON
for u in universidades:
    nombre = u['Nombre '].lower()
    siglas = u['Siglas '].lower()
    sinonimos[nombre] = [nombre, siglas]
    sinonimos[siglas] = [nombre, siglas]

# Homologar universidades
homologadas = []
for row in data:
    candidate_id = row[0]
    value = row[1]
    homologada = None
    for u in universidades:
        nombre = u['Nombre '].lower()
        siglas = u['Siglas '].lower()
        if value.lower() in sinonimos[nombre] or value.lower() in sinonimos[siglas]:
            homologada = nombre
            break
    homologadas.append([candidate_id, value, homologada])

# Guardar resultados en archivos
with open('universidades_homologadas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['candidateId', 'value', 'universidad homologada'])
    writer.writerows(homologadas)

with open('sinonimo_universidades.json', 'w', encoding='utf-8') as f:
    json.dump([{'nombre_universidad': k, 'sinonimos': v} for k, v in sinonimos.items()], f, indent=4, ensure_ascii=False)
