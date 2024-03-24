import pygame
from Velha import Velha
from Spritesheet import Spritesheet

class Game:
    # Pygame
    screen: pygame.Surface
    clock: pygame.time.Clock
    running: bool

    # Jogo da velha
    velha: Velha
    spritesheet: Spritesheet

    def __init__(self, titulo: str, width: int, height: int) -> None:
        pygame.init()
        pygame.display.set_caption(titulo)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.velha = Velha()
        self.velha.Inicio()


        self.spritesheet = Spritesheet("assets/velha_128.png")
        self.__Draw()
        return
    
    def Update(self):

        # Loop principal
        while self.running:
            mouse_b: bool = False
            # Capturar eventos de input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    mouse_b = pygame.mouse.get_pressed()[0]


            if(mouse_b):
                self.velha.Jogada()
                self.__Draw()
        
        # Finaliza o pygame quando sair do loop
        pygame.quit()
        return
    
    # Loop de renderização
    def __Draw(self):
        self.screen.fill("purple")

        self.__DrawTabuleiro()

        pygame.display.flip()
        self.clock.tick()
        return
    
    def __DrawTabuleiro(self):
        t = self.velha.tabuleiro
        for r in range(3):
            for c in range(3):
                p = self.velha.tabuleiro[r][c].value
                self.screen.blit(self.spritesheet.image_at((p*128, 0, 128, 128)), (128*c, 128*r))
        return