import json
x = '''
{
    "imie": "Bartosz",
    "wiek": 20,
    "miasto": ["Poznan", "Jarocin"]
}
'''
#klucze i wartości muszą być w cudzysłowie podwójnym

json_string = json.loads(x)
print(json_string['wiek'])  # 20
print(json_string['miasto'])
#loads(str) bierze string w JSON i zamienia go na obiekt Python 


#dodawanie
json_string['dodawanie'] = True
new_json = json.dumps(json_string,indent=2,sort_keys=True)
#dumps(obj, indent) zamienia obiekt python (dict,str,list) na JSON
#argument indent powoduje zmianę prezentacji danych wyświetlanych z JSONa
print(new_json)

#Zadanie 1 - zaimportuj odpowiedni moduł JSON, stwórz słownik w python i przekonwertuj 
# go na JSON
 
#import json

slownik1 = {
    'Imie': 'Bartosz',
    'Wiek': 20,
    'Kierunek': 'Elektronika i Telekomunikacja'
}

json_slownik1 = json.dumps(slownik1,indent=2)
print(json_slownik1)

#Zadanie 2 - zaimportuj odpowiedni moduł JSON, stwórz słownik na podstawie danych z pliku 'slownik.txt'
#przekonwertuj go na JSON

#import json

with open('slownik.txt', 'r') as file:
    json_slownik2 = json.load(file)
print(json_slownik2)

#json.load() używamy bezpośrendio do odczytu z plików, natomiast json.loads() do odczytów ze string