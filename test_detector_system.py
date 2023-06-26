import time 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from tkinter import *
import tkinter.messagebox 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
   
      
class analysis_text(): 
      
    
    def center(self, toplevel): 
        toplevel.update_idletasks() 
        w = toplevel.winfo_screenwidth() 
        h = toplevel.winfo_screenheight() 
        size = tuple(int(_) for _ in 
                     toplevel.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y))) 
   
    def callback(self): 
        if tkinter.messagebox.askokcancel("Quit", 
                                          "Do you want to leave?"): 
            self.main.destroy() 
   
    def setResult(self, type, res): 
        
        if (type == "neg"): 
            self.negativeLabel.configure(text = 
                                         "you typed negative comment : "
                                         + str(res) + " % \n")  
        elif (type == "neu"): 
            self.neutralLabel.configure( text = 
                                        "you typed  comment : "
                                        + str(res) + " % \n") 
        elif (type == "pos"): 
            self.positiveLabel.configure(text  
                                        = "you typed positive comment: "
                                         + str(res) + " % \n") 
          
   
    def runAnalysis(self): 
        sentences = [] 
        sentences.append(self.line.get()) 
        sid = SentimentIntensityAnalyzer() 
        for sentence in sentences: 
                  ss = sid.polarity_scores(sentence) 
                if ss['compound'] >= 0.05 :  
                self.normalLabel.configure(text = 
                                           " you typed postive statement: ")  
       elif ss['compound'] <= - 0.05 :  
                self.normalLabel.configure(text = 
                                           " you typed negative statement")  
       else :  
             self.normalLabel.configure(text = 
                                        " you normal typed  statement: ")  
            for k in sorted(ss): 
                self.setResult(k, ss[k]) 
        print() 
          
   
    def editedText(self, event): 
        self.typedText.configure(text = self.line.get() + event.char) 
          
   
    def runByEnter(self, event): 
        self.runAnalysis() 
   
  
    def __init__(self): 
      self.main = Tk() 
        self.main.title("Text Detector system") 
        self.main.geometry("600x600") 
        self.main.resizable(width=FALSE, height=FALSE) 
        self.main.protocol("WM_DELETE_WINDOW", self.callback) 
        self.main.focus() 
        self.center(self.main) 
 
        self.label1 = Label(text = "type a text here :") 
        self.label1.pack() 
 
        self.line = Entry(self.main, width=70) 
        self.line.pack() 
 self.textLabel = Label(text = "\n", 
                               font=("Helvetica", 15)) 
        self.textLabel.pack() 
        self.typedText = Label(text = "",  
                               fg = "blue",  
                               font=("Helvetica", 20)) 
        self.typedText.pack() 
 self.line.bind("<Key>",self.editedText) 
        self.line.bind("<Return>",self.runByEnter) 
   
 self.result = Label(text = "\n",  
                            font=("Helvetica", 15)) 
        self.result.pack() 
        self.negativeLabel = Label(text = "",  
                                   fg = "red", 
                                   font=("Helvetica", 20)) 
        self.negativeLabel.pack() 
        self.neutralLabel  = Label(text = "", 
                                   font=("Helvetica", 20)) 
        self.neutralLabel.pack() 
        self.positiveLabel = Label(text = "", 
                                   fg = "green", 
                                   font=("Helvetica", 20)) 
        self.positiveLabel.pack() 
        self.normalLabel =Label (text ="", 
                                 fg ="red", 
                                 font=("Helvetica", 20)) 
        self.normalLabel.pack() 
          
myanalysis = analysis_text() 
mainloop()
