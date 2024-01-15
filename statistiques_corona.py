#imports
import numpy as np
from operator import itemgetter

def tableau_donnees(): 
""" Affiche un ta"""

	#stream
	f = open("donnees_corona.csv", "r")
	content = f.readlines()
	f.close()

	liste_content = []
	for x in content : 
		liste_content.append(np.array(x[:-1].split(",")))
	
	#transformer en tableau
	tableau_donnees_np = np.array(liste_content)

	return tableau_donnees_np

tableau_donnees()

def corona_par_region(): 

	tableau_np = tableau_donnees()

	nombre_de_cas = dict()
	nombre_de_deces = dict()
	population = dict()

	for x in tableau_np[1:]: 
		if not(x[3] in nombre_de_cas):
			nombre_de_cas[x[3]] = int(x[1])
			nombre_de_deces[x[3]]= int(x[2])
			population[x[3]]= int(x[4])
		else: 
			nombre_de_cas[x[3]] = nombre_de_cas[x[3]]+int(x[1])
			nombre_de_deces[x[3]] = nombre_de_deces[x[3]]+ int(x[2])
			population[x[3]] = population[x[3]]+ int(x[4])

	array_regions = []
	for x in population : 
		array_regions.append(np.array([x, population[x], nombre_de_deces[x], nombre_de_cas[x]]))

	tableau_reg = np.array(array_regions)
	
	return tableau_reg

def corona_par_pays(list_countries = tableau_donnees()[1:,0]): 

	tableau_complet = tableau_donnees()
	
	if (len(list_countries) == len(tableau_complet[1:,0])) and (list_countries == tableau_complet[1:,0]).all():
		tableau_tous = []
		for x in tableau_complet[1:] : 
			tableau_tous.append(np.array([x[0],(int(x[1])/int(x[4]))*1000000, (int(x[2])/int(x[4]))*1000000, x[4], x[5], x[6]]))
		tableau_tous = np.array(tableau_tous)
		return tableau_tous

	else : 
		table_shown = []
		for x in tableau_complet: 
			if x[0] in list_countries:
				table_shown.append(np.array([x[0],(int(x[1])/int(x[4]))*1000000, (int(x[2])/int(x[4]))*1000000, x[4], x[5], x[6]]))
		
		tableau_partiel = np.array(table_shown)
		return tableau_partiel


def donnees_pire_mort_pays(k, n=0):
	
	tableau_de_base = corona_par_pays()
	
	
	tableau_pire_mort = []
	for x in tableau_de_base: 
		if int(x[3]) >= n: 
			tableau_pire_mort.append([x[0], float(x[2]), x[4], x[5]])

	list_sorted = sorted(tableau_pire_mort, key=itemgetter(1), reverse=True)
	array_sorted = np.array(list_sorted)
	
	return array_sorted[:k]


def donnees_pire_cas_pays(k, n=0):
	
	tableau_de_base = corona_par_pays()

	tableau_pire_cas = []
	for x in tableau_de_base: 
		if int(x[3]) >= n: 
			tableau_pire_cas.append([x[0], float(x[2]), x[4], x[5]])


	list_sorted = sorted(tableau_pire_cas, key=itemgetter(1), reverse=True)
	tableau_ordonne = np.array(list_sorted)
	for x in tableau_ordonne: print(x)
	
	return tableau_ordonne[:k]






