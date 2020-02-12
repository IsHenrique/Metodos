import math

def tabelanormal(confianca):
    confianca = confianca / 2
    confianca = confianca / 100
    confianca = '{0:.4f}'.format(confianca)

    arquivo = open("Tabela.txt", 'r')
    dados = {}
    #coluna = ['0','0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09']
    for index, number in enumerate(arquivo):
        linha = number.split(" ")
        linha[-1] = linha[-1].strip()
        if (index != 0):
            for i, linha in enumerate(linha):
                if (i == 0):
                    aux = (float(linha) + float(coluna[i]))
                else:
                    dados[linha] = (float(aux) + float(coluna[i]))
        else:
            coluna = linha

    if confianca in dados:
        zcrit = dados[confianca]

    return zcrit


def tabelastuden(p, gl):
    coluna = ['0', '0.95', '0.90', '0.80', '0.70', '0.60', '0.50', '0.40', '0.30', '0.20', '0.10', '0.05', '0.02 ', '0.01', '0.001']
    arquivo = open("TabelaTStudent.txt", 'r')
    dados = {}
    for index, number in enumerate(arquivo):
        linha = number.split(" ")
        linha[-1] = linha[-1].strip()
        if (index != 0):
            for i, numero in enumerate(linha):
                if (i == 0):
                    dados[float(numero) + float(coluna[i])] = 0
                    Valor = numero
                else:
                    dados[float(Valor) + float(coluna[i])] = numero
    return float(dados[(float(gl) + float(p))])

def calculodeN(amostra):
    frequencia = {}
    for item in amostra:
        if item in frequencia:
            frequencia[item] = frequencia[item] + 1
        else:
            frequencia[item] = 1
    somafi = sum([float(x) for x in frequencia.values()])
    return somafi

def mediaamostral(frequencia, amostra):
    soma = 0
    for key in frequencia:
        soma = soma + float(key) * frequencia[key]
    mediaamostral = soma / calculodeN(amostra)
    return mediaamostral

def frequencia(amostra):
    frequencia = {}
    for item in amostra:
        if item in frequencia:
            frequencia[item] = frequencia[item] + 1
        else:
            frequencia[item] = 1
    return(frequencia)

def calculodeS(frequencia, mediaamostral, amostra):
    variancia = 0
    for key in frequencia:
        variancia = variancia + frequencia[key] * ((float(key) - mediaamostral) ** 2) / (calculodeN(amostra) - 1)
    desviopadraoamostral = math.sqrt(variancia)
    return desviopadraoamostral

def intervaloconfiancadesvio(media, n, desvio, confianca):
    zcrit = tabelanormal(confianca)
    aux = zcrit * (desvio / (math.sqrt(n)))
    mais = media + aux
    menos = media - aux
    return mais, menos

def intervaloconfiancasemdesvio(amostra, confianca):
    amostra = amostra
    confianca = confianca
    n = calculodeN(amostra)
    confifloat = confianca / 100
    p = round(1 - confifloat, 2)
    tcrit = tabelastuden(p, (n - 1))
    amostrafrequencia = frequencia(amostra)
    mediaamostralaux = mediaamostral(amostrafrequencia, amostra)
    aux = tcrit * (calculodeS(amostrafrequencia, mediaamostralaux,amostra) / (math.sqrt(n)))
    mais = mediaamostralaux + aux
    menos = mediaamostralaux - aux
    return mais, menos

def populacional(sucesso, totalamostra, confianca):
    p = sucesso / totalamostra
    raiz = math.sqrt(p*(1-p)/totalamostra)
    zcrit = tabelanormal(confianca)
    mais = p + (zcrit*raiz)
    menos = p - (zcrit*raiz)

    return mais, menos



