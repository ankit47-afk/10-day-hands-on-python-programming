import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("X O Game")
white = (255,255,255)
black = (0,0,0)
board =[["","",""],["","",""],["","",""]]
player = "X"
font = pygame.font.Font(None, 100)
run = True
while run:
    screen.fill(white)
    pygame.draw.line(screen,black,(200,0),(200,600),5)
    pygame.draw.line(screen,black,(400,0),(400,600),5)
    pygame.draw.line(screen,black,(0,200),(600,200),5)  
    pygame.draw.line(screen,black,(0,400),(600,400),5)
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, black)
                text_rect = text.get_rect(center=(col*200 + 100, row*200 + 100))
                screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
    pygame.display.flip()
pygame.quit()



