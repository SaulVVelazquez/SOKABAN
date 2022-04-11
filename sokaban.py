class Sokoban:
    """
    0_personaje
    1_espacio
    2_caja
    3_pared
    4_metas
    5-persoaje_meta
    6_caja_meta
    """
  
    mapa=[]
    

    personaje_fila= 3
    personaje_columna= 3
    
    def leerMapa(self):
        self.mapa=[
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 5, 6, 4, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]


        
    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)
            
    def moverDerecha(self):
        print("Mover Derecha")
          # 5 personaje,espacio 0,1 -> 1,0
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1]= 0
            self.personaje_columna += 1
            print("personaje,espacio")
    # 6 personaje, meta 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
            print("personaje,meta")
    #7 personaje,caja,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] ==2 and self.mapa [self.personaje_fila][self.personaje_columna +2 ]==1):
           self.mapa[self.personaje_fila][self.personaje_columna]= 1 
           self.mapa[self.personaje_fila][self.personaje_columna + 1]=0
           self.mapa[self.personaje_fila][self.personaje_columna + 2]=2
           self.personaje_columna   +=1 
           print("personaje,caja,espacio") 
    #8  personaje,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna +1]==2 and self.mapa [self.personaje_fila][self.personaje_columna +2]==4): 
          self.mapa[self.personaje_fila][self.personaje_columna]=  1
          self.mapa[self.personaje_fila][self.personaje_columna + 1]=0
          self.mapa[self.personaje_fila][self.personaje_columna + 2]=6 
          self.personaje_columna     +=1
          print("personaje,caja,meta")  
    #9    personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna +1 ] == 6  and self.mapa [self.personaje_fila][self.personaje_columna + 2] == 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1
          self.mapa[self.personaje_fila][self.personaje_columna + 1] =5
          self.mapa[self.personaje_fila][self.personaje_columna + 2] =2
          self.personaje_columna += 1  
          print("personaje,caja_meta,espacio")  
    #10 personaje,caja_meta,meta 
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna +1]==6  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1   
          self.mapa[self.personaje_fila][self.personaje_columna +1]=5
          self.mapa[self.personaje_fila][self.personaje_columna +2 ]=6
          self.personaje_columna     +=1 
          print("personaje,caja_meta,meta")  
    #11   personaje_meta,espacio 5,1->
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1
            print("personaje_meta,espacio")
          
    #12 personaje_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
            print("personaje_meta,meta")
            #13 personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==2  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna ]=  4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=0
          self.mapa[self.personaje_fila][self.personaje_columna +2]=2
          self.personaje_columna     +=1  
          print("personaje_meta,caja,espacio")  
        #14 personaje_meta,caja_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==2  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=0
          self.mapa[self.personaje_fila][self.personaje_columna +2]=6
          self.personaje_columna     +=1  
          print("personaje_meta,caja_meta") 
          #15personaje_meta,caja_meta,espacio  
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==6  and self.mapa [self.personaje_fila][self.personaje_columna+ 2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=5
          self.mapa[self.personaje_fila][self.personaje_columna +2]=2
          self.personaje_columna     +=1  
          print("personaje_meta,caja_meta,espacio ")   
          #16 personaje_meta,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==6  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=5
          self.mapa[self.personaje_fila][self.personaje_columna +2]=6
          self.personaje_columna     +=1     
          print("personaje_meta,caja_meta,meta")      
        
            
    def moverIzquierda(self):
        print("Mover izquierda")
    
    def moverArriba(self):
        print("Mover arriba")
    
    def moverAbajo(self):
        print("Mover abajo")
    
    def jugar(self):
        instrucciones="a-izquierda\nd-derecha\nw-arriba\ns-abajo"
        print(instrucciones)
        self.leerMapa()
        while True:
            self.imprimirMapa()
            movimiento = input("Mover Hacia: ")
            if movimiento == "d":
                self.moverDerecha()
            elif movimiento == "a":
                self.moverIzquierda()
            elif movimiento == "w":
                self.moverArriba()
            elif movimiento == "s":
                self.moverAbajo()
            elif movimiento == "q":
              print("salir del juego")
              break
                
juego = Sokoban()
juego.jugar()

          
            
   
         
