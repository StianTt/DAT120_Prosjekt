"""Beregn veksten for den tenkte planten for hvert år i datasettet med bruk av funksjonen fra
del 1 oppgave h). Plott dette for hvert år i datasettet. Inkluder bare år hvor det er
temperaturdata for mesteparten av året, det må være data for minst 300 dager for at et år
skal være gyldig. Dette vil kreve at dere lager separate lister for hvert år som kan brukes som
parameter til funksjonen fra del 1 oppgave h)"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

#Henter funksjon fra del 1 av prosjektet
def beregn_plantevekst(temp_liste):
    total_vekst = 0
    for temperatur in temp_liste:
        if temperatur > 5:
            vekst = temperatur - 5
            total_vekst += vekst
    return total_vekst

# Leser data fra CSV-filen snoedybder_vaer_en_stasjon_dogn.csv
årslister = {}
with open('snoedybder_vaer_en_stasjon_dogn.csv', newline='', encoding='utf-8') as csvfile:
    leser = csv.DictReader(csvfile, delimiter=';')
    
    # Sjekk kolonnenavnene
    #print(leser.fieldnames)

    for rad in leser:
        # Endre dette til å matche det faktiske kolonnenavnet i dataene dine
        dato_str = rad['Tid(norsk']
        temperatur_str = rad['Middeltemperatur']

        try:
            # Prøv å konvertere dato til datetime-objekt
            dato = datetime.strptime(dato_str, '%d.%m.%Y')
        except ValueError:
            # Ignorer rader med ugyldige datoer
            #print(f'Ignorerer ugyldig dato: {dato_str}')
            print('Trend for plantevekst over tid opprettet. Rader med ugyldig dato ignorert')
            continue

        år = dato.year
        if år not in årslister:
            årslister[år] = []

        # Erstatt komma med prikk og konverter til float
        temperatur_str = temperatur_str.replace(',', '.')
        if temperatur_str and float(temperatur_str):
            årslister[år].append(float(temperatur_str))

# Beregn plantens vekst for hvert år og lagre resultatene
resultater = {}
for år, temperaturliste in årslister.items():
    # Bare inkluder år med minst 300 dager med temperaturdata
    if len(temperaturliste) >= 300:
        vekst = beregn_plantevekst(temperaturliste)
        resultater[år] = vekst

# Plot resultatene
år = list(resultater.keys())
vekst = list(resultater.values())

plt.plot(år, vekst, marker='o')
plt.xlabel('År')
plt.ylabel('Plantevekst')
plt.title('Plantevekst over tid')
plt.show()
