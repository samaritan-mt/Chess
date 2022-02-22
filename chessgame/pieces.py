import pygame as p
from .constants import SQUARE_SIZE, WHITE

class Piece:
    def __init__(self,color,image,row,col):
        self.color=color
        self.image=image
        self.row=row
        self.col=col
        self.calc_pos()
        self.clear_availables_moves()
        
    def piece_move(self,row,col):
        self.row=row
        self.col=col
        self.calc_pos()
        
    
    def calc_pos(self):
        self.x=self.col*SQUARE_SIZE
        self.y=self.row*SQUARE_SIZE
        
    def clear_availables_moves(self):
        self.availables_moves=[]
        
    def draw_Piece(self,window):
        window.blit(self.image, p.Rect(self.col*SQUARE_SIZE,self.row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
    
    def moveTo(self,row,col,board):
        board.delete(self)
        self.piece_move(row,col)
        board.create(self)
        board.selected_piece=None
        self.get_available_moves(board)
        
class Pawn(Piece):
    def __init__(self,color,image,row,col):
        super().__init__(color,image,row,col)
        self.first_move=True    #1er coup pt avancer de deux cases
        
    def get_available_moves(self,board):
        self.clear_availables_moves()
        if self.color==WHITE and board.whiteToMove==True:
            print("ok get aai moves")
            for l in board.board:
                print(l)
            print (board.board[self.row-1][self.col])
            print (board.board[self.row-2][self.col])
            if board.board[self.row-1][self.col]==0:
                self.availables_moves.append((self.row-1,self.col))
            if self.first_move and board.board[self.row-2][self.col]==0:
                self.availables_moves.append((self.row-2,self.col))
        print(self.availables_moves)
    
    def moveTo(self,row,col,board):
        super().moveTo(row,col,board)
        self.first_move=False
        
            
    
        
        
class Bishop(Piece):
    def __init__(self,type,color,image,row,col):
        super().__init__(type,color,image,row,col)
        self.first_move=True    #1er coup pt avancer de deux cases
        
    def get_available_moves(self):
        self.clear_availables_moves()
        
class Rock(Piece):
    def __init__(self,type,color,image,row,col):
        super().__init__(type,color,image,row,col)
        self.first_move=True    #1er coup pt avancer de deux cases
        
    def get_available_moves(self):
        self.clear_availables_moves()
        
class Queen(Piece):
    def __init__(self,type,color,image,row,col):
        super().__init__(type,color,image,row,col)
        self.first_move=True    #1er coup pt avancer de deux cases
        
    def get_available_moves(self):
        self.clear_availables_moves()
        
class King(Piece):
    def __init__(self,type,color,image,row,col):
        super().__init__(type,color,image,row,col)
        self.first_move=True    #1er coup pt avancer de deux cases
        
    def get_available_moves(self):
        self.clear_availables_moves()
        
        