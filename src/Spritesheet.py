import pygame

# Classe para a definição das sprites do jogo
class Spritesheet:
    sheet: pygame.Surface

    def __init__(self, filename: str) -> None:
        try:
            self.sheet = pygame.image.load(filename).convert()
        except(pygame.error):
            print("Não foi possível carregar a spritesheet da imagem: "+filename)
            raise(SystemExit, "message")
        pass

    # Retorna uma Surface do pygame contendo apenas parte da imagem original demilitada por dado retangulo 
    # usada para renderização
    def image_at(self, rectangle) -> pygame.Surface:
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()

        image.set_colorkey((0, 0, 0))

        image.blit(self.sheet, (0,0), rect)


        return image