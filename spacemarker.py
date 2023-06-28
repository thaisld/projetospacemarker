import pygame
import tkinter as tk
from tkinter import simpledialog
import json
pygame.init()

tamanho = (900, 600)
preto = (0, 0, 0)
fundo = pygame.image.load("galaxia.png")
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
        marcacoes_estrelas.append((nome, pos))
        print(f"Nome da estrela: {nome}")
        print(f"Posição do clique: {pos}")
    else:
        nome = f"desconhecido {pos}"
        marcacoes_estrelas.append((f"{nome}", pos))
        print(f"desconhecido: {pos}")

def salvarMarcacoes():
    with open("marcacoes.json", "w") as arquivo:
         json.dump(marcacoes_estrelas, arquivo)
         print("As marcações foram salvas com sucesso!")

def carregarMarcacoes_salvas():
    try:
        with open("marcacoes.json", "r") as arquivo:
            marcacoes_estrelas.clear()
            marcacoes_estrelas.extend(json.load(arquivo))
        print("As marcações foram carregadas com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de marcações encontrado.")

def excluirMarcacoes():
    marcacoes_estrelas.clear()
    print("As marcações foram excluídas.")
         
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
            elif event.key == pygame.K_F10:  # Tecla F10 para salvar
                salvarMarcacoes()
            elif event.key == pygame.K_F11:  # Tecla F11 para carregar
                carregarMarcacoes_salvas()
            elif event.key == pygame.K_F12:  # Tecla F12 para excluir
                excluirMarcacoes()
        
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
