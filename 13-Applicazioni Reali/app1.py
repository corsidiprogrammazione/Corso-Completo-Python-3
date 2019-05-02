import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

contenuto = json.load(open("dizionario.json","r"))

def significato(parola):
	min_parola = parola.lower()
	if (min_parola in contenuto):
		return contenuto[min_parola]
	elif(len(get_close_matches(min_parola,contenuto.keys())) > 0):
		parola_simile = get_close_matches(min_parola,contenuto.keys())[0]
		domanda = (input(f'Intendevi {parola_simile} ? Scrivi Y per indicare sì e N per indicare no: ' ))
		if (domanda == 'Y'):
			return contenuto[parola_simile]
		else:
			return 'Programma concluso'
	else:
		return 'La parola non esiste'

parola = input('Inserisci la parola: ')

print(
significato(parola)
	)