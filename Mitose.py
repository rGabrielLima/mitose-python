import pygame
import random

# Cores celulas iniciais
fundoTela = (255, 100, 105)
azul = (0, 0, 255)
azul1 = (0, 0, 255)

# Dimensão da tela
WIDTH = 1350
HEIGHT = 720

# Classe das celulas
class Cell:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.radius = 5

    def divide(self):
        # Criar duas novas células randomizando sua cor. Com o random a cor preta surge //nnão entendi o porque mas ficou melhor//
        cor1 = (random.randint(0, 255), random.randint(0, 0), random.randint(0, 0))
        cor2 = (random.randint(0, 255), random.randint(0, 0), random.randint(0, 0))
        cell1 = Cell(self.x, self.y, cor1)
        cell2 = Cell(self.x, self.y, cor2)
        return cell1, cell2

    def move(self):
        # essa função faz com que as células se movam aleatoriamente e define as velocidades para cada eixo (x, y)
        self.x += random.randint(-2, 2)
        self.y += random.randint(-2, 2)
        self.x = max(self.radius, min(self.x, WIDTH - self.radius))
        self.y = max(self.radius, min(self.y, HEIGHT - self.radius))

    def draw(self):
        pygame.draw.circle(screen, self.cor, (self.x, self.y), self.radius)

# Inicialização do Pygame
pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mrMitose")

# var que armazena as células
cells = []

# Criação de uma célula inicial
initial_cell = Cell(WIDTH // 2, HEIGHT // 2, azul1)
cells.append(initial_cell)

#criando um contador
font = pygame.font.Font(None, 30)  # Definindo o contador
total_cells = 1  # Contador das células iniciais
mother_cells = 1  # Contador ds células mães

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar a tela
    screen.fill(fundoTela)

    # Atualizar e desenhar as células
    for cell in cells[:]:
        cell.move()
        cell.draw()

        # Dividir células existentes
        if random.random() < 0.001:
            new_cells = cell.divide()
            cells.extend(new_cells)
            total_cells += 2  # Incrementa o contador de células totais
            mother_cells += 1  # Incrementa o contador de células mães

    # Exibir contador de células
    text = font.render(f"células mães: {mother_cells}  células existentes: {total_cells}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    text1 = font.render(" tu é única menininha", True, (0, 0, 0))
    screen.blit(text1, (1100, 650))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
