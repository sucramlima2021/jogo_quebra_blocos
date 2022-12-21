import pygame as pg
import sys
import random

pg.init()
telaw = 800
telah = 600
tela = pg.display.set_mode((telaw,telah))
titulo = pg.display.set_caption("Brick Breaker")

class Game():
    def __init__(self):
       
        self.tela = tela
        self.init_px = 375
        self.init_py = 550
        self.largura_p = 80
        self.altura_p = 10
        self.muro = Muro()
        self.muro.draw_blocos()
        self.inix = 380
        self.iniy = 550
        self.lista_bateu = []
        self.sentidox = 0
        self.sentidoy = 0
        self.base = pg.Rect(0,0,1,1)
        self.incrementox = 0.01
        self.perdeu = False
        
    def draw(self):
        
        pg.draw.rect(self.tela, (0,0,0), (0,0,800,600))
        if self.perdeu == True:
            font = pg.font.SysFont(None, 50)
            text = font.render('Você perdeu!!', True, (255,255,255))
            self.tela.blit(text, [250, 200])
            text = font.render('Pressione o Backspace para recomecar.', True, (255,255,255))
            self.tela.blit(text, [80, 250])
        else:
            i = -1
            
            #desenha os blocos
            for m in self.muro.lista:
                x,y,w,h = m
                i += 1
                pg.draw.rect(tela, (self.muro.cores[i][0], self.muro.cores[i][1], self.muro.cores[i][2]),
                            (x, y, w, h))
                    
            pg.draw.rect(self.tela, (255,0,0), (self.init_px, self.init_py, self.largura_p, self.altura_p))
            self.base = pg.Rect(self.init_px, self.init_py, self.largura_p, self.altura_p)
            
            self.mover()
            
    def eventos(self):
        for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    sys.exit(0)
                    
        move = pg.key.get_pressed()
        if move[pg.K_LEFT]: 
            if self.init_px <= 2:
                pass
            else:
                self.init_px -= 0.3
        if move[pg.K_RIGHT]: 
            if self.init_px >= telaw - self.largura_p:
                pass
            else:
                self.init_px += 0.3
        if move[pg.K_BACKSPACE]: 
            self.reinicia()
    
    def reinicia(self):
        self.perdeu = False
        self.init_px = 375
        self.init_py = 550
        self.muro.lista = []
        self.muro.cores = []
        self.muro.draw_blocos()
        self.inix = 380
        self.iniy = 550
        self.lista_bateu = []
        self.sentidox = 0
        self.sentidoy = 0
        self.incrementox = 0.01
        
    def mover(self):
        
        pg.draw.circle(tela, (255,255,255), (self.inix, self.iniy),5)
        if self.sentidox == 0:
            self.inix += self.incrementox
        else:
            self.inix -= self.incrementox
        if self.sentidoy == 0:
            self.iniy -=0.2
        else: 
            self.iniy +=0.2
        bola = pg.Rect(self.inix, self.iniy, 5, 5)
        bateu = pg.Rect.collidelistall(bola, self.muro.lista)
        if len(bateu) > 0:
           
            self.sentidoy = 1
            for i in bateu:
                try:
                    self.muro.lista.pop(i)
                    self.muro.cores.pop(i)
                except:
                    print('erro ao retirar da lista o indice ', i)
        if pg.Rect.collidepoint(self.base, (self.inix, self.iniy)):
            self.sentidoy = 0
            if self.inix < self.init_px + (self.largura_p / 2) :
                inc = ((self.init_px + (self.largura_p / 2)) - self.inix)*0.01
                self.sentidox = 1
                self.incrementox = inc
            else:
                inc = (self.inix - (self.init_px + (self.largura_p / 2)))*0.01
                self.sentidox = 0
                self.incrementox = inc
        if self.inix >= 798:
            self.sentidox = 1
        if self.inix <= 2:
            self.sentidox = 0
        
            
        
        if self.iniy <= 1:
            self.sentidoy = 1
        if self.iniy >= 600:
            self.perdeu = True
            
        
    
    def run(self):
        while True:
            self.draw()
            self.eventos()
            

            pg.display.flip()
            
            
class Muro():
    def __init__(self):
        self.largura = 60
        self.altura = 10
        self.quantx = telaw // self.largura
        self.linhas = 8
        self.lista = []
        self.cores = []
        
    def draw_blocos(self):
        px1 = 5
        py1 = 5
        for linha in range(self.linhas):
            for q in range(self.quantx):
                cor1 = random.randint(20,255)
                cor2 = random.randint(20,255)
                cor3 = random.randint(20,255)
                self.cores.append([cor1, cor2, cor3])
                self.lista.append(pg.Rect(px1, py1, self.largura, self.altura))
                pg.draw.rect(tela, (cor1, cor2, cor3), (px1, py1, self.largura, self.altura))
                px1 = px1 + self.largura
                
            py1 = py1 + self.altura
            px1 = 5
        
            
if __name__ == '__main__':
    game = Game()
    game.run()