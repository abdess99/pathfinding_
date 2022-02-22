import pygame
import sys
from create_map import put_zeros_before_int, create_map_visualizer
from Dijkstra_path_finding.dijkstra_algo import dijkstra_dict_visualizer
from A_star_path_finding.A_star_algo import a_star_dict_visualizer


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN=(0,255,0)
RED=(255,0,0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(WHITE)
    blockSize = 10  # Set the size of the grid block
    for x in range(200, WINDOW_WIDTH - 200, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)
    rect = pygame.Rect(85, 200, 30, 30)
    pygame.draw.rect(screen, BLACK, rect, 1)
    rect = pygame.Rect(85, 600, 30, 30)
    pygame.draw.rect(screen, BLACK, rect, 1)
    # text
    font = pygame.font.SysFont('Arial', 12, bold=True)
    img = font.render('Dijkstra', True, (0, 0, 0))
    screen.blit(img, (80, 240))
    font = pygame.font.SysFont('Arial', 12, bold=True)
    img = font.render('A*', True, (0, 0, 0))
    screen.blit(img, (95, 640))
    # Start button
    rect = pygame.Rect(WINDOW_WIDTH - 150, 375, 100, 50)
    pygame.draw.rect(screen, BLACK, rect, 1)
    font = pygame.font.SysFont('Arial', 17, bold=True)
    img = font.render('Start', True, (0, 0, 0))
    screen.blit(img, (WINDOW_WIDTH - 125, 390))

    pygame.display.flip()
    # initialize button position
    button_down = 0
    pressed_algo=None
    blocked_nodes=[]
    start_node=None
    end_node=None
    start_button=0
    while start_button==0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_down=event.button
            if button_down!=0:
                if button_down==1:
                    if pygame.mouse.get_pos()[0] > WINDOW_WIDTH - 150 and pygame.mouse.get_pos()[0] < WINDOW_WIDTH - 50 and pygame.mouse.get_pos()[1] > 375 and pygame.mouse.get_pos()[1] < 425:
                        if start_node is not None and end_node is not None and pressed_algo is not None:
                            start_button=1
                            rect = pygame.Rect(WINDOW_WIDTH - 150, 375, 100, 50)
                            pygame.draw.rect(screen, GREEN, rect, 0)
                            font = pygame.font.SysFont('Arial', 17, bold=True)
                            img = font.render('Start', True, WHITE)
                            screen.blit(img, (WINDOW_WIDTH - 125, 390))
                    if pygame.mouse.get_pos()[0]>85 and pygame.mouse.get_pos()[0]<115 and pygame.mouse.get_pos()[1]>200 and pygame.mouse.get_pos()[1]<230:
                        if pressed_algo!= 'Dijkstra':
                            pressed_algo = 'Dijkstra'
                            pygame.draw.line(screen, BLACK, (85, 200), (115, 230), width=3)
                            pygame.draw.line(screen, BLACK, (85, 230), (115, 200), width=3)
                            rect = pygame.Rect(85, 600, 30, 30)
                            pygame.draw.rect(screen, WHITE, rect, 0)
                            pygame.draw.rect(screen, BLACK, rect, 1)
                    if pygame.mouse.get_pos()[0]>85 and pygame.mouse.get_pos()[0]<115 and pygame.mouse.get_pos()[1]>600 and pygame.mouse.get_pos()[1]<630:
                        if pressed_algo != 'A*':
                            pressed_algo = 'A*'
                            pygame.draw.line(screen, BLACK, (85, 600), (115, 630), width=3)
                            pygame.draw.line(screen, BLACK, (85, 630), (115, 600), width=3)
                            rect = pygame.Rect(85, 200, 30, 30)
                            pygame.draw.rect(screen, WHITE, rect, 0)
                            pygame.draw.rect(screen, BLACK, rect, 1)
                    if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < WINDOW_WIDTH-200 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < WINDOW_HEIGHT:
                        if start_node is not None:
                            rect = pygame.Rect(int(start_node[2:]) * blockSize + 200, int(start_node[:2]) * blockSize, blockSize, blockSize)
                            pygame.draw.rect(screen, WHITE, rect, 0)
                            pygame.draw.rect(screen, BLACK, rect, 1)
                        start_node=put_zeros_before_int(pygame.mouse.get_pos()[1]//blockSize)+put_zeros_before_int((pygame.mouse.get_pos()[0]-200)//blockSize)
                        rect = pygame.Rect(int(start_node[2:]) * blockSize + 200, int(start_node[:2]) * blockSize, blockSize, blockSize)
                        pygame.draw.rect(screen, RED, rect, 0)
                        if start_node in blocked_nodes:
                            blocked_nodes.remove(start_node)
                        if end_node==start_node:
                            end_node=None
                if button_down == 2:
                    if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < WINDOW_WIDTH-200 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < WINDOW_HEIGHT:
                        if end_node is not None:
                            rect = pygame.Rect(int(end_node[2:]) * blockSize + 200, int(end_node[:2]) * blockSize, blockSize, blockSize)
                            pygame.draw.rect(screen, WHITE, rect, 0)
                            pygame.draw.rect(screen, BLACK, rect, 1)
                        end_node=put_zeros_before_int(pygame.mouse.get_pos()[1]//blockSize)+put_zeros_before_int((pygame.mouse.get_pos()[0]-200)//blockSize)
                        rect = pygame.Rect(int(end_node[2:]) * blockSize + 200, int(end_node[:2]) * blockSize, blockSize, blockSize)
                        pygame.draw.rect(screen, GREEN, rect, 0)
                        if end_node in blocked_nodes:
                            blocked_nodes.remove(end_node)
                        if end_node==start_node:
                            start_node=None
                if button_down == 3:
                    if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < WINDOW_WIDTH - 200 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < WINDOW_HEIGHT:
                        clicked_node = put_zeros_before_int(pygame.mouse.get_pos()[1]//blockSize)+put_zeros_before_int((pygame.mouse.get_pos()[0]-200)//blockSize)
                        if clicked_node not in blocked_nodes:
                            blocked_nodes.append(clicked_node)
                            rect = pygame.Rect(int(clicked_node[2:]) * blockSize + 200, int(clicked_node[:2]) * blockSize, blockSize, blockSize)
                            pygame.draw.rect(screen, BLACK, rect, 0)
                        if clicked_node== start_node:
                            start_node=None
                        if clicked_node== end_node:
                            end_node=None



            if event.type == pygame.MOUSEBUTTONUP:
                button_down=0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

    map_dict= create_map_visualizer((((WINDOW_WIDTH - 400)//blockSize), WINDOW_HEIGHT//blockSize) , blocked_nodes)
    if pressed_algo== 'Dijkstra':
        dijkstra_dict_visualizer(map_dict, start_node, end_node, blockSize, screen)
    if pressed_algo== 'A*':
        a_star_dict_visualizer(map_dict, start_node, end_node, blockSize, screen)
    while start_button == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()



main()
