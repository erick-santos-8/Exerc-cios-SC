frequencia = {
    'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57,
    'F': 1.02, 'G': 1.30, 'H': 1.28, 'I': 6.18, 'J': 0.40,
    'K': 0.02, 'L': 2.78, 'M': 4.74, 'N': 5.05, 'O': 10.73,
    'P': 2.52, 'Q': 1.20, 'R': 6.53, 'S': 7.81, 'T': 4.34,
    'U': 4.63, 'V': 1.67, 'W': 0.01, 'X': 0.21, 'Y': 0.01, 'Z': 0.47
}

alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar(texto, chave):
    texto_cifrado = ""
    for c in texto:
        if c == " ":
            texto_cifrado += c
        elif alfabeto_min.find(c) != -1:
            pos = alfabeto_min.find(c) + chave
            if pos>25:
                pos = pos - 26
            texto_cifrado += alfabeto_min[pos]
        elif alfabeto_mai.find(c) != -1:
            pos = alfabeto_mai.find(c) + chave
            if pos>25:
                pos = pos - 26
            texto_cifrado += alfabeto_mai[pos]
        else:
            return "Texto com palavras fora do alfabeto!"
    return texto_cifrado

def decifrar(texto, chave):
    texto_decifrado = ""
    for c in texto:
        if c == " ":
            texto_decifrado += c
        elif alfabeto_min.find(c) != -1:
            pos = alfabeto_min.find(c) - chave
            texto_decifrado += alfabeto_min[pos]
        elif alfabeto_mai.find(c) != -1:
            pos = alfabeto_mai.find(c) - chave
            texto_decifrado += alfabeto_mai[pos]
    return texto_decifrado

texto_cifrar = input("Digite a mensagem: ")
chave = int(input("Digite a chave: (Padrão 3)"))

texto_cifrado = cifrar(texto_cifrar, chave)
print(texto_cifrado)
print(decifrar(texto_cifrado, chave))



def ataque_forca_bruta(texto):
    print("Ataque por Força Bruta:")
    for chave in range(1, 26):
        tentativa = decifrar(texto, chave)
        print(chave," : ",tentativa)

ataque_forca_bruta(texto_cifrado)