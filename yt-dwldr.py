import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
from pytubefix import *

root = tk.Tk() # Cria a raiz da janela
root.geometry('600x400') # Define o dimensionamento da janela
root.title('Youtube Video Downloader') # Título da janela

frame = ttk.Frame(root,width=100,height=300) # Cria um frame onde fica ambas as variaveis input_entry e label
frame.pack(pady=45)

label = ttk.Label(frame, text='Paste URL:') 
label.pack(side='left')

input_entry = ttk.Entry(frame, width=40)
input_entry.pack(side='left')

class defS: # Classe criada para armazenar as funções

    @classmethod
    def askDir(cls): # Função para a escolha de diretório
        cls.path = askdirectory(title='Select Folder',mustexist=True) # Abre uma janela para escolher a pasta onde o arquivo será posto
        frame3 = ttk.Frame(root,width=100,height=100)
        frame3.pack()
        dir_label = ttk.Label(frame3,text=f'Selected Folder 📂: {cls.path}',background='black',foreground='white')
        dir_label.pack(side='bottom')

    @classmethod
    def download(cls): # Função onde se pega o url do video e o baixa
        url1 = input_entry.get() # Coleta o url do video da variavel input_entry
        yt = YouTube(url1)
        print(yt.title)
        stream = yt.streams.get_highest_resolution() # Pega a maior resolução do video escolhido
        stream.download(output_path=cls.path) # Baixa o video para o diretorio escolhido na outra função
        print(url1)
        alert = tkinter.messagebox.showinfo('Download Complete!',f'The video "{yt.title}" has been downloaded successfully to the directory "{cls.path}"') # Alerta de que tudo ocorreu corretamente

frame2 = ttk.Frame(root,width=100,height=100) # Frame criado para armazenar os dois botões
frame2.pack()
but_dir = ttk.Button(frame2,text='Select Folder 📁', width=45,command=defS.askDir) # Botão de seleção de diretório que executa a função askDir
but_dir.pack(side='bottom',pady=15)

submit_button = ttk.Button(root, text='Download', width=25,command=defS.download) # Botão de download que executa a função download
submit_button.pack(side='bottom',pady=10)

root.mainloop() # Mantém a janela aberta em loop