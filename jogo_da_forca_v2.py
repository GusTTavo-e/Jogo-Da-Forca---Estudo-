import random
from os import system, name

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def display_man(chances):
    
    stage = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stage[chances]
    

def game():
    limpar_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    lista_de_palavaras = ["banana","maça",'uva','abacaxi','laranja','melancia','abacate']
    palavra = random.choice(lista_de_palavaras)
    
    letras_descobertas = ['_' for letra in palavra]
    chances = 6
    
    #lista para as letras erradas
    letra_erradas = []
    
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letra_erradas))
        
        # Pedir a letra
        tentativa = input("Digite uma letra: ").lower()
        
        #verificando se a letras existe na palavra
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letra_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("\nParabéns! Vocês ganhou!")
            break
        
    if '_' in letras_descobertas:
        print("\nVocês perdeu! A palavra era:", palavra)
        
if __name__ == "__main__":
    display_man()
    game()
    print("\nParabéns. Vocês está aprendendo programação em Python com a DSA. :)\n")