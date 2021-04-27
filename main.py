import os
import urllib.request
from tkinter import *
from string import ascii_uppercase
from PIL import ImageTk, Image
from random import randint
from tkinter import messagebox

# You could use your web browser to download the file
# But I prefer this solution

DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/dwyl/english-words/master/'
WORDS_PATH = os.path.join('datasets','words')
WORDS_URL = DOWNLOAD_ROOT + 'words_alpha.txt'


def fetch_words_data(words_path=WORDS_PATH,words_url=WORDS_URL):
    ''' Download the Data '''
    os.makedirs(words_path,exist_ok=True)
    words_alpha = os.path.join(words_path,'words_alpha.txt')
    urllib.request.urlretrieve(words_url,words_alpha)
    f = open(words_alpha,'r+')
    dataset = f.read()
    dataset = dataset.splitlines() 
    f.close()
    
    return dataset

df = fetch_words_data() 

class Hangman:
    
    paths = ["images/hang0.png","images/hang1.png","images/hang2.png","images/hang3.png",
            "images/hang4.png","images/hang5.png","images/hang6.png","images/hang7.png",
            "images/hang8.png","images/hang9.png","images/hang10.png","images/hang11.png"]
    
    the_word_withSpace=" "
    numberOfGuesses = 0

    def __init__(self,master):
        self.count = 0
        self.structure(master)
        self.aa = master
    def structure(self,master):

        """ Instruction Label """
        # Create a Hangman's Background
        self.img = ImageTk.PhotoImage(Image.open(self.paths[0]))
        self.imgLabel = Label(master)
        self.imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady= 40)
        self.imgLabel.config(image = self.img)
        
        # Creating label to display current Guessed Status of Word
        self.lblWord = StringVar()
        Label(master,textvariable=self.lblWord,font=("Consolas 24 bold")).grid(row=0,column=3,columnspan=6,padx=10)

        # Create list box for History of wrong answer
        self.lbl = Listbox(master)
        self.lbl.grid(row=0,column=9)
        
        # Create label for count life
        self.lbl2 = Label(master,text=f'{self.numberOfGuesses} / 10 ')
        self.lbl2.grid(row=0,column=0)

        # Alphabet buttons
        n = 0
        for c in ascii_uppercase:
            Button(master,text=c,command=lambda c=c:self.guess(c),font=("Helvetica 18"),width=4).grid(row=1+n // 9,column=n % 9)
            n += 1
        
        # Creating a newGame button
        Button(master,text='New\nGame',command=lambda:self.newGame(),font=("Helvetica 10 bold")).grid(row=3,column=8,sticky='NSWE')

        self.newGame()

    def newGame(self):

        ''' Create new game '''

        # Initialize number of guess 
        self.numberOfGuesses = 0
        
        # Change Hangman's display image
        self.img = ImageTk.PhotoImage(Image.open(self.paths[0]))
        self.imgLabel.config(image = self.img)

        # Change life count text
        self.lbl2.config(text=f'{self.numberOfGuesses}/10')

        # Generate one random word
        the_word = df[randint(0,len(df)-1)] 
        
        # Created for cheating :)
        print(the_word)

        # Change the values 
        self.the_word_withSpace=" ".join(the_word.upper())
        self.lblWord.set(" ".join("_"*len(the_word)))

        
        
    
    def guess(self,letter):
    
        # Check number of Guess value
        if self.numberOfGuesses < 11:
            
            # The random word is 'EQUITY' it's going to be 
            # ['E', ' ', 'Q', ' ', 'U', ' ', 'I', ' ', 'T',' ' , 'Y'] like this
            txt = list(self.the_word_withSpace)
            
            # For example, you guess the two of words  it's going to be 
            # ['E', ' ', 'Q', ' ', '_', ' ', '_', ' ', '_', ' ', '_'] like this
            self.guessed = list(self.lblWord.get())

            if self.the_word_withSpace.count(letter)>0:
                for c in range(len(txt)):
                    # Checked the guessed word is in the txt
                    if txt[c]==letter:
                        self.guessed[c]=letter
                    self.lblWord.set("".join(self.guessed))

                #Condition of Player Won
                if self.lblWord.get()==self.the_word_withSpace:
                    messagebox.showinfo('Hangman','You guessed it!')
            else:
                self.numberOfGuesses +=1

                # Add letter in list box
                self.lbl.insert(self.numberOfGuesses,letter)
                self.lbl2.config(text=f'{self.numberOfGuesses-1}/10')

                self.img = ImageTk.PhotoImage(Image.open(self.paths[self.numberOfGuesses]))
                self.imgLabel.config(image = self.img)

                # Condition Of player Loose
                if self.numberOfGuesses ==11:
                    messagebox.showinfo('Hangman','Game Over')

root = Tk()
root.title("Hangman Game")
root.geometry("750x480")
app = Hangman(root)
root.mainloop()