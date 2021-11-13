# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 23:41:28 2021

@author: Max Rafael
"""
# Importando as Bibliotecas necessárias
from tkinter import *
from sympy import *
import math
import numpy as np

# Parâmetros para Canvas:
xc, yc = 600, 400  # Largura e Altura do Canvas

# Parâmetros para Retângulo:
l, h = 100, 20  # Largura e Altura do Retângulo

# Parâmetro para Círculo:
raio = 10  # Diâmtro do círculo
pos_x, pos_y = l, h / 2  # Posição inicial do círculo

# Parâmetros globais
g = 9.81
n = 0.5  # Traço


# Cria uma Tela Inicial
Tela_inicial = Tk()
Tela_inicial.geometry('900x600+260+60')
Tela_inicial.title('    Janela Inicial')


Tela_inicial.iconbitmap('imagens/teste-online.ico')
Tela_inicial.state('zoomed')

# Texto 1

Label_1 = Label(Tela_inicial, text='Olá, este é um ambiente virtual desenvolvido para o\nestudo de Mecânica Clássica!', font='arial 25 bold')
Label_1.pack()
Label_1.place(x=120, y=80)

# Testo 2

Label_2 = Label(Tela_inicial, text='Selecione uma das opções:', font='arial 17', bd=1)
Label_2.pack()
Label_2.place(x=470, y=200)

Brasao = PhotoImage(file='Imagens/brasao-min.png')
Label_imagem = Label(Tela_inicial, image=Brasao)
Label_imagem.pack()
Label_imagem.place(x=1100, y=20)

Simb_colisao = PhotoImage(file='Imagens/simbol_colisao.png')
Label_imagem = Label(Tela_inicial, image=Simb_colisao, bd=1, relief='solid')
Label_imagem.pack()
Label_imagem.place(x=100+150, y=280)

Simb_canhao = PhotoImage(file='Imagens/simbol_canhao.png')
Label_imagem = Label(Tela_inicial, image=Simb_canhao, bd=1, relief='solid', height=260)
Label_imagem.pack()
Label_imagem.place(x=400+250, y=280)

'''def plot_grafico():
    
    ang = 45
    ang = math.radians(ang)
    v = 10
    a = 9.81
    n = 40
    
    x = Symbol('x')
    y = Function('y')
    R = Function('R')
    
    # Equações para gráfico da trajetória, y(x):
    
    y = math.tan(ang)*x - ((a*x**2)/(2*(v*math.cos(ang))**2))
    R = v**2/a*math.sin(2*ang)
    
    Lista_x = []
    Lista_x = np.linspace(0, R, n)
    
    # Equações para gráfico da posição em função do tempo, y(t):
    
    t =  2 * (v * math.sin(ang))/a
    tp = math.trunc(t) + 1
    
    Lista_t = np.linspace(0, tp, n)
    
    m = len(Lista_t)
    
    # Equações para gráfico da posição em função do tempo, x(t):
    
    Lista_y_t = []
    
    for i in range(m):
        Lista_y_t.append(v * math.sin(ang) * Lista_t[i] - (a * Lista_t[i]**2)/2)    
        
    print(len(Lista_t),len(Lista_y_t))
    
    
    Lista_y = []
    for i in range(n):
        Lista_y.append(math.tan(ang)*Lista_x[i] - ((a*Lista_x[i]**2)/(2*(v*math.cos(ang))**2)))
    
        
    print(ang, R)
    print(len(Lista_x))
    print(len(Lista_y))
    
    x_direct = 1
    y_direct = 0
    
    #print(y)
    plt.style.use('seaborn-white')
    
    fig1, axes_f1 = plt.subplots(nrows=2, ncols=2)
    
    axes_f1[0, 0].plot(Lista_x, Lista_y)
    axes_f1[1, 1].plot(Lista_t, Lista_y_t)
    
    
    for i in range(n):
        axes_f1[0, 0].plot(Lista_t[i], Lista_y[i], 'ro')
        axes_f1[0, 0].plot(Lista_t, Lista_y)
        #axes_f1[1, 0].set_title('Gráfico y(t) e Vetores velocidade')
        #axes_f1[1, 0].set_xlabel('Tempo (s)')
        #axes_f1[1, 0].set_ylabel('y (m)')
        axes_f1[0, 0].quiver(Lista_t[i], Lista_y[i], x_direct, y_direct, scale=10)
        axes_f1[0, 0].quiver(Lista_t[i], Lista_y[i], 0, (v * math.sin(ang)) - (a*Lista_t[i]), scale=200)
        plt.pause(0.001)
        axes_f1[0, 0].cla()
        
    axes_f1[0, 0].plot(Lista_t, Lista_y)
    axes_f1[0, 0].plot(Lista_t[i], Lista_y[i], 'ro')
    axes_f1[0, 0].quiver(Lista_t[i], Lista_y[i], x_direct, y_direct, scale=10)
    axes_f1[0, 0].quiver(Lista_t[i], Lista_y[i], 0, (v * math.sin(ang)) - (a*Lista_t[i]), scale=200)
    #axes_f1[1, 0].set_title('Gráfico y(t) e Vetores velocidade')
    #axes_f1[1, 0].set_xlabel('Tempo (s)')
    #axes_f1[1, 0].set_ylabel('y (m)')
        
    #plot(diff(y, x, 1))
    print(diff(y, x, 1))'''
        

    
'''def ex2():
    # Define os ângulos de 30, 45 e 60 graus para plotar:
    
    ang_1 = math.radians(30)
    ang_2 = math.radians(45)
    ang_3 = math.radians(60)
    
    # Define demais variáveis do problema:
        
    v = 10
    a = 9.81
    n = 40
    
    # Define algumas variáveis simbólocas para facilitar o plot:
        
    x = Symbol('x')
    y = Function('y')
    R = Function('R')
    
    # Equações para gráfico da trajetória, y(x):
        
    y1 = math.tan(ang_1)*x - ((a*x**2)/(2*(v*math.cos(ang_1))**2))
    y2 = math.tan(ang_2)*x - ((a*x**2)/(2*(v*math.cos(ang_2))**2))
    y3 = math.tan(ang_3)*x - ((a*x**2)/(2*(v*math.cos(ang_3))**2))
    
    # Expressão do alcance horizontal para definir a dimensão da matriz dos "x":
        
    R1 = v**2/a*math.sin(2*ang_1)
    R2 = v**2/a*math.sin(2*ang_2)
    R3 = v**2/a*math.sin(2*ang_3)
    
    # Expressão para definir o tempo e limitar o eixo "x":
        
    print(R1, R2, R3)
    Lista_x = []
    Lista_x = np.linspace(0, R2, n)
    
    Lista_y1 = []
    Lista_y2 = []
    Lista_y3 = []
    
    for i in range(n):
        Lista_y1.append(math.tan(ang_1)*Lista_x[i] - ((a*Lista_x[i]**2)/(2*(v*math.cos(ang_1))**2)))
        Lista_y2.append(math.tan(ang_2)*Lista_x[i] - ((a*Lista_x[i]**2)/(2*(v*math.cos(ang_2))**2)))
        Lista_y3.append(math.tan(ang_3)*Lista_x[i] - ((a*Lista_x[i]**2)/(2*(v*math.cos(ang_3))**2)))
        
    plt.style.use('seaborn-white')
        
    fig1, axes_f1 = plt.subplots()
    axes_f1.plot(Lista_x, Lista_y1)
    axes_f1.plot(Lista_x, Lista_y2)
    axes_f1.plot(Lista_x, Lista_y3)
    plt.show()'''
    

    
def Botao_2_click():

    Tela_inicial.destroy()

    class SimulaLanc:
        def __init__(self):

            self.janela = Tk()
            self.janela.geometry('800x600')
            self.janela.title('Lançamento de Projéteis')

            '''Definindo StringVars'''
            self.parameters = StringVar()
            self.propuse = StringVar()
            self.resultados = StringVar()

            '''Criando Contêineres para as geometrias'''
            self.Frame1 = Frame(self.janela)
            self.Frame2 = Frame(self.janela)
            self.Frame3 = Frame(self.janela)

            '''Criando Geometrias dentro dos Contêineres'''
            self.label1 = Label(self.janela, text='Ângulo')
            self.label2 = Label(self.janela, text='Velocidade')
            self.label0 = Label(self.janela, text='PARÂMETROS INICIAIS:')

            self.entry1 = Entry(self.janela)

            self.entry2 = Entry(self.janela)

            self.label3 = Label(self.Frame2, textvariable=self.parameters)

            self.canvas = Canvas(self.Frame1, bg='#d9daec', width=xc, height=yc)

            self.botao1 = Button(self.janela, text='Lançar', command=self.lanca)
            self.botao2 = Button(self.janela, text='Configurar Simulação', command=self.rotate)
            self.botao3 = Button(self.janela, text='Visualizar resultados', command=self.resultado)

            self.entrada1 = Entry(self.Frame3)
            self.entrada2 = Entry(self.Frame3)

            self.Frame1.pack()
            self.Frame2.pack()
            self.Frame3.pack()

            self.label_resultado = Label(self.janela, textvariable=self.resultados)

            self.label0.pack()
            self.label0.place(x=430 - 320, y=410)
            self.label1.pack()
            self.label1.place(x=540 - 320, y=430)
            self.entry1.pack()
            self.entry1.place(x=620 - 320, y=430)
            self.entry2.pack()
            self.entry2.place(x=620 - 320, y=460)
            self.label2.pack()
            self.label2.place(x=540 - 320, y=460)

            self.label3.pack()
            self.canvas.pack()
            # self.botao1.pack()
            self.botao2.pack()
            self.botao2.place(x=620 - 320, y=500)
            # self.botao3.pack()

            # self.entrada1.pack()
            # self.entrada2.pack()

            self.comeca()

            self.janela.mainloop()

        def comeca(self):
            '''
            VARIÁVEIS GLOBAIS PARA RETÂNGULO E CÍRCULO DEVEM
            SER DEFINIDAS
            '''

            self.P = (pos_x, pos_y)
            self.canvas.create_polygon(0, yc, l, yc, l, yc - h, 0, yc - h, fill='#39395a', outline='black', tag='canhao')
            # self.canvas.create_oval(self.P[0], yc - self.P[1], self.P[0] + raio, yc - self.P[1] + raio, fill='white', tag='bola')

        def matriz_rotacao(self, x, y):
            self.xp = (x * math.cos(self.var)) - (y * math.sin(self.var))
            self.yp = (y * math.cos(self.var)) + (x * math.sin(self.var))

            return (self.xp, self.yp)

        def rotate(self):

            try:
                float(self.entry1.get()) and float(self.entry2.get())
                self.label3['fg'] = 'blue'
                self.parameters.set(
                    'Valores fornecidos:       ' + self.entry1.get() + '°     |     ' + self.entry2.get() + 'm/s')

                self.botao2.forget()

                # Configura ângulo:
                self.var = float(self.entry1.get())

                print(self.entry1.get())
                self.var = math.radians(self.var)

                # Retângulo:
                self.B = self.matriz_rotacao(l, 0)
                self.C = self.matriz_rotacao(l, h)
                self.D = self.matriz_rotacao(0, h)

                # Círculo:
                self.P = self.matriz_rotacao(pos_x, pos_y)

                self.desenha()

                self.label1.forget()
                self.entry1.forget()

                self.label2.forget()
                self.entry2.forget()

                self.botao1.pack()
                self.botao1.place(x=800 - 320, y=500)


            except ValueError:

                self.label3['fg'] = 'red'
                self.parameters.set('Inválido')

        def desenha(self):
            self.canvas.delete('canhao')
            self.canvas.delete('bola')
            self.canvas.create_polygon(0, yc, self.B[0], yc - self.B[1], self.C[0], yc - self.C[1], self.D[0],
                                       yc - self.D[1], fill='#39395a', outline='black', tag='canhao')
            # self.canvas.create_oval(self.P[0], yc - self.P[1], self.P[0] + raio, yc - self.P[1] + raio, fill='white', tag='bola')

        # Criar método para associar ao lançamento - botão 2
        def lanca(self):
            self.botao1.forget()
            self.pos_x = self.P[0]
            self.pos_y = self.P[1]

            self.a = 1  # Aceleração para diminuir velocidade da bola no eixo y
            self.v_x, self.v_y = 15, 15

            self.lancamento()

        def lancamento(self):

            if self.pos_y < yc:
                self.update()
                self.desenhabola()
                self.janela.after(30, self.lancamento)

            self.botao3.pack()
            self.botao3.place(x=620 - 315, y=545)

        def update(self):
            self.pos_x += self.v_x * math.cos(self.var)
            self.pos_y = self.pos_y + self.v_y * math.sin(self.var) - self.a

            self.a += 1 / 2

        def desenhabola(self):
            if self.pos_y != yc:
                self.canvas.delete('bola')
            # self.canvas.create_oval(self.pos_x, yc - self.P[1], self.pos_x + n, yc - self.P[1] + n, fill='white', tag='traço')
            self.canvas.create_oval(self.pos_x, yc - self.pos_y, self.pos_x + n, yc - self.pos_y + n, fill='white',
                                    tag='traço')
            self.canvas.create_oval(self.pos_x, yc - self.pos_y, self.pos_x + raio, yc - self.pos_y + raio,
                                    fill='white',
                                    tag='bola')

        def resultado(self):

            self.angle = float(self.entry1.get())
            self.speed = float(self.entry2.get())
            self.angle = math.radians(self.angle)

            # Alcance horizontal
            self.R = (math.sin(2 * self.angle) * (self.speed) ** 2) / g
            self.R = round(self.R, 2)
            str(self.R)

            # Tempo total
            self.t = 2 * self.speed * math.sin(self.angle) / g
            self.t = round(self.t, 2)
            str(self.t)

            self.alc = StringVar()
            self.time = StringVar()

            self.alc.set(self.R)
            self.time.set(self.t)

            self.resultados.set('Alcance horizontal, em m = \n \nTempo total, em s = ')
            self.label_resultado.pack()
            self.label_resultado.place(x=540, y=450)

            self.alcance = Label(self.janela, textvariable=self.alc)
            self.alcance.pack()
            self.alcance.place(x=710, y=450)

            self.tempo = Label(self.janela, textvariable=self.time)
            self.tempo.pack()
            self.tempo.place(x=720, y=480)

        '''def resultado(self):
            self.angle = float(self.entry1.get())
            self.speed = float(self.entry2.get())

            float(self.speed) and float(self.angle)

            self.A = ((self.speed ** 2) * math.sin(2 * self.angle)) / g  # Alcance Horizontal

            x = np.linspace(0, self.A, 100)
            y = np.tan(self.angle) * x - (g * x ** 2) / (2 * (self.speed * np.cos(self.angle)) ** 2)

            plt.plot(x, y)
            plt.show
            print(self.A)'''

    SimulaLanc()


def Botao_1_click():
    pass



Botao_1 = Button(Tela_inicial, text = 'Colisão', command=Botao_1_click, bg='#aed0ea', fg='black', font='arial 15 bold', width=21, height=2, relief='raised', cursor="hand2")
Botao_1.pack()
Botao_1.place(x=99+150, y=543)


Botao_2 = Button(Tela_inicial, text = 'Movimento de Projéteis', command=Botao_2_click, bg='#aed0ea', fg='black', width=21, height=2, font='arial 15 bold', cursor="hand2")
Botao_2.pack()
Botao_2.place(x=397+250, y=543)



Tela_inicial.mainloop()
