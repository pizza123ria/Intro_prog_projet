#imports
import numpy as np
import matplotlib.pyplot as plt
from statistiques_corona import corona_par_region 
from statistiques_corona import tableau_donnees
from statistiques_corona import corona_par_pays
from statistiques_corona import donnees_pire_mort_pays

def camembert_regions(show=False):
	"""Affiche deux graphiques circulaires, un avec les décès par région et un avec les cas par région"""
	
	tableau_donnees_reg = corona_par_region()
	
 
	#camembert morts par region
	plt.figure(figsize = (8, 8))
	plt.title('Décès par région')
	lab = tableau_donnees_reg[:,0]
	valeurs = tableau_donnees_reg[:,2]
	ax = plt.pie(valeurs, autopct = "%0.1f%%", pctdistance=1.15, labeldistance = 1.25)
	plt.legend(ax[0], lab, loc="center left", bbox_to_anchor=(1,0,0.5,1))
	plt.savefig('./graphes/camembert_morts_region.png', bbox_inches='tight', dpi = 1200)
	if show :
		plt.show()

	#camembert cas par region
	plt.figure(figsize = (8, 8))
	plt.title('Nombre des cas positifs par région')
	lab = tableau_donnees_reg[:,0]
	valeurs = tableau_donnees_reg[:,3]
	ax = plt.pie(valeurs, autopct = "%0.1f%%", pctdistance=1.15, labeldistance = 1.25)
	plt.legend(ax[0], lab, loc="center left", bbox_to_anchor=(1,0,0.5,1))
	plt.savefig('./graphes/camembert_cas_region.png', bbox_inches='tight', dpi = 1200)
	if show :
		plt.show()


def baton_mort_pays(liste_pays, show=False):
	""" Affiche un histogramme avec les décès par pays """

	tableau_base = tableau_donnees()

	nombre_mort = []
	pays_melanges = []
	for x in tableau_base:
		if x[0] in liste_pays:
			nombre_mort.append(int(x[2]))
			pays_melanges.append(x[0])

	plt.title('Décès par pays')
	x_pos = np.linspace(1, len(nombre_mort), len(nombre_mort))
	plt.bar(x_pos, nombre_mort, color = 'blue')
	plt.xticks(x_pos, pays_melanges)
	plt.ylabel('Décès')
	plt.savefig('./graphes/baton_mort.png', bbox_inches='tight', dpi = 1200) 
	if show :
		plt.show()

		
def baton_cas_pays(liste_pays, show=False):
	""" Affiche un histogramme avec les cas positifs par pays """

	tableau_base = tableau_donnees()

	nombre_cas = []
	pays_melanges = []
	for x in tableau_base:
		if x[0] in liste_pays:
			nombre_cas.append(int(x[1]))
			pays_melanges.append(x[0])

	plt.title('Cas par pays')
	x_pos = np.linspace(1, len(nombre_cas), len(nombre_cas))
	plt.bar(x_pos, nombre_cas, color = 'blue')
	plt.xticks(x_pos, pays_melanges)
	plt.ylabel('Cas')
	plt.savefig('./graphes/baton_cas.png', bbox_inches='tight', dpi = 1200) 
	if show :
		plt.show()


def pire_baton_mort(k, n=0, show=False): 
	""" Affiche un histogramme avec les k pays avec des taux de décès par millions d'habitants les plus grands parmi les pays avec au moins n habitants."""

	
	tableau_pire_mort = donnees_pire_mort_pays(k,n)
	tableau_taux = []
	for x in tableau_pire_mort: tableau_taux.append(float(x[1]))
	
	plt.title('Pires taux de décès par pays')
	x_pos = np.linspace(1, len(tableau_taux), len(tableau_taux))
	plt.bar(x_pos, tableau_taux, color = 'blue')
	plt.xticks(x_pos, tableau_pire_mort[:,0])
	plt.ylabel('Décès par million habitants')
	plt.savefig('./graphes/pire_baton_mort.png', bbox_inches='tight', dpi = 1200) 
	if show :
		plt.show()






