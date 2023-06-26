import pygame
import tkinter as tk
from tkinter import simpledialog
pygame.init()

tamanho = (900, 600)
preto = (0, 0, 0)
fundo = pygame.image.load("galaxia_.jpg")
display = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SPACE MARKER")
running = True

pygame.mixer.init()
musica_de_fundo = pygame.mixer.music.load('Space_Machine_Power.wav')
pygame.mixer.music.play(-1)

def nomeEstrela(pos):
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    print(nome)
    if nome:
        print(f"Nome da estrela: {nome}")
        print(f"Posição do clique: {pos}")
     else:
        nome = f"desconhecido {pos}"
        marcacoes_estrelas.append((f"{nome} {pos}", pos))
        print(f"Nome da estrela: {nome} {pos}")
         
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                mouse_pos = pygame.mouse.get_pos()
                nomeEstrela(mouse_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Tecla ESC para sair
                running = false
                
    display.fill(preto)
    display.blit(fundo, (0, 0))
    pygame.display.update()

    # Desenha as marcações na tela
    for nome, pos in marcacoes_estrelas:
        pygame.draw.circle(display, (255, 255, 255), pos, 5)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(nome, True, (255, 255, 255))
        display.blit(texto, (pos[0] + 10, pos[1] - 10))

    pygame.display.update()
    
pygame.quit()
