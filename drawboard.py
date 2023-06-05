import pygame
import pygame.gfxdraw
from math import cos, sin, pi, radians
from pygame import gfxdraw
import Tile

class Board:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.black = (40, 40, 40)
        self.white = (255, 255, 255)
        self.teal = (0, 128, 128)
        self.red = (255, 0, 0)
        self.blue = (0,0,255)
        self.boardSize = 10
        self.hex_radius = 20
        self.x_offset, self.y_offset = 60, 60
        self.text_offset = 45
        self.hexDictionary = {}



        #window size and color
        self.winWidth = self.x_offset + (2 * self.hex_radius) * self.boardSize + self.hex_radius * self.boardSize
        self.winHeight = round(self.y_offset + (1.75 * self.hex_radius) * self.boardSize)

        self.screen = pygame.display.set_mode(
            (self.winWidth, self.winHeight))
        
        self.screen.fill(self.white)

        #object
        self.s = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA, 32)
        self.color = [self.black] * (self.boardSize ** 2)
        self.rects = []
        self.node = None
        self.fonts = pygame.font.SysFont("Arial", 20)




    def drawHexagon(self, surface, color: tuple, position: tuple, node: int):
        #print("Drawing hexagon at node: ", node)
        polyEdges = 6
        x, y = position
        offset = 3

        self.hexDictionary[node] = [(x + (self.hex_radius + offset) * cos(radians(90) + 2 * pi * _ / polyEdges),
                                     y + (self.hex_radius + offset) * sin(radians(90) + 2 * pi * _ / polyEdges))
                                 for _ in range(polyEdges)]
        self.hexDictionary[node].append((x,y))

        gfxdraw.aapolygon(self.s, self.hexDictionary[node], color)

        #Make the hexagon filled, we use a polygon and then draw the hexagon from mathematical definition
        gfxdraw.filled_polygon(self.s,
                                [(x + self.hex_radius * cos(radians(90) + 2 * pi * _ / polyEdges),
                                y + self.hex_radius * sin(radians(90) + 2 * pi * _ / polyEdges))
                                for _ in range(polyEdges)],
                                self.red)
        

        #The hexagon outline to be able to see it on the white background

        gfxdraw.aapolygon(surface,
                  [(x + self.hex_radius * cos(radians(90) + 2 * pi * _ / polyEdges),
                    y + self.hex_radius * sin(radians(90) + 2 * pi * _ / polyEdges))
                   for _ in range(polyEdges)],
                  self.black)

        #drawing the boundaries
        #LEFT-RIGHT offset
        LR_boundry_offset = [3, -3]
        #TOP-BOTTOM offset
        TB_boundry_offset = [0, 3]

        #leftside
        if node % self.boardSize:
            if node > self.boardSize:
                #calculate the coordinates of the hexagons
                drawCoords = ([self.hexDictionary[node - self.boardSize][1][_] - LR_boundry_offset[_] for _ in range(2)],
                            [self.hexDictionary[node - self.boardSize][0][_] - LR_boundry_offset[_] for _ in range(2)],
                            [self.hexDictionary[node][1][_] - LR_boundry_offset[_] for _ in range(2)])
                #Fill the hexagon
                gfxdraw.filled_polygon(self.s, drawCoords, self.teal)
                gfxdraw.aapolygon(self.s, drawCoords, self.teal)
                
        #rightside
        if (node + 1) % self.boardSize == 0:
            if node > self.boardSize:
                #calculate the coordinates of the hexagons
                drawCoords = ([self.hexDictionary[node - self.boardSize][4][_] + LR_boundry_offset[_] for _ in range(2)],
                            [self.hexDictionary[node - self.boardSize][5][_] + LR_boundry_offset[_] for _ in range(2)],
                            [self.hexDictionary[node][4][_] + LR_boundry_offset[_] for _ in range(2)])
                #Fill the hexagon
                gfxdraw.filled_polygon(self.s, drawCoords, self.teal)
                gfxdraw.aapolygon(self.s, drawCoords, self.teal)


        #topside
        if 0 < node < self.boardSize:
            #calculate the coordinates of the hexagons
            drawCoords = ([self.hexDictionary[node - 1][3][_] - TB_boundry_offset[_] for _ in range(2)],
                        [self.hexDictionary[node - 1][4][_] - TB_boundry_offset[_] for _ in range(2)],
                        [self.hexDictionary[node][3][_] - TB_boundry_offset[_] for _ in range(2)])
            #Fill the hexagon
            gfxdraw.filled_polygon(self.s, drawCoords, self.red)
            gfxdraw.aapolygon(self.s, drawCoords, self.red)

        #bottomside
        if self.boardSize ** 2 - self.boardSize < node < self.boardSize ** 2:
            #calculate the coordinates of the hexagons
            drawCoords = ([self.hexDictionary[node - 1][0][_] + TB_boundry_offset[_] for _ in range(2)],
                        [self.hexDictionary[node - 1][5][_] + TB_boundry_offset[_] for _ in range(2)],
                        [self.hexDictionary[node][0][_] + TB_boundry_offset[_] for _ in range(2)])
            #Fill the hexagon   
            gfxdraw.filled_polygon(self.s, drawCoords, self.red)
            gfxdraw.aapolygon(self.s, drawCoords, self.red)
        
        #coodinates of the board
        rect = pygame.draw.rect(
            self.s,
            self.color[node],
                pygame.Rect(
                    x - self.hex_radius + offset, 
                    y - self.hex_radius / 2, 2 * self.hex_radius - (2 * offset ),
                    self.hex_radius)
        )

        self.rects.append(rect)


        ''' IMPROVE TOUCHZONE TO DO:
        touchZone = pygame.Rect(0,0,50,
                                150)

        fodder = 10
        n = len(self.hexDictionary)

        startPoint = (self.hexDictionary[0][3][0] - fodder, self.hexDictionary[0][3][1] - fodder)
        secondPoint = (self.hexDictionary[self.boardSize][4][0] + fodder, self.hexDictionary[self.boardSize][4][1] + fodder)
        thirdPoint = (self.hexDictionary[(n-1) - self.boardSize][4][0] - fodder, self.hexDictionary[(n-1) - self.boardSize][4][1] - fodder)
        endPoint = (self.hexDictionary[n-1][5][0] + fodder, self.hexDictionary[n-1][5][1] + fodder)
        
        print(self.hexDictionary)
        
        points = [(self.hexDictionary[0][3][0] - fodder, self.hexDictionary[0][3][1] - fodder),
                    (self.hexDictionary[self.boardSize][4][0] + fodder, self.hexDictionary[self.boardSize][4][1] + fodder),
                    (self.hexDictionary[(n-1) - self.boardSize][4][0] - fodder, self.hexDictionary[(n-1) - self.boardSize][4][1] - fodder),
                    (self.hexDictionary[n-1][5][0] + fodder, self.hexDictionary[n-1][5][1] + fodder)]

        polygon_mask = pygame.Surface((self.winWidth, self.winHeight), pygame.SRCALPHA)
        pygame.gfxdraw.filled_polygon(polygon_mask, points, (0,0,0))  # White fill color
        polygon_mask = pygame.mask.from_surface(polygon_mask)

        #pygame.draw.rect(self.screen, (0,0,0), touchZone)'''




        
    def draw_board_coordinates(self):
        alphabet = list(map(chr, range(97, 123)))

        for _ in range(self.boardSize):
            # Columns
            text = self.fonts.render(alphabet[_].upper(), True, self.red)
            text_rect = text.get_rect()
            text_rect.center = (self.x_offset + (2 * self.hex_radius) * _, self.text_offset / 2)
            self.screen.blit(text, text_rect)

            # Rows
            text = self.fonts.render(str(_), True, self.blue)
            text_rect = text.get_rect()
            text_rect.center = (
                (self.text_offset / 4 + self.hex_radius * _, self.y_offset + (1.75 * self.hex_radius) * _))
            self.screen.blit(text, text_rect)



    def draw_board(self):
        counter = 0
        for row in range(self.boardSize):
            for column in range(self.boardSize):
                self.drawHexagon(self.screen, self.black, self.get_coordinates(row, column), counter)
                counter += 1

        self.draw_board_coordinates()

    def drawChosenTile(self, x, y, color):
        #fill color
        gfxdraw.filled_polygon(self.screen,
                               [(x + self.hex_radius * cos(radians(90) + 2 * pi * _ / 6),
                                 y + self.hex_radius * sin(radians(90) + 2 * pi * _ / 6))
                                for _ in range(6)],
                               color)

        #outline color
        gfxdraw.aapolygon(self.screen,
                          [(x + self.hex_radius * cos(radians(90) + 2 * pi * _ / 6),
                            y + self.hex_radius * sin(radians(90) + 2 * pi * _ / 6))
                           for _ in range(6)],
                          self.black)

        pygame.display.update()



    def get_coordinates(self, row: int, column: int):
        x = self.x_offset + (2 * self.hex_radius) * column + self.hex_radius * row
        y = self.y_offset + (1.75 * self.hex_radius) * row

        return x, y





