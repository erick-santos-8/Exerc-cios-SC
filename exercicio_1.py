from collections import Counter

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
chave = int(input("Digite a chave: (Padrão 3): "))

texto_cifrado = cifrar(texto_cifrar, chave)
print(texto_cifrado)
print(decifrar(texto_cifrado, chave))



def ataque_forca_bruta(texto):
    print("Ataque por Força Bruta:")
    for chave in range(1, 26):
        tentativa = decifrar(texto, chave)
        print(chave," : ",tentativa)

ataque_forca_bruta(texto_cifrado)



frequencia = {
    'A': 13.9, 'B': 1.0, 'C': 4.4, 'D': 5.4, 'E': 12.2,
    'F': 1.0, 'G': 1.2, 'H': 0.8, 'I': 6.9, 'J': 0.4,
    'K': 0.1, 'L': 2.8, 'M': 4.2, 'N': 5.3, 'O': 10.8,
    'P': 2.9, 'Q': 0.9, 'R': 6.9, 'S': 7.9, 'T': 4.9,
    'U': 4.0, 'V': 1.3, 'W': 0.0, 'X': 0.3, 'Y': 0.0, 
    'Z': 0.4
}


def calcular_frequencia_texto(texto):
    texto = texto.upper()
    letras = [c for c in texto if c.isalpha()]
    total = len(letras)

    if total == 0:
        return {letra: 0.0 for letra in frequencia}
    
    contagem = Counter(letras)
    
    distribuicao = {}
    for letra in frequencia:
        distribuicao[letra] = (contagem.get(letra, 0) / total) * 100
    
    print(distribuicao)
    return distribuicao

def ataque_frequencia(texto):
    print("\nAtaque por Frequência:")
    menor_erro = float('inf')
    melhor_chave = None
    melhor_tentativa = ""
    
    for chave in range(1, 26):
        tentativa = decifrar(texto, chave)
        freq_tentativa = calcular_frequencia_texto(tentativa)
        
        # Cálculo do erro entre a frequência do texto e a da língua portuguesa
        erro = 0
        for letra in frequencia:
            erro += abs(frequencia[letra] - freq_tentativa.get(letra, 0))
        
        print(f"Chave {chave} → Erro total: {erro:.2f}")
        
        if erro < menor_erro:
            menor_erro = erro
            melhor_chave = chave
            melhor_tentativa = tentativa

    print(f"\n🔑 Melhor estimativa de chave: {melhor_chave}")
    print(f"📝 Texto decifrado com essa chave: {melhor_tentativa}")
    return melhor_chave, melhor_tentativa


ataque_frequencia(texto_cifrado)