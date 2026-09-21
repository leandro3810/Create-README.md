"""
Python Lord - jogo arcade com Turtle
Autor: Leandro
"""

import math
import random
import turtle

LARGURA_TELA = 900
ALTURA_TELA = 650
LIMITE_X = LARGURA_TELA // 2 - 30
LIMITE_Y = ALTURA_TELA // 2 - 30
VELOCIDADE_JOGADOR = 6
DISTANCIA_COLETA = 22
DISTANCIA_COLISAO = 24


class PythonLordGame:
    """Jogo arcade simples com coleta, sobrevivência e progressão automática."""

    def __init__(self):
        self.tela = turtle.Screen()
        self.tela.title("Python Lord - Desafio Cósmico")
        self.tela.bgcolor("#08111f")
        self.tela.setup(width=LARGURA_TELA, height=ALTURA_TELA)
        self.tela.tracer(0)

        self.score = 0
        self.level = 1
        self.lives = 3
        self.running = True
        self.keys = {"Left": False, "Right": False, "Up": False, "Down": False}
        self.collectibles = []
        self.enemies = []
        self.frames = 0
        self.spawn_enemy_every = 50
        self.spawn_collectible_every = 80
        self.max_collectibles = 3

        self.player = turtle.Turtle()
        self.player.shape("triangle")
        self.player.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.player.color("#66fcf1")
        self.player.penup()
        self.player.setheading(90)

        self.hud = turtle.Turtle()
        self.hud.hideturtle()
        self.hud.color("white")
        self.hud.penup()

        self.message = turtle.Turtle()
        self.message.hideturtle()
        self.message.color("#f8f8f2")
        self.message.penup()

        self.bind_controls()
        self.reset_game()
        self.loop()
        self.tela.mainloop()

    def bind_controls(self):
        """Configura os controles do jogador."""
        self.tela.listen()
        for key in ("Left", "a", "A"):
            self.tela.onkeypress(lambda k="Left": self.set_key(k, True), key)
            self.tela.onkeyrelease(lambda k="Left": self.set_key(k, False), key)
        for key in ("Right", "d", "D"):
            self.tela.onkeypress(lambda k="Right": self.set_key(k, True), key)
            self.tela.onkeyrelease(lambda k="Right": self.set_key(k, False), key)
        for key in ("Up", "w", "W"):
            self.tela.onkeypress(lambda k="Up": self.set_key(k, True), key)
            self.tela.onkeyrelease(lambda k="Up": self.set_key(k, False), key)
        for key in ("Down", "s", "S"):
            self.tela.onkeypress(lambda k="Down": self.set_key(k, True), key)
            self.tela.onkeyrelease(lambda k="Down": self.set_key(k, False), key)

        self.tela.onkey(self.restart, "r")
        self.tela.onkey(self.restart, "R")

    def set_key(self, key, value):
        self.keys[key] = value

    def reset_game(self):
        """Reinicia o estado principal do jogo."""
        self.score = 0
        self.level = 1
        self.lives = 3
        self.running = True
        self.keys = {"Left": False, "Right": False, "Up": False, "Down": False}
        self.frames = 0
        self.spawn_enemy_every = 50
        self.spawn_collectible_every = 80
        self.max_collectibles = 3

        self.clear_entities()
        self.player.goto(0, -220)
        self.player.showturtle()
        self.message.clear()
        self.spawn_collectible()
        self.spawn_collectible()
        self.spawn_enemy()
        self.update_hud()

    def restart(self):
        """Permite reiniciar a partida a qualquer momento."""
        self.reset_game()

    def clear_entities(self):
        """Remove todos os itens e inimigos da tela."""
        for entity in self.collectibles + self.enemies:
            entity.hideturtle()
        self.collectibles.clear()
        self.enemies.clear()

    def create_entity(self, shape, color, x, y):
        entity = turtle.Turtle()
        entity.shape(shape)
        entity.color(color)
        entity.penup()
        entity.goto(x, y)
        return entity

    def spawn_collectible(self):
        """Cria uma energia para coleta automática na arena."""
        if len(self.collectibles) >= self.max_collectibles:
            return

        item = self.create_entity(
            "circle",
            random.choice(["#ffe66d", "#ff9f1c", "#7bed9f", "#70a1ff"]),
            random.randint(-LIMITE_X + 20, LIMITE_X - 20),
            random.randint(-40, LIMITE_Y - 20),
        )
        item.dx = random.choice([-1, 1]) * random.uniform(0.8, 2.0)
        item.dy = random.choice([-1, 1]) * random.uniform(0.8, 2.0)
        self.collectibles.append(item)

    def spawn_enemy(self):
        """Cria um inimigo com movimentação automática."""
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            x, y = random.randint(-LIMITE_X, LIMITE_X), LIMITE_Y
        elif side == "bottom":
            x, y = random.randint(-LIMITE_X, LIMITE_X), -LIMITE_Y
        elif side == "left":
            x, y = -LIMITE_X, random.randint(-LIMITE_Y, LIMITE_Y)
        else:
            x, y = LIMITE_X, random.randint(-LIMITE_Y, LIMITE_Y)

        enemy = self.create_entity("square", "#ff4757", x, y)
        enemy.shapesize(stretch_wid=1.1, stretch_len=1.1)

        angle = self.angle_to_player(x, y)
        base_speed = min(2.4 + self.level * 0.35, 6.5)
        enemy.dx = math.cos(angle) * base_speed
        enemy.dy = math.sin(angle) * base_speed
        self.enemies.append(enemy)

    def angle_to_player(self, x, y):
        """Calcula a direção do inimigo para o jogador."""
        return math.atan2(self.player.ycor() - y, self.player.xcor() - x)

    def update_player(self):
        """Move o jogador respeitando os limites da tela."""
        x = self.player.xcor()
        y = self.player.ycor()

        if self.keys["Left"]:
            x -= VELOCIDADE_JOGADOR
            self.player.setheading(180)
        if self.keys["Right"]:
            x += VELOCIDADE_JOGADOR
            self.player.setheading(0)
        if self.keys["Up"]:
            y += VELOCIDADE_JOGADOR
            self.player.setheading(90)
        if self.keys["Down"]:
            y -= VELOCIDADE_JOGADOR
            self.player.setheading(270)

        x = max(-LIMITE_X, min(LIMITE_X, x))
        y = max(-LIMITE_Y, min(LIMITE_Y, y))
        self.player.goto(x, y)

    def update_collectibles(self):
        """Move e recicla itens coletáveis."""
        for item in self.collectibles:
            item.goto(item.xcor() + item.dx, item.ycor() + item.dy)
            if item.xcor() <= -LIMITE_X or item.xcor() >= LIMITE_X:
                item.dx *= -1
            if item.ycor() <= -LIMITE_Y or item.ycor() >= LIMITE_Y:
                item.dy *= -1

    def update_enemies(self):
        """Move inimigos e mantém todos dentro da arena."""
        for enemy in self.enemies:
            enemy.goto(enemy.xcor() + enemy.dx, enemy.ycor() + enemy.dy)
            if enemy.xcor() <= -LIMITE_X or enemy.xcor() >= LIMITE_X:
                enemy.dx *= -1
            if enemy.ycor() <= -LIMITE_Y or enemy.ycor() >= LIMITE_Y:
                enemy.dy *= -1

    def check_collectibles(self):
        """Atualiza a pontuação ao coletar energia."""
        for item in self.collectibles[:]:
            if self.player.distance(item) < DISTANCIA_COLETA:
                item.hideturtle()
                self.collectibles.remove(item)
                self.score += 10
                self.apply_progression()
                self.spawn_collectible()

    def check_enemy_collisions(self):
        """Remove vidas ao tocar em inimigos."""
        for enemy in self.enemies[:]:
            if self.player.distance(enemy) < DISTANCIA_COLISAO:
                self.lives -= 1
                enemy.hideturtle()
                self.enemies.remove(enemy)
                self.player.goto(0, -220)
                self.keys = {key: False for key in self.keys}
                self.show_temporary_message("Você foi atingido!")
                if self.lives <= 0:
                    self.game_over()
                elif not self.enemies:
                    self.spawn_enemy()
                return

    def apply_progression(self):
        """Aumenta a dificuldade de forma automática."""
        new_level = self.score // 40 + 1
        if new_level > self.level:
            self.level = new_level
            self.spawn_enemy_every = max(20, self.spawn_enemy_every - 4)
            self.spawn_collectible_every = max(35, self.spawn_collectible_every - 2)
            self.max_collectibles = min(5, self.max_collectibles + 1)
            self.show_temporary_message(f"Nível {self.level} desbloqueado!")
            self.spawn_enemy()
            if len(self.collectibles) < self.max_collectibles:
                self.spawn_collectible()

    def show_temporary_message(self, text):
        """Exibe uma mensagem curta no centro da tela."""
        self.message.clear()
        self.message.goto(0, 0)
        self.message.write(text, align="center", font=("Arial", 18, "bold"))
        self.tela.ontimer(self.message.clear, 1200)

    def game_over(self):
        """Finaliza a partida."""
        self.running = False
        self.player.hideturtle()
        self.message.clear()
        self.message.goto(0, -10)
        self.message.write(
            f"Game Over\nPontuação final: {self.score}\nPressione R para reiniciar",
            align="center",
            font=("Arial", 20, "bold"),
        )

    def update_hud(self):
        """Atualiza o painel superior."""
        self.hud.clear()
        self.hud.goto(0, ALTURA_TELA // 2 - 45)
        self.hud.write(
            f"Pontuação: {self.score}   Vidas: {self.lives}   Nível: {self.level}",
            align="center",
            font=("Arial", 16, "bold"),
        )

    def loop(self):
        """Loop principal do jogo."""
        if self.running:
            self.frames += 1
            self.update_player()
            self.update_collectibles()
            self.update_enemies()
            self.check_collectibles()
            self.check_enemy_collisions()

            if self.frames % self.spawn_enemy_every == 0:
                self.spawn_enemy()
            if self.frames % self.spawn_collectible_every == 0:
                self.spawn_collectible()

            self.update_hud()

        self.tela.update()
        self.tela.ontimer(self.loop, 30)


def main():
    PythonLordGame()


if __name__ == "__main__":
    main()
