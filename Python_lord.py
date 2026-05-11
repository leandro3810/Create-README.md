"""
Python Lord - Desenho de formas geométricas com Turtle
Autor: Leandro
"""

import turtle


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


def main():
    # Configuração da janela
    tela = turtle.Screen()
    tela.title("Python Lord - Formas Geométricas")
    tela.bgcolor("black")
    tela.setup(width=800, height=600)

    # Configuração do pincel
    t = turtle.Turtle()
    t.speed(5)
    t.pencolor("white")
    t.pensize(2)

    # Desenha formas geométricas
    desenhar_quadrado(t, x=-300, y=100, tamanho=100, cor="blue")
    desenhar_quadrado(t, x=-150, y=100, tamanho=100, cor="red")
    desenhar_retangulo(t, x=50, y=100, largura=200, altura=100, cor="green")
    desenhar_triangulo(t, x=-50, y=-50, tamanho=150, cor="yellow")
    desenhar_quadrado(t, x=150, y=-100, tamanho=80, cor="purple")

    # Oculta o cursor e aguarda clique para fechar
    t.hideturtle()
    tela.mainloop()


if __name__ == "__main__":
    main()
