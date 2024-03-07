def mostrarCalculadora(textoDeDentro: str):
    linhas = textoDeDentro.split("\n")
    padding = 2
    maximoCaracteresPorLinha = 13
    linhasCalculadora = []

    linhas = [linha.strip() for linha in linhas]
    for linha in linhas:
        if (len(linha) <= maximoCaracteresPorLinha):
            linhasCalculadora.append(linha)
            continue
        palavras = linha.split(" ")
        palavras = [palavra.strip() for palavra in palavras]
        linhaAtual = ""
        for palavra in palavras:
            if (len(linhaAtual + palavra) > maximoCaracteresPorLinha):
                linhasCalculadora.append(linhaAtual)
                linhaAtual = palavra + " "
            else:
                linhaAtual += palavra + " "
        linhasCalculadora.append(linhaAtual)

    maiorComprimentoLinha = max([len(linha) for linha in linhasCalculadora])
    print(" " + "_" * maiorComprimentoLinha + 2 * padding * "_")
    for _ in range(padding):
        print("|" + " " * maiorComprimentoLinha + 2 * padding * " " + "|")
    for linha in linhasCalculadora:
        print("|" + padding * " " + linha.center(maiorComprimentoLinha, " ") + padding * " " + "|")
    for _ in range(padding):
        print("|" + padding * " " + " " * maiorComprimentoLinha + padding * " " + "|")
    print("|" + "_" * maiorComprimentoLinha + 2 * padding * "_" + "|")

