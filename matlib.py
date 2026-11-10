import pygame
import pgzrun
import random
WIDTH = 800
HEIGHT = 600
TITLE = "Jogo da aura tung sahur god"

inimigo = Actor ("von")
inimigo.x = 300
inimigo.y = 200
sahur = Actor("sahur")
sahur.x = 300
sahur.y = 200
robux = Actor("robux")
robux.x = 400
robux.y = 300
moedas = []
vel_inimigo = 1

def redimencionar (ator, altura):
    escala = altura / ator.height
    novo = pygame.transform.smoothscale(
        ator._orig_surf, (int(ator.width * escala), altura)
    )
    ator._orig_surf = ator._surf = novo
    ator._update_pos()

redimencionar(sahur, 100)
redimencionar(robux, 50)
redimencionar(inimigo, 100)

# --- Configuracões e Variáveis de Estado ---
PONTOS_VITORIA = 100
VIDAS_INICIAIS = 3
VELOCIDADE_HEROI = 2
VELOCIDADE_BASE_INIMIGO = 0.8

pontos = 0 
vidas = VIDAS_INICIAIS
estado_jogo = "JOGANDO"
moedas = []

def reiniciar_jogo():
    global pontos, vidas, estado_jogo
    pontos = 0
    vidas = VIDAS_INICIAIS
    sahur.pos = (100, 100)
    robux.pos = (650, 450)
    estado_jogo = "JOGANDO"

def mover_inimigo():
    # A Velocidade aumenta conforma os pontos sobem
    vel_inimigo = VELOCIDADE_BASE_INIMIGO + (pontos // 20) * 0.4

    if inimigo.x < sahur.x:
        inimigo.x += vel_inimigo
    elif inimigo.x > sahur.x:
        inimigo.x -= vel_inimigo

    if inimigo.y < sahur.y:
        inimigo.y += vel_inimigo
    elif inimigo.y > sahur.y:
        inimigo.y -= vel_inimigo

def draw():
    global pontos, estado_jogo
    screen.fill((0, 5, 255))

    if estado_jogo == "JOGANDO":
        robux.draw()
        sahur.draw()
        inimigo.draw()
        # HUB Superior: Pontos e Vidas
        screen.draw.text(f"Pontos: {pontos}/{PONTOS_VITORIA}", topleft=(20,20), fontsize=32, color= "gold", shadow=(1, 1), scolor="black")

        # Exebição de Vidas em formato visual
        cor_vida = "lime" if vidas > 1 else "red"
        screen.draw.text(f"vidas: {vidas}", topright=(WIDTH - 20, 20), fontsize=28, color=cor_vida, shadow=(1, 1), scolor="black")

        # Nível de perigo/velocidade
        nivel = (pontos // 20) + 1
        screen.draw.text(f"Nível de Ameaça: {nivel}", midbottom=(WIDTH // 2, HEIGHT - 15), fontsize=22, color="lightgray")

        for m in moedas:
            m.draw()
    if estado_jogo == "GAMEOVER":
        screen.draw.text(f"Você Perdeu", center=(20,20), fontsize=32, color= "gold", shadow=(1, 1), scolor="black")

    
    
def update():
    global pontos
    global vidas
    if keyboard.a:
        sahur.x -= 5

    if keyboard.d:
        sahur.x += 5

    if keyboard.w:
        sahur.y -= 5

    if keyboard.s:
        sahur.y += 5

    if sahur.colliderect(robux):
        robux.x = random.randint(50, WIDTH -50)
        robux.y = random.randint(50, HEIGHT -50)
        pontos = pontos + 1
        sounds.coletar.play()

    if inimigo.colliderect(sahur):
        sahur.x = random.randint(50, WIDTH - 50)
        sahur.y = random.randint(50, HEIGHT -50)
        pontos = pontos - 1
        vidas = vidas - 1
    mover_inimigo()

    if vidas <= 0:
        estado_jogo = "GAMEOVER"
        


def mover_inimigo():
    if inimigo.x < sahur.x:
        inimigo.x += vel_inimigo
    elif inimigo.x > sahur.x:
        inimigo.x -= vel_inimigo

    if inimigo.y < sahur.y:
         inimigo.y += vel_inimigo
    elif inimigo.y > sahur.y:
        inimigo.y -= vel_inimigo 

def spawn_robux():
    global moedas
    if estado_jogo != "JOGANDO" or len(robux) >= 5:
        return
    m = Actor("robux", (random.randint(60, WIDHT - 60), random.randint(60, HEIGHT - 200)))
    redimensionar(m, 40)
    robux.append(m)

clock.schedule_interval(spawn_robux, 3)


pgzrun.go()
