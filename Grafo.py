# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:09:33 2019

@author: Kleber
"""
# Classe simples de grafo com principais funcionalidades

class Grafo(object):
    
    """
         inicializa um objeto do tipo grafo
         se nao tiver dicionario ou nada for dado,
         um dicionario vazio sera usado
    """
    def __init__(self, grafo_dicio=None):
        if grafo_dicio == None:
            grafo_dicio = {}
        self.__grafo_dicio = grafo_dicio
     
    
    
    """
         retorna o conjunto de vertices do grafo
    """
    def getVertices(self):
        return list(self.__grafo_dicio.keys())
    
    
    
    """
        adiciona um vertice ao grafo
    """
    def addVertices(self, vertice):
        if vertice not in self.__grafo_dicio:
            self.__grafo_dicio[vertice] = []
        print("Vertice foi adicionado!")
            
    
        
    """
       retorna o conjunto de arestas do grafo
    """
    def getArestas(self):
        return self.__gerarArestas()



    """
        adiciona arestas
    """
    def addArestas(self, aresta):
        
        aresta = set(aresta)
        (vertice1, vertice2) = tuple(aresta)
        
        if vertice1 in self.__grafo_dicio:
            self.__grafo_dicio[vertice1].append(vertice2)
        else:
            self.__grafo_dicio[vertice1] = [vertice2]
        print("Aresta adicionada!")
    

    """
        metodo estatico criador de arestas do grafo
    """
    def __gerarArestas(self):
        
        arestas = []
        
        for vertice in self.__grafo_dicio:
            for vizinhanca in self.__grafo_dicio[vertice]:
                if{vizinhanca, vertice} not in arestas:
                    arestas.append({vertice, vizinhanca})
        
        return arestas
