# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:29:32 2019

@author: Kleber
"""

from Grafo import Grafo

if __name__ == "__main__":
    g = { 
            "a" : ["d"],
            "b" : ["c"],
            "c" : ["b", "d", "e"],
            "d" : ["a", "c"],
            "e" : ["c"],
            "f" : []
        }


grafo = Grafo(g)


print(grafo.getVertices())

grafo.addVertices("k")

print(grafo.getVertices())

grafo.addArestas({"k","p"})
print(grafo.getArestas())