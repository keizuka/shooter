import pygame
pygame.init()


# classe qui va representer le joueur
class Player(pygame.sprite.Sprite):

    def __int__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400


# générer la fenetre du jeu
pygame.display.set_caption("Hell_Fire")
screen = pygame.display.set_mode((800, 600))

# importer l'arrier plan du jeu
background = pygame.image.load('PygameAssets-main/bg.jpg')

# charger le joueur
player = Player()

running = True  # pour maintenir la fenetre ouvert

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -350))

    # appliquer l'image du joueur
    screen.blit(player.image, (0, 0))

    # mettre a jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # pour verifier que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
