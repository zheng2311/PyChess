# imports from modules
import pygame
import time
import sys

# creates a board
board = [['  ' for i in range(8)] for i in range(8)]

class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image

bp = Piece('b', 'p', 'b_pawn.png')
wp = Piece('w', 'p', 'w_pawn.png')
bk = Piece('b', 'k', 'b_king.png')
wk = Piece('w', 'k', 'w_king.png')
br = Piece('b', 'r', 'b_rook.png')
wr = Piece('w', 'r', 'w_rook.png')
bb = Piece('b', 'b', 'b_bishop.png')
wb = Piece('w', 'b', 'w_bishop.png')

