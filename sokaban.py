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
    personaje_columna= 6
    
    def leerMapa(self):
        self.mapa=[
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3,3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,3],
            [3, 1, 4, 1, 1, 1, 0, 2, 4, 1,1,3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3,3],
        ]


        
    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)
            
    def moverDerecha(self):
        print("Mover Derecha")
    #5 personaje,espacio 0,1 -> 1,0
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
        #14 personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==2  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 4):
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
    #17 personaje, espacio 
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1]= 1
            self.personaje_columna -= 1
            print("personaje,espacio")    
        #18 personaje,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
            print("personaje,meta")   
        #19 personaje,caja,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] ==2 and self.mapa [self.personaje_fila][self.personaje_columna -2 ]==1):
           self.mapa[self.personaje_fila][self.personaje_columna]= 1 
           self.mapa[self.personaje_fila][self.personaje_columna - 1]=0
           self.mapa[self.personaje_fila][self.personaje_columna - 2]=2
           self.personaje_columna   -=1 
           print("personaje,caja,espacio")    
          #20 personaje,caja,meta  
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==2 and self.mapa [self.personaje_fila][self.personaje_columna -2]==4): 
          self.mapa[self.personaje_fila][self.personaje_columna]=  2
          self.mapa[self.personaje_fila][self.personaje_columna - 1]=4
          self.mapa[self.personaje_fila][self.personaje_columna - 2]=0
          self.personaje_columna     -=1  
          print("personaje,caja,meta")
          #21 personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6 and self.mapa [self.personaje_fila][self.personaje_columna -2]==1):
          self.mapa[self.personaje_fila][self.personaje_columna]= 6
          self.mapa[self.personaje_fila][self.personaje_columna - 1]=1
          self.mapa[self.personaje_fila][self.personaje_columna -2]=0
          self.personaje_columna     -=1    
          print("personaje,caja_meta,espacio")  
          #22 personaje,caja_meta,meta  
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6  and self.mapa [self.personaje_fila][self.personaje_columna -2]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1   
          self.mapa[self.personaje_fila][self.personaje_columna -1]=5
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=6
          self.personaje_columna     -=1 
          print("personaje,caja_meta,meta")    
          #23  personaje_meta,espacio 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1    
            print("personaje,caja_meta,meta")
             
          #24 personaje_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
            print("personaje_meta,meta") 
         #25 personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]==2  and self.mapa [self.personaje_fila][self.personaje_columna -2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2   
          self.mapa[self.personaje_fila][self.personaje_columna -1]=1
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=5
          self.personaje_columna     -=1 
          print("personaje_meta,caja,espacio") 
        #26 personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5  and self.mapa[self.personaje_fila][self.personaje_columna -1]==2  and self.mapa [self.personaje_fila][self.personaje_columna -2]==1):
             self.mapa[self.personaje_fila][self.personaje_columna]= 2 
             self.mapa[self.personaje_fila][self.personaje_columna -1]=4
             self.mapa[self.personaje_fila][self.personaje_columna -2]=5
             print("personaje_meta,caja,meta")
      #27 personaje_meta,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6  and self.mapa [self.personaje_fila][self.personaje_columna -2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna -1]=1
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=5
          self.personaje_columna     -=1 
          print("personaje_meta,caja,espacio")
    #28personaje_meta,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6  and self.mapa [self.personaje_fila][self.personaje_columna -2]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna -1]=4
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=5
          self.personaje_columna     -=1      
    def moverArriba(self):     
        print("Mover arriba")
     #29 espacio ,personaje
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1 ][self.personaje_columna ]== 0):
            self.mapa[self.personaje_fila][self.personaje_columna]= 0
            self.mapa[self.personaje_fila - 1 ][self.personaje_columna]= 1
            self.personaje_fila -= 1
            print("espacio ,personaje")
    #30 meta,personaje
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1 ][self.personaje_columna ]== 0):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila - 1 ][self.personaje_columna]= 0
            self.personaje_fila -= 1
            print("meta,personaje") 
     #31 espacio,caja,personaje    
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 0):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=1
          self.personaje_fila     -=1 
          print("espacio,caja,personaje") 
     #32 meta,caja,personaje     
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 0):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("meta,caja,personaje")
     #33 espacio,caja_meta,personaje       
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 0):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=1
          self.personaje_fila     -=1 
          print("espacio,caja_meta,personaje")   
     #34 meta,caja_meta,personaje
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 0):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("meta,caja_meta,personaje")        
    #35  espacio,personaje_meta
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1 ][self.personaje_columna ]== 5):
            self.mapa[self.personaje_fila][self.personaje_columna]= 5
            self.mapa[self.personaje_fila - 1 ][self.personaje_columna]= 1
            self.personaje_fila -= 1
            print("espacio,personaje_meta")   
    #36 meta,personaje_meta
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1 ][self.personaje_columna ]== 5):
            self.mapa[self.personaje_fila][self.personaje_columna]= 5
            self.mapa[self.personaje_fila - 1 ][self.personaje_columna]= 4
            self.personaje_fila -= 1
            print("meta,personaje_meta")    
    #37 espacio,caja,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=1
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=5
          self.personaje_fila     -=1 
          print("espacio,caja,personaje_meta")    
    #38 meta,caja,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=5
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("meta,caja,personaje_meta")   
    #39 espacio ,caja_meta,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=5
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=1
          self.personaje_fila     -=1 
          print("espacio ,caja_meta,personaje_meta")  
    #40 meta,caja_meta,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -1][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=5
          self.mapa[self.personaje_fila -1 ][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("meta,caja_meta,personaje_meta")    
    def moverAbajo(self):
        print("Mover abajo")
        #41 personaje,espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1 ][self.personaje_columna ]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1 ][self.personaje_columna]= 0
            self.personaje_fila += 1
            print("personaje,espacio") 
      #42 personaje,meta
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1 ][self.personaje_columna ]== 4):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila + 1 ][self.personaje_columna]= 0
            self.personaje_fila += 1
            print("personaje,espacio")  
      #43 personaje,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=1
          self.personaje_fila     +=1 
          print("personaje,caja,espacio")   
       #44 personaje,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=4
          self.personaje_fila     +=1 
          print("personaje,caja,meta") 
       #45 personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=1
          self.personaje_fila     +=1 
          print("personaje,caja_meta,espacio")  
        #46 personaje,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=0
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=4
          self.personaje_fila     +=1 
          print("personaje,caja_meta,meta")   
        #47  personaje_meta,espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1 ][self.personaje_columna ]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1 ][self.personaje_columna]= 5
            self.personaje_fila += 1
            print("personaje_meta,espacio")   
        #48 personaje_meta,meta
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1 ][self.personaje_columna ]== 4):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila + 1 ][self.personaje_columna]= 5
            self.personaje_fila += 1
            print("personaje_meta,meta")  
        #49 personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=1
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=5
          self.personaje_fila     +=1 
          print("personaje_meta,caja,espacio")   
        #50 personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila][self.personaje_columna ]=4
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=5
          self.personaje_fila     +=1 
          print("personaje_meta,caja,meta")   
        #51 personaje_meta,caja_meta,espacio    
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=1
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=5
          self.personaje_fila     +=1 
          print("personaje_meta,caja_meta,espacio")    
          #52 personaje_meta,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila +1][self.personaje_columna]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila][self.personaje_columna ]=4
          self.mapa[self.personaje_fila +1 ][self.personaje_columna]=5
          self.personaje_fila     +=1 
          print("personaje_meta,caja_meta,meta")  
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

          
            
   
         
