'''
'''
import time


from colorama import Fore, Back, Style


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
       pass
    
    def newGame(self):
        self.listWords = self.createList()
        self.loop()

    def loop(self):
        
        wordAttemp = input("Firs Word -> ").lower()
        blockCode : str = input(f"{Fore.GREEN}G{Style.RESET_ALL}/{Fore.YELLOW}R{Style.RESET_ALL}/{Fore.RED}B {Style.RESET_ALL}-> ").lower()
        
        while True:

            t = time.time()

            listBadLetter = []
            letterInGoodPosition = dict()
            listGoodLetter = []
            letterInRegularPosition = dict()
            
            
            listReguarLetter = []
            
            for index, char in enumerate(wordAttemp):
                if ( blockCode[index].__eq__(BAD)):
                    listBadLetter.append(char)
                    
                elif ( blockCode[index].__eq__(GOOD)):
                    letterInGoodPosition[index] = char
                    listGoodLetter.append(char)
                elif ( blockCode[index].__eq__(REGULAR)):
                    letterInRegularPosition[index] = char
                    listReguarLetter.append(char)

            lenOriginal = len(self.listWords)
            originalList = self.listWords.copy()


            #For all the words in dicitonaray
            for index, word in enumerate(originalList):
                deleted = False
                

                for indexLetter, letter in enumerate(word):

                    #GOOD
                    if ( letterInGoodPosition.__contains__(indexLetter) and letterInGoodPosition.get(indexLetter) != letter):
                        deleted= True
                        break
                
                    #Regular
                    elif ( letterInRegularPosition.__contains__(indexLetter) and letterInRegularPosition.get(indexLetter) == letter):
                            deleted = True
                            break
                    
                    #BAD IF letter exist en bad letter
                    if (letter in listBadLetter):
                            #If exist in good letter or regular letter, check if the count of the letter in more than good or regular
                            if(letter in listGoodLetter or letter in listReguarLetter):
                               if (word.count(letter)  >   (listGoodLetter.count(letter) or  listReguarLetter.count(letter))):
                                deleted = True
                                break
                            #Else, means that the letter doens't exist in the good or regular list
                            else:
                                deleted  = True
                                break
                               
                # To check if the any regular letter that must apper, doesn't in the word. In this case delete
                for rword in listReguarLetter:
                    if not rword in word:
                        deleted = True
                        break

                if deleted:
                    self.listWords.remove(word)

            print(f"Tiempo en recorrer y comprobar todo el diccionario -> {time.time() - t }")
            print(f"Tamagno antes de iterar -> {lenOriginal}" )
            print(f"Tamagno despues de iterar -> {len(self.listWords)}" )
            
            
            
            if(self.listWords.__contains__(wordAttemp)):
                self.listWords.remove(wordAttemp)
            
            wordAttemp = self.listWords[0]


            print(f"Try -> {wordAttemp}")
            

            blockCode : str = input(f"{Fore.GREEN}G{Style.RESET_ALL}/{Fore.YELLOW}R{Style.RESET_ALL}/{Fore.RED}B {Style.RESET_ALL}-> ").lower()
            if blockCode.__eq__("exit"):
                self.newGame()
            
        
            


controller = Controller()

controller.newGame()

    