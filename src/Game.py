import pygame

class Game:
    # Pygame
    screen: pygame.Surface
    clock: pygame.time.Clock
    running: bool

    # Jogo da velha
    

    def __init__(self, titulo: str, width: int, height: int) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        return
    
    def Update(self):
        # Loop principal
        while self.running:
            # Capturar eventos de input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.__Draw()
        
        # Finaliza o pygame quando sair do loop
        pygame.quit()
        return
    
    # Loop de renderização
    def __Draw(self):
        self.screen.fill("purple")

        pygame.display.flip()
        self.clock.tick()
        return