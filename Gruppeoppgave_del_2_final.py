import csv
from datetime import datetime
import matplotlib.pyplot as plt
import statistics

#  Oppgave a
def read_weather_data(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) 
        for row in reader:
            name, station_id, date_str, snow_depth_str, precipitation_str, temperature_str, cloud_cover_str, wind_speed_str, *_ = row
            if not date_str:  
                continue
            try:
                date = datetime.strptime(date_str, '%d.%m.%Y')
            except ValueError:
                print(f"Invalid date format for {date_str}. Skipping this row.")
                continue
            if not date_str:  
                continue
            date = datetime.strptime(date_str, '%d.%m.%Y')
            snow_depth = float(snow_depth_str.replace(',', '.')) if snow_depth_str != '-' else 0.0
            precipitation = float(precipitation_str.replace(',', '.')) if precipitation_str != '-' else 0.0
            temperature = float(temperature_str.replace(',', '.')) if temperature_str != '-' else 0.0
            cloud_cover = float(cloud_cover_str.replace(',', '.')) if cloud_cover_str != '-' else 0.0  # Replace comma with period
            wind_speed = float(wind_speed_str.replace(',', '.')) if wind_speed_str != '-' else 0.0
        
            year = date.year
            if year not in data:
                data[year] = {
                    'name': name,
                    'station_id': station_id,
                    'years': {},
                }
            data[year]['years'][date] = {
                'date': date,
                'snow_depth': snow_depth,
                'precipitation': precipitation,
                'temperature': temperature,
                'cloud_cover': cloud_cover,
                'wind_speed': wind_speed,
            }

    return data

# Oppgave b
def calculate_skiing_days(data):
    skiing_data = [] 
    for year, year_data in data.items():
        skiing_days = 0
        year = int(year) 
        winter_start = datetime(year - 1, 10, 1)  
        winter_end = datetime(year, 6, 30)  
        for date, daily_data in year_data['years'].items():
            if winter_start <= date <= winter_end:
                if daily_data['snow_depth'] >= 20:
                    skiing_days += 1
        print(f"Year {year}: {skiing_days} skiing days")
        skiing_data.append(skiing_days)

    return skiing_data

#  Oppgave c
def calculate_skiing_trend(data):
    skiing_data = calculate_skiing_days(data)
    
    n = len(skiing_data)

    def a(i, n, x, y):
        avg_x = sum(x) / len(x)
        avg_y = sum(y) / len(y)
        summert_a_over = sum((x[i] - avg_x) * (y[i] - avg_y) for i in range(n))
        summert_a_under = sum((x[i] - avg_x) ** 2 for i in range(n))
        summert_a = summert_a_over / summert_a_under if summert_a_under != 0 else 0
        return summert_a

    def b(a, x, y):
        avg_x = sum(x) / len(x)
        avg_y = sum(y) / len(y)
        summert_b = avg_y - a * avg_x
        return summert_b

    resultat_a = a(0, n, list(data.keys()), skiing_data)
    resultat_b = b(resultat_a, list(data.keys()), skiing_data)

    trend = "stigende" if resultat_a > 0 else "synkende" if resultat_a < 0 else "uforandret"

    return resultat_a, resultat_b, trend

filename = input("Enter the CSV file name (e.g., weather_data.csv): ")

weather_data = read_weather_data(filename)

trend_a, trend_b, skiing_trend = calculate_skiing_trend(weather_data)

print(f"Trend for skiing days (a value): {trend_a}")
print(f"Intercept for skiing days (b value): {trend_b}")
print(f"Skiing days trend: {skiing_trend}")


#Oppgave d
def plot_skifore_og_trend(data, trend_a, trend_b):
    gyldige_aar = []
    skifore = []

    for year, year_data in data.items():
        if 'years' not in year_data or len(year_data['years']) < 200:
            continue

        gyldige_aar.append(year)
        skifore.append(sum(1 for daily_data in year_data['years'].values() if daily_data['snow_depth'] >= 20))

    plt.scatter(gyldige_aar, skifore, label='Skiføre')
    trend_line_start = trend_a * min(gyldige_aar) + trend_b
    trend_line_end = trend_a * max(gyldige_aar) + trend_b
    plt.plot([min(gyldige_aar), max(gyldige_aar)], [trend_line_start, trend_line_end], label='Trend Linje', linestyle='--')
    plt.xlabel('Skisesong (år)')
    plt.ylabel('Dager med skiføre')
    plt.title('Antall dager med skiføre og trend')
    plt.legend()
    plt.show()

plot_skifore_og_trend(weather_data, trend_a, trend_b)


#Oppgave e
def beregn_plantevekst(temp_liste):
    total_vekst = 0
    for temperatur in temp_liste:
        if temperatur > 5:
            vekst = temperatur - 5
            total_vekst += vekst
    return total_vekst

årslister = {}
#with open('snoedybder_vaer_en_stasjon_dogn.csv', newline='', encoding='utf-8') as csvfile:
with open(filename, 'r' , newline='', encoding='utf-8') as csvfile:
    leser = csv.DictReader(csvfile, delimiter=';')

    for rad in leser:
        dato_str = rad['Tid(norsk']
        temperatur_str = rad['Middeltemperatur']

        try:
            dato = datetime.strptime(dato_str, '%d.%m.%Y')
        except ValueError:
            print('Trend for plantevekst over tid opprettet. Rader med ugyldig dato ignorert')
            continue

        år = dato.year
        if år not in årslister:
            årslister[år] = []
            
        temperatur_str = temperatur_str.replace(',', '.')
        if temperatur_str and float(temperatur_str):
            årslister[år].append(float(temperatur_str))


resultater = {}
for år, temperaturliste in årslister.items():
    if len(temperaturliste) >= 300:
        vekst = beregn_plantevekst(temperaturliste)
        resultater[år] = vekst

år = list(resultater.keys())
vekst = list(resultater.values())

plt.plot(år, vekst, marker='o')
plt.xlabel('År')
plt.ylabel('Plantevekst')
plt.title('Plantevekst over tid')
plt.show()


#Oppgave g
def lengste_null_sekvens(liste):
    maks_lengde = 0
    gjeldende_lengde = 0

    for tall in liste:
        if tall == 0:
            gjeldende_lengde += 1
            maks_lengde = max(maks_lengde, gjeldende_lengde)
        else:
            gjeldende_lengde = 0

    return maks_lengde

def plot_lengste_null_sekvens(data):
    gyldige_aar = []
    lengste_torkeperiode = []

    for year, year_data in data.items():
        if len(year_data['years']) < 300:
            continue

        gyldige_aar.append(year)
        precipitation_data = [daily_data['precipitation'] for daily_data in year_data['years'].values()]
        lengste_torkeperiode.append(lengste_null_sekvens(precipitation_data))

    plt.bar(gyldige_aar, lengste_torkeperiode, color='orange')
    plt.xlabel('År')
    plt.ylabel('Lengste tørkeperiode (Dager)')
    plt.title('Lengste tørkeperiode hvert år')
    plt.show()

plot_lengste_null_sekvens(weather_data)

#Oppgave i
import matplotlib.pyplot as plt

def replace_commas_with_dots(input_string):
    result_string = input_string.replace(",", ".")
    return float(result_string)

def update_dictionary_key(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def penvarsdag(verdi, fast_verdi):
    return verdi <= fast_verdi

def sjekk(verdi):
    try:
        if verdi != "-" and verdi != "0":
            return replace_commas_with_dots(verdi)
        return None
    except ValueError:
        return None

def plot_dictionary_bar(dictionary, Xaxis, Yaxis, plotlabel):
    keys = dictionary.keys()
    values = dictionary.values()
    plt.figure(figsize=(25, 6))
    plt.bar(keys, values)
    plt.xlabel(Xaxis)
    plt.ylabel(Yaxis)
    plt.title(plotlabel)
    plt.show()

daily_data = []
dic_skydekke = {}
entries_per_year = {}

with open("snoedybder_vaer_en_stasjon_dogn.csv") as data:
    next(data)  
    
    for line_number, line in enumerate(data, start=2):
        if line_number == 15709:
            continue

        entry = line.strip().split(";")
        
        if len(entry) < 7:
            print(f"Error reading line {line_number}: Not enough elements")
            continue

        try:
            date = entry[2].strip().split(".")
            year = date[2]

            if year in entries_per_year:
                entries_per_year[year] += 1
            else:
                entries_per_year[year] = 1

            if sjekk(entry[6]) is not None and penvarsdag(sjekk(entry[6]), 3):
                update_dictionary_key(dic_skydekke, year)
        except (IndexError, ValueError) as e:
            print(f"Error processing line {line_number}: {e}")
            print(f"Line causing the error: {entry}")

# Filtrer ut år med mindre enn 300 oppføringer
dic_skydekke = {year: count for year, count in dic_skydekke.items() if entries_per_year.get(year, 0) >= 300}

plot_dictionary_bar(dic_skydekke, "År", "Antall penværsdager", "År VS Antall penværsdager")


#Oppgave H
def read_filtered_data_Wind(file_path):
    with open(file_path, 'r') as file:
        linjer = file.readlines()
    data = [line.strip().split(';') for line in linjer[1:len(linjer) - 1]]

    gyldig_data = []

    for day in data:
        if day[5] != '-':
            if day[5] == "0":
                filtered_day = int(day[5])
                day[5] = filtered_day
                gyldig_data.append(day)
            else:
                filtered_day = float(day[5].replace(',', '').replace('.', '', day[5].count('.') - 1))
                day[5] = filtered_day
                gyldig_data.append(day)

    for day in gyldig_data:
        filtered_date = day[2]
        år = int(filtered_date[-4:])
        month = int(filtered_date[3:5])
        day.pop(2)
        day.insert(2, month)
        day.insert(3, år)

    return gyldig_data

def find_wind_stats(data):
    wind_stats = {"År": [], "Høyeste Middelvind": [], "Median Vindstyrke": []}

    for år in set(day[3] for day in data):
        årlig = [da for da in data if da[3] == år and da[5] != '-']
        if len(årlig) >= 300:
            vindstyrker = [float(da[5].replace(',', '').replace('.', '', da[5].count('.') - 1)) for da in årlig]
            høyeste_middelvind = max(statistics.mean(vindstyrker) for da in årlig)
            median_vindstyrke = statistics.median(vindstyrker)

            wind_stats["År"].append(år)
            wind_stats["Høyeste Middelvind"].append(høyeste_middelvind)
            wind_stats["Median Vindstyrke"].append(median_vindstyrke)

    return wind_stats

def plot_wind_stats(stats):
    plt.figure(figsize=(10, 6))

    plt.plot(stats["År"], stats["Høyeste Middelvind"], marker='o', linestyle='-', color='blue', label='Høyeste Middelvind')
    plt.plot(stats["År"], stats["Median Vindstyrke"], marker='o', linestyle='-', color='orange', label='Median Vindstyrke')

    plt.xlabel("År")
    plt.ylabel("Vindstyrke (m/s)")
    plt.title("Høyeste Middelvind og Median Vindstyrke for Hvert År")
    plt.legend()
    plt.grid(True)
    plt.show()

wind_data = read_filtered_data_Wind(filename)
wind_stats = find_wind_stats(wind_data)
plot_wind_stats(wind_stats)

#Oppgave I
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader) 

    data = [row for row in reader if len(row) >= 6 and row[0] != 'Data']

dates = [row[2] for row in data]

filtered_data = []
for date, row in zip(dates, data):
    try:
        date_obj = datetime.strptime(date, '%d.%m.%Y')
        temp = row[5].replace(',', '.')
        temp = float(temp)  
        filtered_data.append((date_obj, temp))
    except (ValueError, IndexError):
        print(f"Ugyldig data oppdaget: {row}")

# Sjekk om det er data å behandle
if not filtered_data:
    print("Ingen gyldig data tilgjengelig for behandling.")
else:
    dates, temperatures = zip(*filtered_data)

    monthly_avg = {}
    for date, temp in zip(dates, temperatures):
        key = (date.year, date.month)
        if key in monthly_avg:
            monthly_avg[key].append(temp)
        else:
            monthly_avg[key] = [temp]

    sorted_months = sorted(monthly_avg.keys(), key=lambda x: (x[0], x[1]))

    avg_temps = [sum(monthly_avg[key]) / len(monthly_avg[key]) for key in sorted_months]
    differences = [avg_temps[i] - avg_temps[i - 1] if i > 0 else 0 for i in range(len(avg_temps))]

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(sorted_months, avg_temps, marker='o')
    plt.title('Gjennomsnittstemperaturer per måned')
    plt.xlabel('Måned og År')
    plt.ylabel('Gjennomsnittstemperatur (°C)')

    plt.subplot(2, 1, 2)
    plt.plot(sorted_months, differences, marker='o', color='r')
    plt.title('Differanser mellom påfølgende måneder')
    plt.xlabel('Måned og År')
    plt.ylabel('Differanse i temperatur (°C)')

    plt.tight_layout()

    plt.show()
