import pygame 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_SIZE = 50
PLAYER_COLOR = (0, 0, 255)
PLAYER_SPEED = 5
GRAVITY = 1 
JUMP_STRENGTH = -20

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(PLAYER_COLOR)

        self.rect = self.image.get_rect()

        self.rect.x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
        self.rect.y = SCREEN_HEIGHT - PLAYER_SIZE - 50

        self.change_x = 0 # Velocidade horizontal
        self.change_y = 0 # Velocidade vertical (para pulo e gravidade)
        self.on_ground = True # Indica se o jogador está no chão
        self.lives = 3 # Vidas do jogador

    def update(self):
        """Método chamado a cada frame para atualizar a posição do jogador."""
        
        # --- 1. Movimento Lateral ---
        self.rect.x += self.change_x
        
        # Manter o jogador dentro dos limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            
        # --- 2. Gravidade e Pulo ---
        # Aplica a gravidade se o jogador não estiver no chão
        if not self.on_ground:
            self.change_y += GRAVITY
            
        self.rect.y += self.change_y
        
        # Verifica se o jogador atingiu o "chão" (o terreno plano)
        # O "chão" está em SCREEN_HEIGHT - 50
        ground_level = SCREEN_HEIGHT - 50 - PLAYER_SIZE
        
        if self.rect.y >= ground_level:
            self.rect.y = ground_level
            self.change_y = 0
            self.on_ground = True

    def jump(self):
        """Inicia o pulo do jogador."""
        if self.on_ground:
            self.change_y = JUMP_STRENGTH
            self.on_ground = False

    def move_left(self):
        """Define a velocidade para mover para a esquerda."""
        self.change_x = -PLAYER_SPEED

    def move_right(self):
        """Define a velocidade para mover para a direita."""
        self.change_x = PLAYER_SPEED

    def stop_move(self):
        """Para o movimento lateral."""
        self.change_x = 0

