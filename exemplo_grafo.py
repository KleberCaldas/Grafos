grafo   =   {   "a" : ["c"],
                "b" : ["c","e"],
                "c" : ["a","b","c","d","e"],
                "d" : ["c"],
                "e" : ["c","b"],
                "f" : [],
}

def gerar_arestas(grafo):
#exibe o conjunto de arestas do grafo
    arestas = []

    for nos in grafo:
        for vizinhanca in grafo[nos]:
            arestas.append((nos,vizinhanca))

    return arestas

def encontrar_no_isolado(grafo):
    #retorna a lista de nos isolados
    isolados = []

    for nos in grafo:
        if not grafo[nos]:
            isolados += nos
    return isolados

# Testando as funcoes

#print(gerar_arestas(grafo))
print(encontrar_no_isolado(grafo))