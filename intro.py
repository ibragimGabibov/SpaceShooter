import pygame
inIntro = True

background = pygame.image.load('assets/ui/background.jpg')
play_button = pygame.image.load('assets/ui/play_button.png')
quit_button = pygame.image.load('assets/ui/quit_button.png')
def showIntro(screen, width, height):
    global inIntro
    screen.blit(background, (0, 0))
    screen.blit(play_button, (width / 2 - play_button.get_width() / 2, height / 2 - play_button.get_height() / 2))
    screen.blit(quit_button, (width / 2 - quit_button.get_width() / 2, height / 2 - quit_button.get_height() / 2 + play_button.get_height() * 2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (width / 2 - play_button.get_width() / 2 <= mouse_pos[0] <= width / 2 + play_button.get_width() / 2) and (height / 2 - play_button.get_height() / 2 <= mouse_pos[1] <= height / 2 + play_button.get_height() / 2):
                inIntro = False
            elif (width / 2 - quit_button.get_width() / 2 <= mouse_pos[0] <= width / 2 + quit_button.get_width() / 2) and (height / 2 - quit_button.get_height() / 2 + play_button.get_height() * 2 <= mouse_pos[1] <= height / 2 + quit_button.get_height() / 2 + play_button.get_height() * 2):
                pygame.quit()