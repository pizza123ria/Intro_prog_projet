#imports
import numpy as np
import requests
from bs4 import BeautifulSoup

def cas_morts ():

	# récuperer des données (pas encore organisés)
	page = requests.get("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
	soup = BeautifulSoup(page.content, 'html.parser')
	tr_dans_td = soup.select('tr td')
	unorganized_data_cm = []
	for elt in tr_dans_td:
		unorganized_data_cm.append(elt.get_text())

	# editer Japan (+Diamond Princess) --> Japan
	unorganized_data_cm[unorganized_data_cm.index('Japan (+Diamond Princess)')]= 'Japan'


	# enlever MS Zadaam et structurer données en lignes
	data_structured=[]
	for i in range(len(unorganized_data_cm)-4): #les derniers 4 elements referent a MS Zadaam
		if i in range(0,len(unorganized_data_cm),4): #chaque pays contient 4 données 
			data_structured.append([unorganized_data_cm[i], unorganized_data_cm[i+1].replace(",",""), unorganized_data_cm[i+2].replace(",",""), unorganized_data_cm[i+3]]) #population et cas morts sont des entiers 

	# transformer liste en tableau numpy 2D
	cas_morts_tableau = np.array(data_structured)

	
	return cas_morts_tableau
	

cas_morts()

	
def population ():

	# récuperer des données (pas encore organisés)
	page = requests.get("https://www.worldometers.info/world-population/population-by-country/")
	soup = BeautifulSoup(page.content, 'html.parser')
	tr_dans_td_pop = soup.select('tr td')

	# put raw data into a list
	unorganized_data_pop =[]

	for elt in tr_dans_td_pop:
		unorganized_data_pop.append(elt.get_text())

	# put country and population into a list
	structured_data_pop = []
	for i in range (len(unorganized_data_pop)):
		if i in range(0, len(unorganized_data_pop),12): #12 données par pays
			structured_data_pop.append([unorganized_data_pop[i+1], unorganized_data_pop[i+2].replace(",","")]) #on est seulement interesse au pays et a la population
	
	# transformer liste en tableau numpy 2D
	population_tableau = np.array(structured_data_pop)

	return population_tableau

def capitales_coordonnees (): 

	#stream
	f = open("worldcities.csv", "r")
	content_worldcities = f.readlines()
	f.close()

	data_capitales = []
	for x in content_worldcities : 
		data_capitales.append(x.split(","))
		
	#sort data
	structured_data_capitales = []
	countries = set()
	for x in data_capitales : 
		if x[8] == 'primary' and not(x[4] in countries) : 
			countries.add(x[4])
			structured_data_capitales.append([x[4], x[2], x[3]])


	tableau_cap = np.array(structured_data_capitales)
	#print(tableau_cap[tableau_cap[:,0].argsort()])
	
	return tableau_cap
	

#capitales_coordonnees()

def donnees_completes():

	#changer les noms des pays dans le tableau_cap pour inclure les 
	#pays avec une autre ecriture dans l'intersection

	array_long_lat = capitales_coordonnees()
	
	array_long_lat[array_long_lat == "Antigua And Barbuda"] = "Antigua and Barbuda"
	array_long_lat[array_long_lat == "Bahamas The"] = "Bahamas"
	array_long_lat[array_long_lat == "Bosnia And Herzegovina"] = "Bosnia and Herzegovina"
	array_long_lat[array_long_lat == "Congo (Kinshasa)"] = "DR Congo"
	array_long_lat[array_long_lat == "Congo (Brazzaville)"] = "Congo"
	array_long_lat[array_long_lat == "Côte D’Ivoire"] = "Côte d'Ivoire"
	array_long_lat[array_long_lat == "Czechia"] = "Czech Republic (Czechia)"
	array_long_lat[array_long_lat == "Micronesia Federated States Of"] = "Micronesia"
	array_long_lat[array_long_lat == "Macedonia"] = "North Macedonia"
	array_long_lat[array_long_lat == "Saint Kitts And Nevis"] = "Saint Kitts & Nevis"
	array_long_lat[array_long_lat == "Saint Vincent And The Grenadines"] = "St. Vincent & Grenadines"
	array_long_lat[array_long_lat == "Sao Tome And Principe"] = "Sao Tome & Principe"
	array_long_lat[array_long_lat == "Trinidad And Tobago"] = "Trinidad and Tobago"

	array_pop = population()
	array_pop[array_pop == "Brunei "] = "Brunei"

	array_mort = cas_morts()
	array_mort[array_mort == "Brunei "] = "Brunei"

	#creer ensembles avec les pays issus de chaque tableau
	

	countries_cap = dict()
	for i in range(len(array_long_lat)): 
		countries_cap[array_long_lat[i, 0]] = i

	countries_pop = dict()
	for i in range(len(array_pop)): 
		countries_pop[array_pop[i, 0]] = i

	countries_mort = dict()
	for i in range(len(array_mort)): 
		countries_mort[array_mort[i, 0]] = i



	intersection = countries_cap.keys() & countries_pop.keys() & countries_mort.keys()
	#leftovers_cap = np.sort(list(countries_cap - intersection))
	#leftovers_pop = np.sort(list(countries_pop - intersection))
	#leftovers_mort = np.sort(list(countries_mort - intersection))
	
	final_array = []
	#for x in intersection : 
		#final_array.append([array_mort[countries_mort[x],0], array_mort[countries_mort[x],1], array_mort[countries_mort[x],2], array_mort[countries_mort[x],3], array_pop[countries_pop[x],1], array_long_lat[countries_cap[x],1],array_long_lat[countries_cap[x],2]])
	

	#transformer le tableau en CSV
	f = open("donnees_corona.csv", "w")
	f.write("pays,nombre de cas,nombre de décès,région,population,latitude,longitude\n")
	for x in intersection :
		f.write(array_mort[countries_mort[x],0] + "," + array_mort[countries_mort[x],1] + "," + array_mort[countries_mort[x],2] + "," + array_mort[countries_mort[x],3] + "," + array_pop[countries_pop[x],1] + "," + array_long_lat[countries_cap[x],1] + "," + array_long_lat[countries_cap[x],2] + "\n")
	f.close()

donnees_completes()

	





