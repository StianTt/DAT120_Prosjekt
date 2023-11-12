# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:21:27 2023

@author: aboos
"""


#imports
import matplotlib.pyplot as plt
import statistics

daily_data=[] #list inneholder hverdags data

#Funksjoner


def replace_commas_with_dots(input_string):#Funksjon endrer , til . og returnere float verdi
    result_string = input_string.replace(",", ".")
    return float(result_string)

def update_dictionary_key(dictionary, key):
    # Check if the key already exists in the dictionary
    if key in dictionary:
        # If the key exists, increase its value by one
        dictionary[key] += 1
    else:
        # If the key does not exist, create a new key with the value of 1
        dictionary[key] = 1


def penvarsdag(verdi,fast_verdi): #funksjon sjekker om penvarsdag
  if verdi<=fast_verdi:
    return verdi

def sjekk(verdi): #Funksjonen skjekker om det finnes verdig i Gjennomsnittlig skydekke (døgn)
  if verdi!="-":
     if verdi!="0":
      return replace_commas_with_dots(verdi)

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def plot_dictionary_bar(dictionary,Xaxis,Yaxis,plotlabel): #Funksjon som plotter dictionary
  keys = dictionary.keys()
  values = dictionary.values()
  plt.figure(figsize=(25, 6))
  plt.bar(keys, values)
  plt.xlabel(Xaxis)
  plt.ylabel(Yaxis)
  plt.title(plotlabel)
  plt.show()
  
  
  
  
  #oppgave G
#En feil som jeg vet om, Jeg finner ingen value i dictionay høyere enn 300, så plotter jeg alt

dic_skydekke={}

with open("snoedybder_vaer_en_stasjon_dogn.csv") as data:

  #for løkke fo å opprette daily data liste
  for line in data:
    daily_data.append(line.strip().split(";"))
  daily_data.pop(0) #slett første linje
  daily_data.pop(15707) #slett siste lije

  #for løkke for å finne data relevant til oppgave G
  for i in daily_data:
    date=i[2].strip().split(".") #liste for dato
    if sjekk(i[6]):
      if penvarsdag(sjekk(i[6]),3):
        update_dictionary_key(dic_skydekke, date[2])

plot_dictionary_bar(dic_skydekke,"År","Antal penværsdager", "År VS Antal penværsdager")


#Oppgave I
import matplotlib.pyplot as plt
def read_filtered_data_skydekke(file_path):
    with open(file_path, 'r') as file:
        linjer = file.readlines()
    Første_linje = linjer[0].strip().split(';')
    siste_linje=linjer[len(linjer)-1].strip().split(';')
    data = [line.strip().split(';') for line in linjer[1:len(linjer)-1]]
    gyldig_data=[]
    for day in data:
      if day[7] != '-':
        filtered_day=int(day[2][-4:])
        day[2]=filtered_day
        
        if day[7]!="0":
          filtered_skydekke_data=float(day[7].replace(',', '.'))
          day[7]=filtered_skydekke_data
          gyldig_data.append(day)
        else:
          filtered_skydekke_data=int(day[7])
          day[7]=filtered_skydekke_data
    return gyldig_data

#denne funksjonen for å fullføre krave på 300!! men det tar veldig lang tid, 80 minutter i hvertfall
def read_filtered_data_skydekke_300(file_path):
    with open(file_path, 'r') as file:
        linjer = file.readlines()
    Første_linje = linjer[0].strip().split(';')
    siste_linje=linjer[len(linjer)-1].strip().split(';')
    data = [line.strip().split(';') for line in linjer[1:len(linjer)-1]]
    gyldig_data=[]
    for day in data:
      if day[7] != '-':
        filtered_day=int(day[2][-4:])
        day[2]=filtered_day
        
        if day[7]!="0":
          filtered_skydekke_data=float(day[7].replace(',', '.'))
          day[7]=filtered_skydekke_data
          gyldig_data.append(day)
        else:
          filtered_skydekke_data=int(day[7])
          day[7]=filtered_skydekke_data
      valid=[dd for dd in gyldig_data if gyldig_data.count(dd[2]) >= 300]
    return valid

def dictionay_of_skydekke_data(list_of_data):
  deictionay_of_data={"År":[],"Høyeste middelvind":[],"Medianen for vindstyrke":[]}
  for day in list_of_data:
    år=day[2]
    if år not in deictionay_of_data["År"]:
      årlig=[da for da in list_of_data if da[2] == år]
      Høyeste_middelvind= max(d[7]for d in årlig)
      f=[d[7]for d in årlig]
      f.sort()
      Medianen_for_vindstyrke = f[len(f) // 2]
      deictionay_of_data["År"].append(år)
      deictionay_of_data["Høyeste middelvind"].append(Høyeste_middelvind)
      deictionay_of_data["Medianen for vindstyrke"].append(Medianen_for_vindstyrke)
  return deictionay_of_data

  #Oppgave I del 2
  data_skydekke=read_filtered_data_skydekke("snoedybder_vaer_en_stasjon_dogn.csv")
  dictionay_of_skydekke_data=dictionay_of_skydekke_data(data_skydekke)
  plt.figure(figsize=(10, 6))
  plt.plot(dictionay_of_skydekke_data["År"], dictionay_of_skydekke_data["Høyeste middelvind"], label="Høyeste middelvind")
  plt.plot(dictionay_of_skydekke_data["År"], dictionay_of_skydekke_data["Medianen for vindstyrke"], label="Medianen for vindstyrke")
  plt.xlabel("År")
  plt.ylabel("vindstyrke (m/s)")
  plt.title("Høyeste middelvind og Medianen for vindstyrke hvert år")
  plt.legend()
  plt.grid(True)
  plt.show()
  
  #oppgave H
def read_filtered_data_Middeltemperatur(file_path):
    with open(file_path, 'r') as file:
        linjer = file.readlines()
    Første_linje = linjer[0].strip().split(';')
    siste_linje=linjer[len(linjer)-1].strip().split(';')
    data = [line.strip().split(';') for line in linjer[1:len(linjer)-1]]
    
    gyldig_data=[]

    #fjerne data med "-", konvertere data med "0" til integer og andre data til float
    for day in data:
      if day[5] != '-':
        if day[5]=="0":
          filtered_day=int(day[5])
          day[5]=filtered_day
          gyldig_data.append(day)
        else:
          filtered_day=float(day[5].replace(',', '.'))
          day[5]=filtered_day
          gyldig_data.append(day)
    #rydde dato. splitte dato into to elementer (integers), måned og år 
    for day in gyldig_data:
      filtered_date=day[2]
      år=int(filtered_date[-4:])
      month=int(filtered_date[3:5])
      day.pop(2)
      day.insert(2,month)
      day.insert(3,år)
    return gyldig_data

def finn_gjennomsnitt(data):
  import statistics

  dictionay_of_tempratur={"År":[],"Måneder":[],"Gjennomsnittstemperaturen for hver måned":[],"Differanser":[]}

  for day in data:
    år=day[3]
    if år not in dictionay_of_tempratur["År"]:
      årlig=[da for da in data if day[3] == år]
      monthly=[1,2,3,4,5,6,7,8,9,10,11,12]
      monthes=[]
      averages=[]
    
      for month in monthly:
        counter=0
        sum=0
        for day in årlig:
          if day[2]==month:
            sum+=day[6]
            counter+=1
        average=round(sum/counter,3)
        monthes.append(month)
        averages.append(average)
      differences_betweeen_averages = [round(averages[i + 1] - averages[i]) for i in range(len(averages) - 1,3)]

      dictionay_of_tempratur["År"].append(år)
      dictionay_of_tempratur["Måneder"].append(monthes)
      dictionay_of_tempratur["Gjennomsnittstemperaturen for hver måned"].append(averages)
      dictionay_of_tempratur["Differanser"].append(differences_betweeen_averages)
  return dictionay_of_tempratur
  
x=read_filtered_data_Middeltemperatur("snoedybder_vaer_en_stasjon_dogn.csv")
y=finn_gjennomsnitt(x)

def plotting_dic_temp(dict):
  for key in dict:
    #print(dict[key])
    #print(len(dict[key]))
    if key=="År":
      for år in range (len(dict[key])):
        
        År=dict["År"]

        Måneder=dict["Måneder"]
        Gjennomsnittstemperaturen_for_hver_måned=dict["Gjennomsnittstemperaturen for hver måned"]
        Differanser=dict["Differanser"]    

        plt.plot(Måneder[år],Gjennomsnittstemperaturen_for_hver_måned[år], label="Gjennomsnittstemperaturen_for_hver_måned")
        plt.plot(Måneder[år][1:],Differanser[år], label="Differanser")


        plt.xlabel("Måneder")
        plt.ylabel("Gjennomsnittstemperaturen og  Differanser  (℃)")
        plt.title(f"Året {År[år]}\nGjennomsnittstemperaturen og  Differanser VS Måneder")
        #plt.legend(loc='right')
        plt.legend(loc='center right', bbox_to_anchor=(1.8, 0.5))
        plt.grid(True)

        plt.show()



  