from pickle import FALSE, TRUE
import pygame as p
from chessgame.constants import BLACK, SQUARE_COLOR_DARK,SQUARE_COLOR_LIGHT,ROWS,COLS,SQUARE_SIZE, WHITE,RED
from chessgame.pieces import Pawn



#chargement unique des images+redimentionnement:
IMAGES={}
def loadImages():
    PIECE=["wP","wN","wB","wR","wQ","wK","bP","bN","bB","bR","bQ","bK"]
    for piece in PIECE:
        image = p.image.load("chessgame/images/"+piece+".png")
        IMAGES[piece]=p.transform.scale(image,(SQUARE_SIZE,SQUARE_SIZE))


class Board():
    def __init__(self):
        #indique la pièce qui est sélectionnée sur le plateau
        self.selected_piece=None
        #couleure du joueur/change le plateau/les algo d'IA
        self.whiteToMove=True
        #coups particuliers joués qu'il faut enregistrer pour les règles spéciales
        self.moveLog=[]
        #plateau de jeu
        self.create_Board()
    
    #initialisation du plateau en fonction de la couleure du joueur
    def create_Board(self):
        #lignes de pions
        wP_line=[]
        bP_line=[]
        #ligne vide
        clean_line=[0]*COLS
        #lignes ou autres pieces
        #A faire :avec des objets piece qd les objets sont crées
        #reine et roi à inverser quand le joueur joue les noirs

        if self.whiteToMove:
            #lignes ou autres pieces
            #A faire :avec des objets piece qd les objets sont crées
            #reine et roi à inverser quand le joueur joue les noirs
            B_line=["bR","bN","bB","bQ","bK","bB","bN","bR"]
            W_line=["wR","wN","wB","wK","wQ","wB","wN","wR"]
            for i in range(COLS):
                wP_line.append(Pawn(WHITE,IMAGES["wP"],6,i))
                bP_line.append(Pawn(BLACK,IMAGES["bP"],1,i))
            self.board=[
                B_line,
                bP_line,
                clean_line*1,
                clean_line*1,
                clean_line*1,
                clean_line*1,    
                wP_line,
                W_line,
            ]
        else:
            B_line=["bR","bN","bB","bK","bQ","bB","bN","bR"]
            W_line=["wR","wN","wB","wQ","wK","wB","wN","wR"]
            for i in range(COLS):
                wP_line.append(Pawn(WHITE,IMAGES["bP"],6,i))
                bP_line.append(Pawn(BLACK,IMAGES["wP"],1,i))
            self.board=[
                W_line,
                wP_line,
                clean_line*1,
                clean_line*1,
                clean_line*1,
                clean_line*1, 
                bP_line,
                B_line,
            ]
     
    def __str__(self) -> str:
        ch1="piece select:"+self.selected_piece==None
        ch2="Aux blancs de jouer:"+self.whiteToMove==True
        ch3="Coup particulier joué:"+self.moveLog==[]
        return(ch1+"\n"+ch2+"\n"+ch3+"\n")
    
    #affichage des carrés du plateau
    def draw_squares(self,window):
        window.fill(SQUARE_COLOR_DARK)
        for row in range(ROWS):
            for col in range (row % 2,COLS,2):
                p.draw.rect(window,SQUARE_COLOR_LIGHT,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
    
    #affichage des pieces du plateau
    def drawPieces(self,window):
        for row in range(ROWS):
            for col in range(COLS):
                piece=self.board[row][col]
                if piece != 0:
                    if piece in ["wP","wN","wB","wR","wQ","wK","bP","bN","bB","bR","bQ","bK"]:
                        window.blit(IMAGES[piece], p.Rect(col*SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    else:
                        piece.draw_Piece(window)
    
    #affichage des cases ou l'on peut se déplacer en fontion des moves availables quand piece selectionner
    def draw_moves(self,window):
        if self.selected_piece!=None:
            for position in self.selected_piece.availables_moves:
                p.draw.rect(window,RED,(position[1]*SQUARE_SIZE,position[0]*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    
    
    #enlève une piece du plateau de jeu  
    def delete(self,piece):
        self.board[piece.row][piece.col]=0
    
    #ajoute une piece au plateau de jeu  
    def create(self,piece):
        r=piece.row
        c=piece.col
        print("coord d'ajout"+str(r)+str(c))
        self.board[r][c]=piece
        print("aff apres creation")
        for l in self.board:
            print(l)
            