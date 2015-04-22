# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:03:11 2015

@author: Raphael
"""

import turtle

#Boneco da forca
   
   #Base
   
def base():
    base  = turtle.Turtle()  
    base.pensize(8)
    base.speed(100)  
    base.penup()     
    base.setpos(-660,0)
    base.pendown()
    base.fd(100)
    base.color("black")
    base.hideturtle()
   
   
   #poste
def poste():
    poste  = turtle.Turtle()  
    poste.pensize(8)
    poste.speed(100)  
    poste.penup()    
    poste.setpos(-610,0)
    poste.pendown()
    poste.lt(90)
    poste.fd(235)
    poste.color("black")
    poste.hideturtle()


    #haste de cima da forca
def prendedor():
    prendedor  = turtle.Turtle()  
    prendedor.pensize(8)
    prendedor.speed(100)  
    prendedor.penup()     
    prendedor.setpos(-610,235)
    prendedor.pendown()
    prendedor.fd(130)
    prendedor.color("black")
    prendedor.hideturtle()

   #o que prende a cabeça do boneco

def corda():
    corda  = turtle.Turtle() 
    corda.pensize(8)
    corda.speed(100)  
    corda.penup()     
    corda.setpos(-480,235)
    corda.pendown()
    corda.rt(90)
    corda.fd(5)
    corda.color("black")
    corda.hideturtle()





#Corpo
    #cabeca

def cabeca():
    cabeca  = turtle.Turtle()  
    cabeca.pensize(8)
    cabeca.speed(100)  
    cabeca.penup()     
    cabeca.setpos(-480,180)
    cabeca.pendown()
    cabeca.circle(20)
    cabeca.color("black")
    cabeca.hideturtle()




    #tronco

def tronco():
    tronco  = turtle.Turtle()  
    tronco.pensize(8)
    tronco.speed(100)  
    tronco.penup()     
    tronco.setpos(-480,175)
    tronco.pendown()
    tronco.rt(90)
    tronco.fd(80)
    tronco.color("black")
    tronco.hideturtle()


    #braço direito
def bracod():
    bracod  = turtle.Turtle()  
    bracod.pensize(8)
    bracod.speed(100)  
    bracod.penup()    
    bracod.setpos(-480,167)
    bracod.pendown()
    bracod.rt(120)
    bracod.fd(55)
    bracod.color("black")
    bracod.hideturtle()



def bracoe():
    bracoe  = turtle.Turtle()  # Cria um objeto "desenhador"
    bracoe.pensize(8)
    bracoe.speed(100)  # define a velocidade
    bracoe.penup()     # Remova e veja o que acontece
    bracoe.setpos(-480,167)
    bracoe.pendown()
    bracoe.rt(60)
    bracoe.fd(55)
    bracoe.color("black")
    bracoe.hideturtle()


def pernad():
    pernad  = turtle.Turtle()  # Cria um objeto "desenhador"
    pernad.pensize(8)
    pernad.speed(100)  # define a velocidade
    pernad.penup()     # Remova e veja o que acontece
    pernad.setpos(-480,95)
    pernad.pendown()
    pernad.rt(120)
    pernad.fd(70)
    pernad.color("black")
    pernad.hideturtle()


def pernae():
    pernae  = turtle.Turtle()  # Cria um objeto "desenhador"
    pernae.pensize(8)
    pernae.speed(100)  # define a velocidade
    pernae.penup()     # Remova e veja o que acontece
    pernae.setpos(-480,95)
    pernae.pendown()
    pernae.rt(60)
    pernae.fd(70)
    pernae.color("black")
    pernae.hideturtle()



def espaco(a):    
    for e in range(a):    
        espaco  = turtle.Turtle()  # Cria um objeto "desenhador"
        espaco.pensize(5)
        espaco.speed(100)  # define a velocidade
        espaco.penup()     # Remova e veja o que acontece
        espaco.setpos(-430+e*50,-140)
        espaco.pendown()
        espaco.fd(30)
        espaco.color("black")
        espaco.hideturtle()
espaco(5)


def escrever(letra,e):
        escrever=turtle.Turtle()
        escrever.setpos(-445+e*50,-140)
        escrever.write(letra, font=('Arial', 12, 'normal'))
        escrever.color("black")
       

def MontarCorpo(m):
    if m==0:
        cabeca()
    if m==1:
        tronco()
    if m==2:
        bracoe()
    if m==3:
        bracod()
    if m==4:
        pernae()
    if m==5:
        pernad()




