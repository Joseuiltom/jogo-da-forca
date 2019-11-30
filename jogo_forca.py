#importa a função para escolher uma das palavras
from random import choice
#importa o modulo tkinter
from tkinter import *
#importa o partial
from functools import partial
#escolhe qual dos temas vai ser sorteado
temas = ['animais','comidas',]
tema = choice(temas)
#escolhe qual palavra vai ser sorteada
animais = ['soinho','galinha','vaca','gato','girafa']
comidas = ['melancia','peixe','manga','bolacha','feijao']
if tema == 'animais':
    palavra = choice(animais)
elif tema == 'comidas':
    palavra = choice(comidas)
palavra2 = palavra
palavra = list(palavra.upper())
palavra_aux = []
palavra_aux2 = palavra.copy()
for letra in range(len(palavra)):
    palavra_aux.append('_')
existentes = []
errados = []
#cria a lista com nossas letras
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#cria a classe do nosso programa
class jogo_forca(object):
    """
    classe que contém todo o nosso programa.
    e a sua logica
    """
    #inicializa nossos atributos
    def __init__(self,i):
        #atributo para verificar se a palavra ja foi terminada
        self.aux = False
        #cria o frame que contem o texto com o tema do jogo
        self.frame1 = Frame(i)
        self.frame1['bg'] = 'white'
        self.frame1['pady'] = 10
        self.frame1.pack()
        #cria o frame que contém a imagen do jogo da forca
        self.frame2 = Frame(i)
        self.frame2['pady'] = 20
        self.frame2['bg'] = 'white'
        self.frame2.pack()
        #frame com as palavras existentes erradas
        self.frame_letras = Frame(i)
        self.frame_letras['pady'] = 10
        self.frame_letras['bg'] = 'white'
        self.frame_letras.pack()
        #cria o frame do texto com as letras da palavra escolhida
        self.frame3 = Frame(i)
        self.frame3['bg'] = 'white'
        self.frame3.pack()
        #frame dos botões
        self.frame4 = Frame(i)
        self.frame4['bg'] = 'white'
        self.frame4['pady'] = 10
        self.frame4.pack()
        #cria a frame com o resultado das ações do usuário
        self.frame5 = Frame(i)
        self.frame5['bg'] = 'white'
        self.frame5.pack()
        #cria nossos sprites para ser ultilizados no nosso jogo
        self.sprite1 = PhotoImage(file='imagens/imagem_1.ppm')
        self.sprite2 = PhotoImage(file='imagens/imagem_2.ppm')
        self.sprite3 = PhotoImage(file='imagens/imagem_3.ppm')
        self.sprite4 = PhotoImage(file='imagens/imagem_4.ppm')
        self.sprite5 = PhotoImage(file='imagens/imagem_5.ppm')
        self.sprite6 = PhotoImage(file='imagens/imagem_6.ppm')
        self.sprite7 = PhotoImage(file='imagens/imagem_7.ppm')
        #widget do tema do jogo
        self.texto_tema = Label(self.frame1,text=f'Tema:\n{tema} ',fg='green',bg='white',font=('Verdana',20,'bold'))
        self.texto_tema.pack()
        #widget da imagem do jogo da forca
        self.imagem1 = Label(self.frame2)
        self.imagem1['image'] = self.sprite1
        self.imagem1.imagem = self.sprite1
        self.imagem1.pack(side=LEFT)
        #widget das palavras existentes e as erradas
        self.texto_ex = Label(self.frame_letras,text=f'Existentes: {existentes}',bg='white',fg='green',font=('Verdana',15,'bold'))
        self.texto_ex.pack(side=LEFT)
        self.texto_er = Label(self.frame_letras,text=f'Errados: {errados}',bg='white',fg='green',font=('Verdana',15,'bold'))
        self.texto_er.pack(side=LEFT)
        self.mudar_ex()
        self.mudar_er()
        #widget do texto da palavra escolhida
        letras = ''
        for letra in palavra_aux:
            letras +=  letra + ' '
        self.texto1 = Label(self.frame3,text=letras,fg='green',bg='white',font=('Verdana',25,'bold'))
        self.texto1.pack()
        #cria os nossos botões
        self.cont = 0
        for i in range(len(alfabeto)):
            if i % 5 == 0:
                subframe = Frame(self.frame4)
                subframe['padx'] = 5
                subframe['bg'] = 'white'
                subframe.pack()
            a = Button(subframe,text=alfabeto[i],fg='green',width=10,command=partial(self.inserir,alfabeto[i]))
            a.pack(side=LEFT)
        #cria o widget do texto do resultado das ações do usuário
        self.texto2 = Label(self.frame5,text='',bg='white',fg='green',font=('Verdana',25,'bold'))
        self.texto2.pack()
    #cria o metodo para inserir a palavra digitada
    def inserir(self,letra):
        if self.cont >= 6 or letra in existentes or '_' not in palavra_aux:
             return
        if letra in palavra:
            for caractere in range(0,len(palavra)):
                if letra == palavra[caractere]:
                    palavra_aux[caractere] = letra
            self.mudar()
            existentes.append(letra)
            self.mudar_ex()
            if '_' not in palavra_aux:
                self.texto2['text'] = 'Parabéns você ganhou!'
        else:
            self.cont += 1
            errados.append(letra)
            self.mudar_er()
            if self.cont == 1:
                self.imagem1['image'] = self.sprite2
                self.imagem1.imagem = self.sprite2
            elif self.cont == 2:
                self.imagem1['image'] = self.sprite3
                self.imagem1.imagem = self.sprite3
            elif self.cont == 3:
                self.imagem1['image'] = self.sprite4
                self.imagem1.imagem = self.sprite4
            elif self.cont == 4:
                self.imagem1['image'] = self.sprite5
                self.imagem1.imagem = self.sprite5
            elif self.cont == 5:
                self.imagem1['image'] = self.sprite6
                self.imagem1.imagem = self.sprite6
            elif self.cont == 6:
                self.imagem1['image'] = self.sprite7
                self.imagem1.imagem = self.sprite7
                self.texto2['text'] = f'Você perdeu!! a palavra era {palavra2}'
                self.texto2['fg'] = 'red'
            
            
    #metodo para mudar o texto da palavra
    def mudar(self):
        letras = ''
        for letra in palavra_aux:
            letras +=  letra + ' '
        self.texto1['text'] = letras
    def mudar_ex(self):
        self.texto_ex['text'] = f'Existentes: {existentes}'
    def mudar_er(self):
        self.texto_er['text'] = f'Errados: {errados}'
    
        
#cria as nossa janela e define as coisas iniciais
janela = Tk()
jogo_forca(janela)
janela.title('Jogo da forca')
janela.geometry('800x600')
janela['bg'] = 'white'
janela.mainloop()
        

