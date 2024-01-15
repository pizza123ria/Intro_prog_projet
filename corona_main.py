#imports
from graphes_corona import camembert_regions
from graphes_corona import baton_mort_pays
from graphes_corona import baton_cas_pays
from graphes_corona import pire_baton_mort


premiere_question = input("Bonjour ! Voulez-vous avoir des informations sur le coronavirus ?\n")

affirmation = ["Oui", "oui", "yes", "Yes"]

ongoing_premier = True
while ongoing_premier:

	if premiere_question in affirmation:
		ongoing_second = True
		second_round = False
		while ongoing_second :
			if second_round : 
				clarification_3 = input("Voulez-vous plus d'information sur le coronavirus ?\nSi vous souhaitez continuer, tapez 'oui'. Sinon, je vous souhaite une bonne journée !\n")
				if not(clarification_3 in affirmation): 
					ongoing_premier = False
					break
			premier_choix = input("Je vous propose différentes options : \n" 
				"Tapez 1 pour voir le nombre des cas positifs et des décès dans les différentes régions du monde.\n"
				"Tapez 2 pour voir le nombre des décès dans les pays de votre choix.\n"
				"Tapez 3 pour voir le nombre des cas positifs dans les pays de votre choix.\n"
				"Tapez 4 pour voir les pays avec le plus grand nombre de décès par millions d'habitants. "
				"Vous choissisez combien des pays vous voulez comparer et vous pouvez fixer le nombre minimal d'habitants.\n"
				)
			if premier_choix == "1": 
				camembert_regions(True)
				second_round = True
			elif premier_choix == "2": 
				liste_pays = input("Desquels pays voulez-vous voir le nombre de décès ?\nDonnez une liste, s'il-vous plaît, des noms des pays écrits en anglais. Par exemple : ['France', 'Brazil']\n")
				baton_mort_pays(liste_pays, True)
				second_round = True
			elif premier_choix == "3": 
				liste_pays = input("Desquels pays voulez-vous voir le nombre des cas positifs ?\nDonnez une liste, s'il-vous plaît, des noms des pays écrits en anglais. Par exemple : ['France', 'Brazil']\n")
				baton_cas_pays(liste_pays, True)
				second_round = True
			elif premier_choix == "4": 
				k = int(input("Combien des pays les plus touchés par le coronavirus voulez vous voir ?\n"))
				reponse_optionelle = input("Voulez-vous indiquer un nombre minimal des habitants ?\nSi vous n'indiquez rien, il n'y aura pas de nombre minimal d'habitants.\n")
				if reponse_optionelle == "":
					pire_baton_mort(k, show=True)
					second_round = True
				else: 
					pire_baton_mort(k, int(reponse_optionelle), show=True)
					second_round = True
			else: 
				clarification_1 = input("Pardon, malheureusement je n'ai pas compris votre réponse.\nSi vous souhaitez continuer, tapez 'oui'. Sinon, je vous souhaite une bonne journée !\n")
				if clarification_1 in affirmation: 
					continue
				else: 
					ongoing_second = False
					ongoing_premier = False			
	else: 
		clarification_2 = input("Pardon, malheureusement je n'ai pas compris votre réponse.\nSi vous souhaitez continuer, tapez 'oui'. Sinon, je vous souhaite une bonne journée !\n")
		if clarification_2 in affirmation:
			premiere_question = "Oui"
		else: 
			ongoing_premier=False 




