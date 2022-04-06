class Sokaban:
     personaje=0
     espacio=1
     caja=2
     meta=3
     pared=4
     personaje_meta=5
     caja_meta=6 
     mapa=[]
     personaje_fila=0
     personaje_columna=0
    
     def __int__(self):
       pass
    
     def leermapa(self):
       self.mapa=[
     [3,3,3,3,3,3]
     [3,1,1,1,3,3] 
     [3,1,1,0,1,3]
     [3,1,1,1,1,3]
     [3,3,3,3,3,3]
     ] 
     self.personaje_fila=3
     self.personaje_columna=5
    
     def imprimirmapa(self):
      for fila in self.mapa:
          print(fila)
            
     def moverderecha(self):
        print("mover derecha")

     #5. personaje, espacio
     if  (self.mapa[self.personaje_fila][self.personaje_columna] == self.personaje
     and self.mapa[self.personaje_fila][self.personaje_columna + 1]== self.espacio):

      self.mapa[self.personaje_fila][self.personaje_columna]=self.espacio
      self.mapa[self.personaje_fila][self.personaje_columna+1]=self.personaje
      self.personaje_columna+=1
       #6.personaje,meta
     elif (self.mapa[self.personaje_fila][self.personaje_columna]==0
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==4):

          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna+1]=5
          self.personaje_columna+=1
          #7personaje,caja ,espacio
         elif (self.mapa[self.personaje_fila][self.personaje_columna]==0
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==2):
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==1):   
         
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna]=0
          self.mapa[self.personaje_fila][self.personaje_columna+1]=2
          self.personaje_columna+=1
          #8personaje,caja,meta
          elif (self.mapa[self.personaje_fila][self.personaje_columna]==0
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==2):
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==4): 
    
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna]=0
          self.mapa[self.personaje_fila][self.personaje_columna+1]=6
          self.personaje_columna+=1
          #9personaje ,caja_meta,espacio
         elif (self.mapa[self.personaje_fila][self.personaje_columna]==0
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==6):
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==1): 

          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna]=5
          self.mapa[self.personaje_fila][self.personaje_columna+1]=2
        #10 personaje,caja_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna]==0
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==6):
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==1):

    self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna]=5
          self.mapa[self.personaje_fila][self.personaje_columna+1]=6
          self.personaje_columna+=1
      #11personaje_meta,espacio
          elif (self.mapa[self.personaje_fila][self.personaje_columna]==5
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==1):

          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna+1]=5
          self.personaje_columna+=1
        
       #12 personaje_meta,metav
        elif (self.mapa[self.personaje_fila][self.personaje_columna]==5
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==4):

          self.mapa[self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila][self.personaje_columna+1]=5
          self.personaje_columna+=1
         #13 personaje_meta,caja,espacio
         elif (self.mapa[self.personaje_fila][self.personaje_columna]==5
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==2):
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==1):

          self.mapa[self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila][self.personaje_columna]=0
          self.mapa[self.personaje_fila][self.personaje_columna+1]=2
          self.personaje_columna+=1
          #14personaje_meta,caja,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna]==5
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==2):
      and self.mapa[self.personaje_fila][self.personaje_columna+1]==4):

          self.mapa[self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila][self.personaje_columna]=0
          self.mapa[self.personaje_fila][self.personaje_columna+1]=6
          self.personaje_columna+=1
 #


     def moverIzquierda(self): 
       print("Moverizquierda")
         
     def moverArriba(self):
        print("Mover arriba")
         
     def  moverAbajo(self):
              print("Mover abajo")
     def jugar (self):
      Instrucciones="a-izquierda\nd-derecha\nw-arriba\ns-abajo"
     print(instrucciones)
     self.leermapa()
     while True:
            self.imprimirmapa()
            movimiento = input("mover hacia:")
            if movimiento == "d":
                self.derecha()
            elif movimiento == "a":
                self.moverizquierda()
            elif movimiento == "w":
                self.movimientoarriba()
            elif movimiento == "s":
                self.movimientoabajo()
            elif movimiento == "q":
                print("salir del juego")
                break
    
    
         juego=sokoban()
         juego.jugar()
          
            
   
         
