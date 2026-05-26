"""
Python Lord - Desenho de formas geométricas com Turtle
Autor: Leandro
"""

import random
import turtle

CORES_DISPONIVEIS = ["blue", "red", "green", "yellow", "purple", "orange", "cyan", "magenta"]


def desenhar_quadrado(t, x, y, tamanho, cor):
    """Desenha um quadrado na posição (x, y) com o tamanho e cor especificados."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(4):
        t.forward(tamanho)
        t.right(90)
    t.end_fill()


def desenhar_retangulo(t, x, y, largura, altura, cor):
    """Desenha um retângulo na posição (x, y) com largura, altura e cor especificados."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for comprimento in [largura, altura, largura, altura]:
        t.forward(comprimento)
        t.right(90)
    t.end_fill()


def desenhar_triangulo(t, x, y, tamanho, cor):
    """Desenha um triângulo equilátero na posição (x, y)."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(3):
        t.forward(tamanho)
        t.left(120)
    t.end_fill()


def desenhar_circulo(t, x, y, raio, cor):
    """Desenha um círculo preenchido na posição (x, y)."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()


def desenhar_estrela(t, x, y, tamanho, cor):
    """Desenha uma estrela de 5 pontas na posição (x, y)."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
    t.end_fill()


def desenhar_cena_padrao(t):
    """Desenha a composição padrão de formas geométricas."""
    desenhar_quadrado(t, -320, 150, tamanho=110, cor="blue")
    desenhar_quadrado(t, -170, 150, tamanho=110, cor="red")
    desenhar_retangulo(t, 10, 150, largura=220, altura=110, cor="green")
    desenhar_triangulo(t, -60, -20, tamanho=160, cor="yellow")
    desenhar_quadrado(t, 170, -130, tamanho=90, cor="purple")
    desenhar_circulo(t, -260, -150, raio=45, cor="orange")
    desenhar_estrela(t, 40, -130, tamanho=110, cor="cyan")


def desenhar_cena_aleatoria(t):
    """Desenha uma cena com cores aleatórias."""
    cores = random.sample(CORES_DISPONIVEIS, k=len(CORES_DISPONIVEIS))
    desenhar_quadrado(t, -320, 150, tamanho=110, cor=cores[0])
    desenhar_quadrado(t, -170, 150, tamanho=110, cor=cores[1])
    desenhar_retangulo(t, 10, 150, largura=220, altura=110, cor=cores[2])
    desenhar_triangulo(t, -60, -20, tamanho=160, cor=cores[3])
    desenhar_quadrado(t, 170, -130, tamanho=90, cor=cores[4])
    desenhar_circulo(t, -260, -150, raio=45, cor=cores[5])
    desenhar_estrela(t, 40, -130, tamanho=110, cor=cores[6])


def main():
    # Configuração da janela
    tela = turtle.Screen()
    tela.title("Python Lord - Formas Geométricas")
    tela.bgcolor("black")
    tela.setup(width=900, height=650)

    # Configuração do pincel
    t = turtle.Turtle()
    t.speed(6)
    t.pencolor("white")
    t.pensize(2)

    def limpar():
        t.clear()

    def redesenhar_padrao():
        limpar()
        desenhar_cena_padrao(t)

    def redesenhar_aleatorio():
        limpar()
        desenhar_cena_aleatoria(t)

    # Desenho inicial
    redesenhar_padrao()
    t.hideturtle()

    # Novas funcionalidades de interação
    tela.listen()
    tela.onkey(redesenhar_padrao, "p")
    tela.onkey(redesenhar_padrao, "P")
    tela.onkey(redesenhar_aleatorio, "r")
    tela.onkey(redesenhar_aleatorio, "R")
    tela.onkey(limpar, "c")
    tela.onkey(limpar, "C")

    tela.mainloop()


if __name__ == "__main__":
    main()
