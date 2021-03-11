"""
Huvudfil, tar hand om användarens input och att displaya den.
"""
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #dimensionen på en ett shckbräde 8x8
SQ_SIZE = HEIGHT // DIMENSION #Storleken på varje ruta
MAX_FPS = 15 #för animationer
IMAGES = {}

"""
Laddar in bilderna, en gång
"""
def loadImages():
    pieces = ["wp", "bp", "bR", "bN", "bB", "bQ", "bK", "wQ", "wK", "wB", "wN", "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Pieces/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

"""
användar input, uppdaterar grafiken 
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.gameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

"""
Ritar upp brädet med alla pjaser
"""
def drawGameState(screen,gs):
    drawBoard(screen) #ritar rutorna på brädet
    drawPieces(screen,gs.board) #ritar pjäserja på brädet

"""
Ritar upp alla rutor på brädet
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
"""
Ritar pjäserna på rutorna
"""
def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

main()