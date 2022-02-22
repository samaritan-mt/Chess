import pygame as p
from chessgame.constants import WIDTH,HEIGHT,SQUARE_SIZE
from chessgame.board import Board, loadImages
from chessgame.pieces import Pawn,Piece



#initialisation de l'affichage
WINDOW=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption('chessGame')
FPS = 60




#boucle d'événement du jeu
def main():
    run=True
    clock= p.time.Clock()
    #Chargement unique des pièces
    loadImages()
    board=Board()
    
    while run:
        clock.tick(FPS)
        
        for event in p.event.get():    #récupère les évenements sur la fenêtre
            if event.type == p.QUIT:
                run = False
            elif event.type == p.MOUSEBUTTONDOWN:
                if p.mouse.get_pressed()[0]:
                    location=p.mouse.get_pos()
                    row,col=get_position(location)
                    print(("row"+str(row),"col"+str(col)))
                    #bouger une piece
                    if board.selected_piece!=None and (row,col) in board.selected_piece.availables_moves:
                        board.selected_piece.moveTo(row,col,board)
                    #selectionner une piece
                    elif board.board[row][col]!=0:
                        board.selected_piece=board.board[row][col]
                        board.board[row][col].get_available_moves(board)
                        print(board.board[row][col].availables_moves)
                    #plus de selection si autre cas
                    elif board.board[row][col]==0:
                        board.selected_piece=None                    
        #dessine le patern de cases
        board.draw_squares(WINDOW)
        #dessine le patern de pieces
        board.drawPieces(WINDOW)
        #dessine les moves autorisés selon la piece seelectionnée
        board.draw_moves(WINDOW)
        p.display.update()    
    p.quit()
#converti coord x/y en row/col
def get_position(location):
    row=location[1]//SQUARE_SIZE
    col=location[0]//SQUARE_SIZE
    return(row,col)
#appel du jeu
main()

#TODO
'''
faire les moves des pions...caval fou reine roi
    céer l'affichage avec un petit cercle sur les deplacements possibles du pion

faire le deplacement moveTo du pion...

faire les règles spéciales






affichage centré pt importe HEIGHT_&_WIDTH
'''