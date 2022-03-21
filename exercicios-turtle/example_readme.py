"""
extraído de https://pythonguides.com/python-turtle-art/
"""
from turtle import *
import turtle
ws = turtle.Screen()
ws.bgcolor("black")
sk = turtle.Turtle()
sk.color("cyan")

def squarefunc(size):
	for i in range(4):
		sk.fd(size)
		sk.left(90)
		size = size + 6

squarefunc(7)
squarefunc(27)
squarefunc(47)
squarefunc(67)
squarefunc(87)
squarefunc(107)
squarefunc(127)
squarefunc(147)
