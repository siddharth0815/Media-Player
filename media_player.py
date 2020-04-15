from tkinter import *
from tkinter.filedialog import askdirectory
import os
import pygame
#from pygame import games
from mutagen.id3 import ID3
from PIL import ImageTk,Image
index= 0
listofsongs=[]
realnames=[]




class Media:
    
    def __init__(s):
        
        try:
            s.root.destroy()
        except:
            pass

       # s.v = StringVar()
        s.root= Tk()
        s.root.geometry('1450x700+0+0')#'widthxheight+x+y'
        s.root.config(bg='Khaki1')
        s.root.minsize(300,300)
       #background_image=PhotoImage(file=r'C:\Users\Divya Asrani\Desktop\hh.jpg')
        #background_label=Label(s.root,image=background_image)
        
        #background_label.place(x=0,y=0,relwidth=1,relheight=1)
        
        l1=Label(s.root,text='Music Player',bg='orange')
        l1.pack(side='top',fill='x')
        listbox=Listbox(s.root)
        listbox.place(x=500,y=200)
        previous=Button(s.root, text='previous song',bg='cyan',fg='red',command=s.previoussong,cursor='man')
        pause=Button(s.root, text='pause',bg='cyan',fg='orange',command=s.stopsong,cursor='man')
        play=Button(s.root, text='play',bg='cyan',fg='orange',command=s.playsong,cursor='man')
        nxt=Button(s.root, text='next song',bg='cyan',fg='orange',command=s.nextsong,cursor='man')
        previous.place(x=500,y=600)
        pause.place(x=595,y=600)
        nxt.place(x=640,y=600)
        play.place(x=720,y=600)
        s.directorychooser()
        realnames.reverse()
        for items in realnames:
            
            listbox.insert(0,items)
            
        realnames.reverse()
        s.cursong=Label(s.root,width='35',text=realnames[0],bg='yellow')
        s.cursong.place(x=200,y=400)
        



    def nextsong(s):
            
            global index
            index+=1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            s.updatelabel()

    def stopsong(s):
            pygame.mixer.music.stop()

    def previoussong(s):
            global index
            index-=1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            s.updatelabel()
    
    def directorychooser(s):
            s.directory=askdirectory()
            os.chdir(s.directory)
            for files in os.listdir(s.directory):
                
                
                        if(files.endswith(".mp3")):
                            
                            realdir=os.path.realpath(files)
                            audio=ID3(realdir)
                            realnames.append(audio['TIT2'].text[0])
                            listofsongs.append(files)
                        pygame.mixer.init()
                        pygame.mixer.music.load(listofsongs[0])

                        pygame.mixer.music.play()

    def playsong(s):
        pygame.mixer.music.play()
   

    def updatelabel(s):
        global index
        s.cursong.config(text=realnames[index])
        
        
         
          


    






