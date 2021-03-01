from tkinter import *

def calc_main():
    class Calculadora():
        def __init__(self, master):
            # Instanciando Frames
            frm_resultado = Frame(master)
            frm_botoes = Frame(master)
            # Instanciando Labels
            self.entry_resultado = Entry(frm_resultado, width=13, bg='#fff', font=('helvetica', 32))

            #instanciando Botões
            btn_porcento = Button(frm_botoes, text='%', width=10, pady=10, command=lambda: self.click('%'))
            btn_raiz = Button(frm_botoes, text='raiz', width=10, pady=10, command=lambda: self.click(''))
            btn_exp = Button(frm_botoes, text='Exp', width=10, pady=10, command=lambda: self.click('**'))
            btn_fracao = Button(frm_botoes, text='1/x', width=10, pady=10, command=lambda: self.click(''))

            btn_CE = Button(frm_botoes, text='CE', width=10, pady=10, state=DISABLED)
            btn_C = Button(frm_botoes, text='C', width=10, pady=10, command=self.clear)
            btn_back = Button(frm_botoes, text='<<', width=10, pady=10, command=self.clear_end)
            btn_div = Button(frm_botoes, text='/', width=10, pady=10, command=lambda: self.click('/'))

            btn_7 = Button(frm_botoes, text='7', width=10, pady=10, command=lambda: self.click('7'))
            btn_8 = Button(frm_botoes, text='8', width=10, pady=10, command=lambda: self.click('8'))
            btn_9 = Button(frm_botoes, text='9', width=10, pady=10, command=lambda: self.click('9'))
            btn_mult = Button(frm_botoes, text='x', width=10, pady=10, command=lambda: self.click('x'))

            btn_4 = Button(frm_botoes, text='4', width=10, pady=10, command=lambda: self.click('4'))
            btn_5 = Button(frm_botoes, text='5', width=10, pady=10, command=lambda: self.click('5'))
            btn_6 = Button(frm_botoes, text='6', width=10, pady=10, command=lambda: self.click('6'))
            btn_sub = Button(frm_botoes, text='-', width=10, pady=10, command=lambda: self.click('-'))

            btn_1 = Button(frm_botoes, text='1', width=10, pady=10, command=lambda: self.click('1'))
            btn_2 = Button(frm_botoes, text='2', width=10, pady=10, command=lambda: self.click('2'))
            btn_3 = Button(frm_botoes, text='3', width=10, pady=10, command=lambda: self.click('3'))
            btn_soma = Button(frm_botoes, text='+', width=10, pady=10, command=lambda: self.click('+'))

            btn_inverte_sinal = Button(frm_botoes, text='+/-', width=10, pady=10)
            btn_zero = Button(frm_botoes, text='0', width=10, pady=10, command=lambda: self.click('0'))
            btn_ponto = Button(frm_botoes, text=',', width=10, pady=10, command=lambda: self.click('+'))
            btn_iqual = Button(frm_botoes, text='=', width=10, pady=10, command=self.igual)

            lista_btn = [btn_porcento, btn_raiz, btn_exp, btn_fracao, btn_CE, btn_C, btn_back, btn_div,
                         btn_7, btn_8, btn_9, btn_mult, btn_4, btn_5, btn_6, btn_sub, btn_1, btn_2, btn_3,
                         btn_soma, btn_inverte_sinal, btn_zero, btn_ponto, btn_iqual]

            #Exibindo widgets na tela
            frm_resultado.pack()
            frm_botoes.pack()
            self.entry_resultado.pack(padx=10, pady=10)

            cont = 0
            for row in range(0, 6):
                for col in range(4):
                    lista_btn[cont].grid(row=row, column=col)
                    cont += 1

        def click(self, txt):
            vlr_atual = self.entry_resultado.get()
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, vlr_atual + txt)

        def igual(self):
            vlr_atual = self.entry_resultado.get()
            if '+' in vlr_atual:
                vlr_atual = vlr_atual.split('+')
                result = float(vlr_atual[0]) + float(vlr_atual[1])
                self.entry_resultado.delete(0, END)
                self.entry_resultado.insert(0, str(result))
            elif '-' in vlr_atual:
                vlr_atual = vlr_atual.split('-')
                result = float(vlr_atual[0]) - float(vlr_atual[1])
                self.entry_resultado.delete(0, END)
                self.entry_resultado.insert(0, str(result))
            elif 'x' in vlr_atual:
                vlr_atual = vlr_atual.split('x')
                result = float(vlr_atual[0]) * float(vlr_atual[1])
                self.entry_resultado.delete(0, END)
                self.entry_resultado.insert(0, str(result))
            elif '/' in vlr_atual:
                vlr_atual = vlr_atual.split('/')
                result = float(vlr_atual[0]) / float(vlr_atual[1])
                self.entry_resultado.delete(0, END)
                self.entry_resultado.insert(0, str(result))

        def clear(self):
            self.entry_resultado.delete(0, END)

        def clear_end(self):
            vlr_atual = self.entry_resultado.get()
            vlr_atual = vlr_atual[:len(vlr_atual)-1]
            self.entry_resultado.delete(0, END)
            self.entry_resultado.insert(0, vlr_atual)


    root = Tk()
    root.title('Calculadora')
    root.resizable(False, False)
    my_gui = Calculadora(root)
    root.mainloop()

calc_main()