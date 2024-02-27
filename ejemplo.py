meme_dict = {
    "cringe": "Algo excepcionalmente raro o embarazoso",
    "lol": "Una respuesta común a algo gracioso",
    "ROFL" : "Una respuesta a una broma",
    "sheesh" : "Ligera desaprobación",
    "creepy" : "Aterrador, siniestro",
    "aggro" : "Ponerse agresivo/enojado"
    }
    
word = input( "\n ¡Hola! Escribe una palabra que no entiendas: (FAVOR USAR MINUSCULAS) \n" )

if word in meme_dict.keys():
    print(f"{word} es : {meme_dict[word]}")
else:
    print(f"La palabra '{word}' es INVALIDA 🗣️.")
