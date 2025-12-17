# Caçador de Estrelas: Guia de Desenvolvimento de Jogo 2D em Python

Este documento serve como um guia inicial e estrutura base para o desenvolvimento de um jogo 2D simples em Python, onde o jogador deve coletar estrelas que caem e desviar de rochas.

## 1. Bibliotecas Recomendadas

Para o desenvolvimento de jogos 2D em Python, a biblioteca **Pygame** é a mais recomendada, especialmente para iniciantes, devido à sua vasta documentação, comunidade ativa e simplicidade para lidar com gráficos, sons e entrada de usuário.

| Biblioteca | Vantagens | Desvantagens | Uso Recomendado |
| :--- | :--- | :--- | :--- |
| **Pygame** | Simples, excelente para 2D, grande comunidade, fácil de começar. | Baseada em CPU (raster graphics), pode ser mais lenta para jogos muito complexos. | Jogos 2D simples, prototipagem, aprendizado. |
| **Arcade** | Mais moderna, baseada em OpenGL (aceleração por GPU), possui funções de física e sprites integradas. | Curva de aprendizado um pouco maior que Pygame, comunidade menor. | Jogos 2D que exigem melhor performance gráfica e física. |

**Recomendação para este projeto:** Utilizaremos o **Pygame** por ser a opção mais direta e com melhor suporte para a estrutura de jogo proposta.

## 2. Estrutura do Projeto

A estrutura de diretórios e arquivos foi organizada para manter o código limpo e modular, seguindo as boas práticas de desenvolvimento de jogos.

```
jogo_estrelas/
├── assets/
│   ├── images/     # Para imagens do jogador, estrelas, rochas, fundo, etc.
│   └── sounds/     # Para efeitos sonoros e música de fundo.
├── src/
│   ├── __init__.py
│   ├── main.py         # O loop principal do jogo e inicialização.
│   ├── player.py       # Classe para o personagem do jogador.
│   ├── star.py         # Classe para as estrelas (coletáveis).
│   ├── rock.py         # Classe para as rochas (obstáculos).
│   └── game_manager.py # Classe para gerenciar a pontuação, vidas e estados do jogo.
├── README.md           # Este guia de desenvolvimento.
└── requirements.txt    # Lista de dependências (Pygame).
```

## 3. Guia Passo a Passo para o Desenvolvimento

Siga estes passos para construir o jogo:

### Passo 1: Configuração do Ambiente

1.  **Instalar Pygame:**
    ```bash
    pip install -r requirements.txt
    ```

### Passo 2: Inicialização e Loop Principal (`src/main.py`)

O arquivo `main.py` já contém a estrutura básica do Pygame: inicialização, criação da tela, o *game loop* (laço principal) e o controle de FPS.

### Passo 3: Criação do Terreno (Plataforma)

O terreno plano será a base onde o jogador se move. Em um jogo 2D simples como este, o terreno pode ser representado por:

1.  **Desenho Simples:** Uma linha ou um retângulo na parte inferior da tela, desenhado diretamente no `main.py`.
2.  **Colisão:** Definir uma coordenada Y (por exemplo, `SCREEN_HEIGHT - 50`) que será o "chão" para o jogador.

### Passo 4: Implementação do Jogador (`src/player.py`)

Crie uma classe `Player` que herde de `pygame.sprite.Sprite`.

1.  **Movimento Lateral:** Implementar a lógica para mover o sprite do jogador para a esquerda e direita em resposta às teclas (ex: `pygame.K_LEFT`, `pygame.K_RIGHT`).
2.  **Pulo:** Implementar a lógica de pulo, que envolve aumentar a velocidade vertical (`vy`) e aplicar a gravidade para trazê-lo de volta ao chão.
3.  **Vidas:** Adicionar um atributo para rastrear as 3 vidas.

### Passo 5: Implementação dos Itens (`src/star.py` e `src/rock.py`)

Crie classes `Star` e `Rock`, ambas também herdando de `pygame.sprite.Sprite`.

1.  **Queda:** Ambas as classes devem ter uma lógica de movimento vertical (queda) e serem geradas em posições X aleatórias no topo da tela.
2.  **Remoção:** Implementar a lógica para remover o objeto quando ele sair da parte inferior da tela.

### Passo 6: Gerenciamento do Jogo (`src/game_manager.py`)

Crie uma classe `GameManager` para centralizar a lógica do jogo.

1.  **Pontuação:** Gerenciar a pontuação total.
2.  **Geração de Itens:** Implementar um sistema para gerar estrelas e rochas em intervalos de tempo aleatórios.
3.  **Colisões:**
    *   **Jogador vs. Estrela:** Se colidir, aumentar a pontuação e remover a estrela.
    *   **Jogador vs. Rocha:** Se colidir, diminuir uma vida, aplicar um breve período de invulnerabilidade (para evitar dano múltiplo instantâneo) e remover a rocha.
4.  **Fim de Jogo:** Verificar se as vidas do jogador chegaram a zero.

### Passo 7: Refinamento e Assets

1.  **Gráficos:** Substituir os retângulos coloridos (placeholders) por imagens reais (`assets/images/`).
2.  **Interface:** Desenhar a pontuação e o número de vidas na tela.
3.  **Sons:** Adicionar efeitos sonoros para coleta de estrela, dano e pulo (`assets/sounds/`).

Este guia fornece a estrutura e o caminho para começar. O próximo passo é focar na implementação das classes e na integração com o loop principal.
