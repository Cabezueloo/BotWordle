'''
'''
import time

BAD = 'b'
GOOD = 'g'
REGULAR = 'r'
NO_EXIST = "."

class Controller:
    
    def createList(self) -> list:
        
        
        f = open('dictionary_spanish.txt', 'r')

        listaWords = f.read().lower().split("\n")
        self.supposedWord = ""

        f.close()
        return listaWords
    
    def __init__(self):
        self.listWords = self.createList()
        
           
    def loop(self):
        
        wordAttemp = input("Word -> ").lower()
        blockCode : str = input("G/R/B -> ").lower()
        
        while True:

            t = time.time()

            listLetterInBadPosition = []
            dictLetterInBadPosition = dict()
            letterInGoodPosition = dict()
            listLetterInGoodPosition = []
            letterInRegularPosition = dict()
            
            regularLetterList = []
            
            for index, char in enumerate(wordAttemp):
                if ( blockCode[index].__eq__(BAD)):
                    listLetterInBadPosition.append(char)
                    dictLetterInBadPosition[index] = char
                elif ( blockCode[index].__eq__(GOOD)):
                    letterInGoodPosition[index] = char
                    listLetterInGoodPosition.append(char)
                elif ( blockCode[index].__eq__(REGULAR)):
                    letterInRegularPosition[index] = char
                    regularLetterList.append(char)

            lenOriginal = len(self.listWords)
            originalList = self.listWords.copy()


            #For in all the words dicitonaray
            for index, word in enumerate(originalList):
                deleted = False
                

                for indexLetter, letter in enumerate(word):

                    #GOOD
                    if ( letterInGoodPosition.__contains__(indexLetter)):
                        if (letterInGoodPosition.get(indexLetter) != letter):
                            deleted= True
                            break
                        
                
                    #Regular
                    elif ( letterInRegularPosition.__contains__(indexLetter)):
                        if(letterInRegularPosition.get(indexLetter) == letter):
                            deleted = True
                            break
                    
                    #TODO Mejorar doble caracter bad, KEY OPERA -> LLAVE, ACEDA, ABAJA
                    if (letter in listLetterInBadPosition):
                            if(letter in listLetterInGoodPosition):
                               if (word.count(letter)  >   listLetterInGoodPosition.count(letter)):
                                deleted = True
                                break
                            else:
                                deleted  = True
                                break
                                

                        
                    
                for rword in regularLetterList:
                    if not rword in word:
                        deleted = True
                        break


                
                if deleted:
                    self.listWords.remove(word)

            print(f"Tiempo en recorrer y comprobar todo el diccionario -> {time.time() - t }")
            print(f"Tamagno antes de iterar -> {lenOriginal}" )
            print(f"Tamagno despues de iterar -> {len(self.listWords)}" )
            print(f"Existe todos -> {(self.listWords.__contains__("todos"))}" )
            #check : str= input("Check:")

            #if (check != ""):
             #   print(self.listWords.__contains__(check))
            
            if(self.listWords.__contains__(wordAttemp)):
                self.listWords.remove(wordAttemp)
            
            wordAttemp = self.listWords[0]


            print(f"Try -> {wordAttemp}")


            blockCode : str = input("G/R/B -> ").lower()
        
            


controller = Controller()

controller.loop()

    