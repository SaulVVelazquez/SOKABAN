from os import system, name
from time import sleep
class Sokoban:
    """
    0_personaje
    1_espacio
    2_caja
    3_pared
    4_metas
    5-personaje_meta
    6_caja_meta
    """
  
    mapa=[]
    personaje_fila= 1
    personaje_columna= 1
    
    def leerMapa(self,lvl):
        if lvl == 1:
          self.nivel=open("nivel 1.SV", "r")
        else:
          self.nivel=open("nivel 2.SV", "r")
        self.mapa = []
        for  row in self.nivel:
            linea = []
            for digito in row:
                if digito == "\n":
                    continue
                linea.append(int(digito))
            self.mapa.append(linea)

    def imprimirMapa(self):
        fin = False
        for fila in self.mapa:
            for  i in fila:
                if i==0:
                    print("🙂", end="")
                elif i==1:
                    print("  ",end="")
                elif i==2:
                    print("🎁",end="")
                elif i==3:
                    print("🖼",end=" ")
                elif i==4:
                    print("🎈",end="")
                elif i==5:
                    print("😎",end="")
                elif i==6:
                    print("🎡",end="")
                    fin = True
                elif i==7:
                    print("💰",end="")
                elif i==8:
                    print("😱",end="")
                    fin = True
            print()    
        return fin
    def borrarS(self): #borra pantalla
        if name == 'nt':
            system("cls")
        else:
            system("clear")

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
    # 6.2 personaje, meta 2
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 7):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.personaje_columna += 1
            print("personaje,meta2")

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
          self.mapa [self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna + 1] =5
          self.mapa[self.personaje_fila][self.personaje_columna + 2] =2
          self.personaje_columna += 1  
          print("personaje,caja_meta,espacio")  
    #10 personaje,caja_meta,meta 
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna +1]==6  and self.mapa [self.personaje_fila][self.personaje_columna +2]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=1   
          self.mapa[self.personaje_fila][self.personaje_columna +1]=5
          self.mapa[self.personaje_fila][self.personaje_columna +2]=6
          self.personaje_columna     +=1 
          print("personaje,caja_meta,meta")  
    #11   personaje_meta,espacio 5,1->
        elif (self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna + 1]==1):
            self.mapa[self.personaje_fila][self.personaje_columna]=4
            self.mapa[self.personaje_fila][self.personaje_columna + 1]=0
            self.personaje_columna += 1
            print("personaje_meta,espacio")
          
    #12 personaje_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna + 1]==4):
            self.mapa[self.personaje_fila][self.personaje_columna]=4
            self.mapa[self.personaje_fila][self.personaje_columna + 1]=5
            self.personaje_columna += 1
            print("personaje_meta,meta")
            #13 personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==2  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna ]=4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=0
          self.mapa[self.personaje_fila][self.personaje_columna +2]=2
          self.personaje_columna     +=1  
          print("personaje_meta,caja,espacio")  
        #14 personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==2  and self.mapa [self.personaje_fila][self.personaje_columna +2]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=0
          self.mapa[self.personaje_fila][self.personaje_columna +2]=6
          self.personaje_columna     +=1  
          print("personaje_meta,caja_meta") 
          #15personaje_meta,caja_meta,espacio  
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==6  and self.mapa [self.personaje_fila][self.personaje_columna+ 2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=5
          self.mapa[self.personaje_fila][self.personaje_columna +2]=2
          self.personaje_columna     +=1  
          print("personaje_meta,caja_meta,espacio ")   
          #16 personaje_meta,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna +1]==6  and self.mapa [self.personaje_fila][self.personaje_columna +2]== 4):
          self.mapa [self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila][self.personaje_columna +1]=5
          self.mapa[self.personaje_fila][self.personaje_columna +2]=6
          self.personaje_columna     +=1     
          print("personaje_meta,caja_meta,meta")   
          
      
            
    def moverIzquierda(self):
        print("Mover izquierda")
    #17 personaje, espacio 
        if (self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila][self.personaje_columna - 1]==1):
            self.mapa[self.personaje_fila][self.personaje_columna]=1
            self.mapa[self.personaje_fila][self.personaje_columna - 1]=0
            self.personaje_columna -= 1
            print("personaje,espacio")    
        #18 personaje,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1]==4):
            self.mapa[self.personaje_fila][self.personaje_columna]=1
            self.mapa[self.personaje_fila][self.personaje_columna - 1]=5
            self.personaje_columna -= 1
            print("personaje,meta")   
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1]==7):
            self.mapa[self.personaje_fila][self.personaje_columna]=1
            self.mapa[self.personaje_fila][self.personaje_columna - 1]=8
            self.personaje_columna -= 1
            print("personaje,meta")   
        #19 personaje,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==2 and self.mapa [self.personaje_fila][self.personaje_columna -2]==1): 
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna - 1]=0
          self.mapa[self.personaje_fila][self.personaje_columna - 2]=2
          self.personaje_columna     -=1 
          print("personaje,caja,espacio")    
          #20 personaje,caja,meta  
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==2 and self.mapa [self.personaje_fila][self.personaje_columna -2]==4):
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna - 1]=0
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=6
          self.personaje_columna     -=1  
          print("personaje,caja,meta")
          #21 personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6 and self.mapa [self.personaje_fila][self.personaje_columna -2]==1):
          self.mapa[self.personaje_fila][self.personaje_columna]=1
          self.mapa[self.personaje_fila][self.personaje_columna - 1]=5
          self.mapa[self.personaje_fila][self.personaje_columna -2]=2
          self.personaje_columna     -=1    
          print("personaje,caja_meta,espacio")  
          #22 personaje,caja_meta,meta  
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6  and self.mapa [self.personaje_fila][self.personaje_columna -2]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=1   
          self.mapa[self.personaje_fila][self.personaje_columna -1]=5
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=6
          self.personaje_columna     -=1 
          print("personaje,caja_meta,meta")    
          #23  personaje_meta,espacio 
        elif (self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila][self.personaje_columna - 1]==1):
            self.mapa[self.personaje_fila][self.personaje_columna]=4
            self.mapa[self.personaje_fila][self.personaje_columna - 1]=0
            self.personaje_columna -= 1    
            print("personaje_meta,espacio")
             
          #24 personaje_meta,meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna]=4
            self.mapa[self.personaje_fila][self.personaje_columna - 1]=5
            self.personaje_columna -= 1
            print("personaje_meta,meta") 
         #25 personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]==2  and self.mapa [self.personaje_fila][self.personaje_columna -2]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=4  
          self.mapa[self.personaje_fila][self.personaje_columna -1]=0
          self.mapa[self.personaje_fila][self.personaje_columna -2]=2
          self.personaje_columna     -=1 
          print("personaje_meta,caja,espacio") 
        #26 personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5  and self.mapa[self.personaje_fila][self.personaje_columna -1]==2  and self.mapa [self.personaje_fila][self.personaje_columna -2]==4):
             self.mapa[self.personaje_fila][self.personaje_columna]= 4 
             self.mapa[self.personaje_fila][self.personaje_columna -1]=0
             self.mapa[self.personaje_fila][self.personaje_columna -2]=6
             print("personaje_meta,caja,meta")
      #27 personaje_meta,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6  and self.mapa [self.personaje_fila][self.personaje_columna -2]==1):
          self.mapa [self.personaje_fila][self.personaje_columna]=4  
          self.mapa[self.personaje_fila][self.personaje_columna -1]=5
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=2
          self.personaje_columna     -=1 
          print("personaje_meta,caja,espacio")
    	#28 Personaje_meta, caja_meta, meta.
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila][self.personaje_columna -1]==6  and self.mapa [self.personaje_fila][self.personaje_columna -2]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  4  
          self.mapa[self.personaje_fila][self.personaje_columna -1]=5
          self.mapa[self.personaje_fila][self.personaje_columna -2 ]=6
          self.personaje_columna     -=1  
          print("Personaje_meta, caja_meta, meta")

    def moverArriba(self):     
        print("Mover arriba")
     #29 espacio ,personaje
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila -1][self.personaje_columna]=0
            self.personaje_fila -= 1
            print("espacio ,personaje")
    #30 meta,personaje
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 4):
            self.mapa[self.personaje_fila -1][self.personaje_columna]= 1
            self.mapa[self.personaje_fila][self.personaje_columna]= 5
            self.personaje_fila -= 1
            print("meta,personaje") 
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 7):
            self.mapa[self.personaje_fila -1][self.personaje_columna]= 1
            self.mapa[self.personaje_fila][self.personaje_columna]= 8
            self.personaje_fila -= 1
            print("meta,personaje") 
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 9):
            self.mapa[self.personaje_fila -1][self.personaje_columna]= 1
            self.mapa[self.personaje_fila][self.personaje_columna]= 7
            self.personaje_fila -= 1
            print("meta,personaje") 
     #31 espacio,caja,personaje    
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -2][self.personaje_columna]==1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1  
          self.mapa[self.personaje_fila -1][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -2 ][self.personaje_columna]=2
          self.personaje_fila     -=1 
          print("espacio,caja,personaje") 
     #32 meta,caja,personaje     
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -2][self.personaje_columna]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1  
          self.mapa[self.personaje_fila -1][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -2 ][self.personaje_columna]=6
          self.personaje_fila     -=1 
          print("meta,caja,personaje")
     #33 espacio,caja_meta,personaje       
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -2][self.personaje_columna]==1):
          self.mapa [self.personaje_fila][self.personaje_columna]=1 
          self.mapa[self.personaje_fila -1][self.personaje_columna ]=5
          self.mapa[self.personaje_fila -2][self.personaje_columna]=2
          self.personaje_fila     -=1 
          print("espacio,caja_meta,personaje")   
     #34 meta,caja_meta,personaje
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -2][self.personaje_columna]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=1  
          self.mapa[self.personaje_fila -1][self.personaje_columna]=5
          self.mapa[self.personaje_fila -2][self.personaje_columna]=6
          self.personaje_fila     -=1 
          print("meta,caja_meta,personaje")        
    #35  espacio,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 5):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila -1][self.personaje_columna]= 0
            self.personaje_fila -= 1
            print("espacio,personaje_meta")   
    #36 meta,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna ]== 5):
            self.mapa[self.personaje_fila][self.personaje_columna]=5
            self.mapa[self.personaje_fila - 1 ][self.personaje_columna]=4
            self.personaje_fila -= 1
            print("meta,personaje_meta")    
    #37 espacio,caja,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -2][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=  2  
          self.mapa[self.personaje_fila -1][self.personaje_columna ]=0
          self.mapa[self.personaje_fila -2][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("espacio,caja,personaje_meta")    
    #38 meta,caja,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna]==2  and self.mapa [self.personaje_fila -2][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=  6  
          self.mapa[self.personaje_fila -1][self.personaje_columna]=0
          self.mapa[self.personaje_fila -2][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("meta,caja,personaje_meta")   
    #39 espacio ,caja_meta,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 1 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -2][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=2  
          self.mapa[self.personaje_fila -1][self.personaje_columna]=5
          self.mapa[self.personaje_fila -2][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("espacio ,caja_meta,personaje_meta")  
    #40 meta,caja_meta,personaje_meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 4 and self.mapa[self.personaje_fila -1][self.personaje_columna]==6  and self.mapa [self.personaje_fila -2][self.personaje_columna]== 5):
          self.mapa [self.personaje_fila][self.personaje_columna]=6  
          self.mapa[self.personaje_fila -1][self.personaje_columna]=5
          self.mapa[self.personaje_fila -2][self.personaje_columna]=4
          self.personaje_fila     -=1 
          print("meta,caja_meta,personaje_meta")    
    def moverAbajo(self):
        print("Mover abajo")
        #41 personaje,espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna ]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila +1][self.personaje_columna]= 0
            self.personaje_fila += 1
            print("personaje,espacio") 
      #42 personaje,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna ]== 4):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila +1][self.personaje_columna]= 5
            self.personaje_fila += 1
            print("personaje,meta")  
      #42 personaje,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna ]== 7):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila +1][self.personaje_columna]= 8
            self.personaje_fila += 1
            print("personaje,meta")  
      #43 personaje,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +2][self.personaje_columna]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1  
          self.mapa[self.personaje_fila +1][self.personaje_columna ]=0
          self.mapa[self.personaje_fila +2 ][self.personaje_columna]=5
          self.personaje_fila     +=1 
          print("personaje,caja,espacio")   
       #44 personaje,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +2][self.personaje_columna]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=  1  
          self.mapa[self.personaje_fila +1][self.personaje_columna ]=0
          self.mapa[self.personaje_fila +2][self.personaje_columna]=6
          self.personaje_fila     +=1 
          print("personaje,caja,meta") 
       #45 personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila +2][self.personaje_columna]==1):
          self.mapa [self.personaje_fila][self.personaje_columna]=1 
          self.mapa[self.personaje_fila +1][self.personaje_columna ]=5
          self.mapa[self.personaje_fila +2][self.personaje_columna]=2
          self.personaje_fila     +=1 
          print("personaje,caja_meta,espacio")  
        #46 personaje,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila +2][self.personaje_columna]==4):
          self.mapa [self.personaje_fila +2][self.personaje_columna]=6  
          self.mapa[self.personaje_fila +1][self.personaje_columna ]=5
          self.mapa[self.personaje_fila ][self.personaje_columna]=1
          self.personaje_fila     +=1 
          print("personaje,caja_meta,meta")   
        #47  personaje_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna ]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila + 1 ][self.personaje_columna]= 0
            self.personaje_fila += 1
            print("personaje_meta,espacio")   
        #48 personaje_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]== 4):
            self.mapa[self.personaje_fila][self.personaje_columna]= 4
            self.mapa[self.personaje_fila +1][self.personaje_columna]= 5
            self.personaje_fila += 1
            print("personaje_meta,meta")  
        #49 personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2 and self.mapa [self.personaje_fila +2][self.personaje_columna]== 1):
          self.mapa [self.personaje_fila][self.personaje_columna]=4 
          self.mapa[self.personaje_fila +1][self.personaje_columna]=0
          self.mapa[self.personaje_fila +2][self.personaje_columna]=2
          self.personaje_fila     +=1 
          print("personaje_meta,caja,espacio")   
        #50 personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]== 5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==2  and self.mapa [self.personaje_fila +2][self.personaje_columna]==4):
          self.mapa [self.personaje_fila][self.personaje_columna]=4  
          self.mapa[self.personaje_fila +1][self.personaje_columna]=0
          self.mapa[self.personaje_fila +2][self.personaje_columna]=6
          self.personaje_fila     +=1 
          print("personaje_meta,caja,meta")   
        #51 personaje_meta,caja_meta,espacio    
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila][self.personaje_columna]==1):
          self.mapa [self.personaje_fila][self.personaje_columna]=4  
          self.mapa[self.personaje_fila +1][self.personaje_columna]=5
          self.mapa[self.personaje_fila +2][self.personaje_columna]=2
          self.personaje_fila     +=1 
          print("personaje_meta,caja_meta,espacio")    
          #52 personaje_meta,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna]==5 and self.mapa[self.personaje_fila +1][self.personaje_columna]==6  and self.mapa [self.personaje_fila][self.personaje_columna]==4):
          self.mapa[self.personaje_fila][self.personaje_columna]=4
          self.mapa[self.personaje_fila +1][self.personaje_columna]=5
          self.mapa[self.personaje_fila +2][self.personaje_columna]=6
          self.personaje_fila     +=1 
          print("personaje_meta,caja_meta,meta")  
    def jugar(self):
        instrucciones="a-izquierda\nd-derecha\nw-arriba\ns-abajo"
        print(instrucciones)
        lvl = 1
        while True:
          self.leerMapa(lvl)
          print(f"\nNivel {lvl}")
          self.imprimirMapa()
          while True:
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
              else: 
                pass
              self.borrarS()
              print(f"\nNivel {lvl}")
              fin = self.imprimirMapa()
              if fin:
                print("Has completado el nivel!!!")
                print("SIGUIENTE NIVEL")
                lvl = 2
                # espera 3 segundos para cambiar de nivel
                sleep(3)
                self.borrarS()
                break
              

                
juego = Sokoban()
juego.jugar()
            
        
            
          
          
            
   
         
