import pygame
import sys
from player import Player

# --- Configurações Globais ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CAPTION = "Caçador de Estrelas"

# --- Cores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0) # Cor para o terreno

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

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # --- Loop Principal do Jogo ---
    while running:
        # 1. Processamento de Eventos (Input do Usuário)
        # Adicionar lógica de input do jogador aqui (teclas pressionadas)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.move_right()
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    player.jump()

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                    player.stop_move
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > 0:
                    player.stop_move()
                    

        # 2. Atualização do Jogo (Lógica)
        # Atualizar posição do jogador, estrelas, rochas, pontuação, etc.

        all_sprites.update()

        
        # 3. Desenho (Renderização)
        screen.fill(BLACK) # Preenche a tela com preto
        
         # Desenha o terreno plano (uma linha verde)
         # O "chão" está 50 pixels acima da borda inferior
        ground_y = SCREEN_HEIGHT - 50
        pygame.draw.line(screen, GREEN, (0, ground_y), (SCREEN_WIDTH, ground_y), 5)

        # Desenha todos os sprites (incluindo o jogador)
        all_sprites.draw(screen)

        # Atualiza a tela para mostrar o que foi desenhado
        pygame.display.flip()
        
        # Limita o FPS
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
