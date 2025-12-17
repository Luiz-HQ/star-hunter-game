import pygame
import sys

# --- Configurações Globais ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CAPTION = "Caçador de Estrelas"

# --- Cores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

def main():
    """Função principal do jogo."""
    pygame.init()
    
    # Configuração da tela
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    
    # Relógio para controlar o FPS
    clock = pygame.time.Clock()
    
    # Variável de controle do loop principal
    running = True
    
    # --- Loop Principal do Jogo ---
    while running:
        # 1. Processamento de Eventos (Input do Usuário)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Adicionar lógica de input do jogador aqui (teclas pressionadas)
            
        # 2. Atualização do Jogo (Lógica)
        # Atualizar posição do jogador, estrelas, rochas, pontuação, etc.
        
        # 3. Desenho (Renderização)
        screen.fill(BLACK) # Preenche a tela com preto
        
        # Desenhar todos os elementos do jogo aqui (jogador, estrelas, rochas)
        
        # Atualiza a tela para mostrar o que foi desenhado
        pygame.display.flip()
        
        # Limita o FPS
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
