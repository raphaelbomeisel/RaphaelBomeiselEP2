# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:30:47 2015

@author: Raphael
"""
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightgreen")
window.title("Forca!")
window.setup( width = 1400, height = 640, startx = None, starty = None)

#import tkinter

import ForcaGraficos

ForcaGraficos.base()
ForcaGraficos.poste()
ForcaGraficos.prendedor()
ForcaGraficos.corda()


import random
ArquivoPalavras=open("PalavrasForca.txt",'r',encoding="UTF-8")

ler=ArquivoPalavras.readlines()

linha=ler[0]  #é uma string

valores=linha.split(",")


escolhida=ler[random.randint(0,10)]

a=len(escolhida)-2
print(escolhida)
print(a)
print(escolhida[0])


ForcaGraficos.espaco(a)
        
    
tentativas=0
contador=0

while tentativas<6:
    letra=window.textinput("Forca!","Digite a letra de seu chute: ")   

    for e in range(a):
        if letra==escolhida[e]:
            ForcaGraficos.escrever(letra,e)
            contador+=contador
            if contador==a:
                ("Parabéns! Você ganhou!")
   
    else:
        ForcaGraficos.MontarCorpo(tentativas);
        tentativas+=tentativas
        if tentativas==6:
            window.textinput("Você foi enforcado!")
            turtle.done()
    



window.exitonclick()
turtle.done()


    
    