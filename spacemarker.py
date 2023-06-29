import pygame
import tkinter as tk
from tkinter import simpledialog
import json
import math
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

estrelas_marcadas = []

def nomes_estrelas(pos):
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    if nome:
        estrelas_marcadas.append((nome, pos))
        print(f"Nome da estrela:{nome}")
        print(f"Posição do clique:{pos}")
    else:
        nome = f"desconhecido {pos}"
        estrelas_marcadas.append((f"{nome}", pos))
        print(f"desconhecido: {pos}")
def exibir_opcoes():
    fonte = pygame.font.Font(None, 22)  # Escolha a fonte e o tamanho desejado
    cor = (255, 255, 255)  # Escolha a cor do texto (branco neste exemplo)
    texto1 = fonte.render("Pressione ESC para sair", True, cor)
    texto2 = fonte.render("Pressione F10 para salvar os pontos", True, cor)
    texto3 = fonte.render("Pressione F11 para carregar seus pontos", True, cor)
    texto4 = fonte.render("Pressione F12 para excluir os pontos", True, cor)
    
    # Defina as posições dos textos na tela
    posicao1 = (10, 10)
    posicao2 = (10, 25)
    posicao3 = (10, 40)
    posicao4 = (10, 55)
    
    # Desenhe os textos na tela
    display.blit(texto1, posicao1)
    display.blit(texto2, posicao2)
    display.blit(texto3, posicao3)
    display.blit(texto4, posicao4)

def salvarMarcacoes():
    with open("marcacoes.json", "w") as arquivo:
         json.dump(estrelas_marcadas, arquivo)
         print("As marcações foram salvas com sucesso!")

def carregarMarcacoes_salvas():
    try:
        with open("marcacoes.json", "r") as arquivo:
            estrelas_marcadas.clear()
            estrelas_marcadas.extend(json.load(arquivo))
        print("As marcações foram carregadas com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de marcações encontrado.")
def excluirMarcacoes():
    estrelas_marcadas.clear()
    print("As marcações foram excluídas.")

def calcularDistancia(pos1, pos2):
    x1, y1 = pos2
    x2, y2 = pos1
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
opcoes_posClique = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvarMarcacoes()
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Botão esquerdo do mouse
                mouse_pos = pygame.mouse.get_pos()
                nomes_estrelas(mouse_pos)
                opcoes_posClique = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Tecla ESC para sair
                salvarMarcacoes()
                running = False
            elif event.key == pygame.K_F10:  # Tecla F10 para salvar
                salvarMarcacoes()
            elif event.key == pygame.K_F11:  # Tecla F11 para carregar
                carregarMarcacoes_salvas()
            elif event.key == pygame.K_F12:  # Tecla F12 para excluir
                excluirMarcacoes()
    display.fill(preto)
    display.blit(fundo, (0, 0))

# Desenha as marcações na tela
    last_pos = None # Armazenar a posição da última marcação feita
    for nome, pos in estrelas_marcadas:
        pygame.draw.circle(display, (255, 255, 255), pos, 5)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(nome, True, (255, 255, 255))
        display.blit(texto, (pos[0] + 10, pos[1] - 10))
        if last_pos is not None:
            pygame.draw.line(display, (255, 255, 255), last_pos, pos, 2) #Desenhar linha na tela 

            #Calcular e exibir a distância entre as marcações
            distancia = calcularDistancia(last_pos, pos)
            texto_distancia = fonte.render(f"Distância: {distancia:.2f}", True, (255, 255, 255))
            texto_distancia = pygame.transform.rotate(texto_distancia, 360)
            texto_rect = texto_distancia.get_rect(center=((last_pos[0] + pos[0]) // 2, (last_pos[1] + pos[1]) // 2))
            texto_rect.y -= texto_rect.height  # Mover o texto para cima
            display.blit(texto_distancia, texto_rect.topleft)

        last_pos = pos #Atualiza a última posição
    if opcoes_posClique:
        exibir_opcoes()
    pygame.display.update()

pygame.quit()