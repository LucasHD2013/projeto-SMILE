meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor   ",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "abreviação da palavra *verdade*",
            "BISCOITAR": "postar algo pra chamar atenção",
            "HATER": "pessoa que esta constantemente criticando algo ou alguém",
            "VLW": "abreviação de *valeu*"}

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print(" palavra desconhecida até pelo app")
