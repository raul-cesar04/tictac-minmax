import pygame
from Velha import Velha
from Spritesheet import Spritesheet

# Botões
class Button:
    rect: pygame.Rect
    pos: tuple
    used: bool

    def __init__(self, pos: tuple, dimensions: tuple) -> None:
        self.used = False
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], dimensions[0], dimensions[1])

class Game:
    # Pygame
    screen: pygame.Surface
    clock: pygame.time.Clock
    running: bool
    font: pygame.font.Font

    # Jogo da velha
    velha: Velha
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    spritesheet: Spritesheet

    def __init__(self, titulo: str, width: int, height: int) -> None:

        # Inicializa pygame e seus componentes
        pygame.init()
        pygame.display.set_caption(titulo)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

        # Jogo da velha e seus componentes
        self.velha = Velha()

        # Start
        self.Start()
        return
    def Start(self):
        self.velha.Inicio()

        # Botões do tabuleiro
        for r in range(3):
            for c in range(3):
                self.tabuleiro[r][c] = Button((c*128, r*128), (128, 128))

        # Carrega recursos
        self.spritesheet = Spritesheet("assets/velha_128.png")
        self.font = pygame.font.SysFont("comic_sans.ttf", 35)
        self.__Draw()

    def Update(self):

        # Loop principal
        while self.running:
            mouse_b: bool = False
            keys_pressed: pygame.key.ScancodeWrapper = []
            # Capturar eventos de input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    mouse_b = pygame.mouse.get_pressed()[0]
                
                if(event.type == pygame.KEYDOWN):
                    keys_pressed = pygame.key.get_pressed()


            # Captura o input e processa as jogadas se o jogo ainda não tem um fim
            if(not self.velha.fim_jogo):
                if(mouse_b):
                    b = self.__CheckButtonPressed()
                    if(b != None):
                        self.velha.Jogada(( int(b.pos[0]/128), int(b.pos[1]/128)))
                        self.__Draw()
            else:
                if(len(keys_pressed) > 0 and keys_pressed[pygame.K_r]):
                    self.Start()

        # Finaliza o pygame quando sair do loop
        pygame.quit()
        return
    
    # Loop de renderização
    def __Draw(self):
        self.screen.fill((128, 128, 128))

        self.__DrawTabuleiro()
        self.__DrawText("Jogador 1: O", (400, 8))
        self.__DrawText("Jogador 2: X", (400, 32))
        self.__DrawText("Vez de: "+self.velha.vez.to_str(), (16, 384))
        
        if(self.velha.fim_jogo):
            vencedor_str: str = self.velha.vencedor.to_str() if(self.velha.vencedor != None) else "Deu Velha!"
            self.__DrawText("Fim de jogo. Vencedor: "+vencedor_str, (16, 414), "red")
            self.__DrawText("Pressione 'R' para jogar novamente", (16, 444), "yellow")
        pygame.display.flip()
        self.clock.tick()
        return
    
    # Método para renderizar o tabuleiro
    def __DrawTabuleiro(self):
        t = self.tabuleiro
        for r in range(3):
            for c in range(3):
                p = self.velha.tabuleiro[r][c].value
                b: Button = t[r][c]
                self.screen.blit(self.spritesheet.image_at((p*128, 0, 128, 128)), b.pos)
        return
    
    # Método para renderizar textos
    def __DrawText(self, texto: str, pos: tuple, color: pygame.Color = "white"):
        img = self.font.render(texto, True, color)
        self.screen.blit(img, pos)


    # Verifica se algum botão foi pressionado
    def __CheckButtonPressed(self)->Button:
        for r in range(3):
            for c in range(3):
                mouse_pos = pygame.mouse.get_pos()
                b: Button = self.tabuleiro[r][c]

                if(b.rect.collidepoint(mouse_pos)):
                    return b
        
        return None
                
                