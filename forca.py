from random import seed
from random import randint
from os import system

def clear():
    name = system.__name__
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Forca:
    def __init__(self):
        self.worldList = ["BANANA", "CACHORRO", "BETERRABA", "COMPUTADOR", "FAXINA", "ELEVADOR", "MANDIOCA", "FARINHA", "GARRAFA", "TELEVISAO", "PLANETA", "DESENHO", "MARIONETE", "ELEFANTE", "AVESTRUZ", "IMPRESSORA"]
        self.word = self.worldList[randint(0, len(self.worldList)-1)]
        self.chances = 5
        self.tam = len(self.word)
        self.secreta = self.word
        self.falhas = []

    def exibeCorpo(self):
        if self.chances == 5:
            self.body = """            ---------
            |	    |
            |	    O
            |      /|\x5c
            |	    |
            |      / \x5c
            |
            ================
            ==	      ==		
            ==	      == """
        if self.chances == 4:
            self.body = """            ---------
            |	    |
            |	    O
            |      /|\x5c
            |	    |
            |      / 
            |
            ================
            ==	      ==		
            ==	      == """
        if self.chances == 3:
            self.body = """            ---------
            |	    |
            |	    O
            |      /|\x5c
            |	    |
            |      
            |
            ================
            ==	      ==		
            ==	      == """
        if self.chances == 2:
            self.body = """            ---------
            |	    |
            |	    O
            |      /|
            |	    |
            |      
            |
            ================
            ==	      ==		
            ==	      == """
        if self.chances == 1:
            self.body = """            ---------
            |	    |
            |	    O
            |       |
            |	    |
            |      
            |  ...última chance...
            ================
            ==	      ==		
            ==	      == """
        print(self.body)

    def iniciaSecreta(self):
        for i in range(0, self.tam):
            self.secreta = self.secreta.replace(self.word[i], "_")
    
    def exibePalavra(self):
        print("Palavra: ", end='')
        for i in range(self.tam):
            print(f"{self.secreta[i]} ", end='')
        print()

    def exibeTentativas(self):
        print(f"Tentativas restantes: {self.chances}")

    def tentativa(self):
        letra = input("=> Insira uma letra: ").upper()
        index = 0
        troca = list(self.secreta)
        temLetra = False
        for i in self.word:
            if i == letra:
                troca[index] = letra
                self.secreta = "".join(troca)
                temLetra = True
                        
            index = index+1

        if not temLetra:
            print(f"A palavra não tem a letra {letra}") 
            self.falhas.append(letra)
            self.chances = self.chances - 1
        
    def exibeFalhas(self):
        if len(self.falhas) > 0:
            print("Letras erradas: ", end='')
            for i in self.falhas:
                print(f"{i} ", end="")
            print()

    def acabaJogo(self):
        if self.secreta == self.word:
            print("Parabéns, você venceu!")
        elif self.chances == 0:
            print(f"Você perdeu... A palavra era {self.word}")

palavra = Forca()
palavra.iniciaSecreta()

while (palavra.chances > 0) and (palavra.secreta != palavra.word):
    clear()
    palavra.exibeCorpo()
    palavra.exibePalavra()
    palavra.exibeTentativas()
    palavra.exibeFalhas()
    palavra.tentativa()
    
palavra.acabaJogo()
