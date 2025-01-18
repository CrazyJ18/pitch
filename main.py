import pygame, os

pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
running = True
card = pygame.image.load(os.path.join('assets', 'cards', 'ace_of_spades.webp'))
card = pygame.transform.smoothscale_by(card.convert_alpha(), 0.3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("dark green")
    screen.blit(card, (700, 400))

    # deal hands of 9 cards
    # bid
    # winner declares suit
    # other players discard all cards not in suit
    # other players are dealt cards until 6 cards in their hands
    # winner receives rest of deck
    # winner discards out-of-suit cards until 6 cards in hand
    # players take tricks
    # round ends when all cards in suit have been played

    pygame.display.flip()
    clock.tick(60)

pygame.quit()