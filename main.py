meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "NGL": "NOT GONNA LIE "Indicar que está admitiendo algo que puede considerarse extraño.",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Todavia no esta disponible")
  
