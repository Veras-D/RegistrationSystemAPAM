# importando dependencias do Tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from ttkthemes import ThemedTk


# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date
from banco import RegistrationSystem
from util import Validacao
# chamdo a view
from banco import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul

class Example(ThemedTk):
    """
    Example that is used to create screenshots for new themes.
    """
    def __init__(self, theme="aquativo"):
        """
        :param theme: Theme to show off
        """
        ThemedTk.__init__(self, fonts=True, themebg=True)
        self.set_theme(theme)
        # Create widgets
        self.notebook = ttk.Notebook(self)
        self.notebook.add(ttk.Button(self, text="Hello World"), text="Frame One")
        self.notebook.add(ttk.Button(self, text="Hello Universe"), text="Frame Two")
        self.menu = tk.Menu(self, tearoff=False)



#janelas 
janela = Tk()
janela.title("SISTEMA DE CADASTRO | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)")
janela.geometry('1200x600')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# janela = Tk()
# janela.title("SISTEMA DE CADASTRO | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)")
# janela.configure(background=co1)
# janela.resizable(True, True)



for i in range(5):
    janela.grid_columnconfigure(i, weight=1)
    
def maximize_window(event=None):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    window_width = janela.winfo_reqwidth()
    window_height = janela.winfo_reqheight()
    # x = (screen_width // 10) - (window_width // 10)
    # y = (screen_height // 5) - (window_height // 5)
    # janela.geometry(f"{window_width}x{window_height}+{x}+{y}")
    

janela.bind("<Configure>", maximize_window)



style = Style(janela)
style.theme_use("clam")

# Frames
frame_logo = Frame(janela, width=1200, height=70, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=1200, height=100, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=1200, height=1200, bg=co1)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)


# frame Logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('assets/logo.png')
app_lg = app_lg.resize((65,65))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="APAM - Associação Mato-Grossense Protetora dos Animais", width=1200, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1, padx=20)
app_logo.place(x=5, y=0)


# abrindo a imagem
imagem  = Image.open('assets/logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

# l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
# l_imagem.place(x=755, y=10)

# ------------- funcoes para CRUD ---------------

def adicionar():
    global imagem_string

    # nome = e_nome.get()
    # cpf = c_cpf.get()
    # rg = r_rg.get()
    # data = data_nascimento.get()
    # email = e_email.get()
    # endereco = e_endereco.get()
    # matricula = e_matricula.get()
    # telefone_empresa = e_telefone_empresa.get()
    # sexo = c_sexo.get()
    # temperamento = t_temperamento.get()
    # img = imagem_string
    data_registro = d_data_registro.get()
    email = e_email.get()
    name = n_nome.get()
    cpf = c_cpf.get()
    rg = r_rg.get()
    data_nascimento = d_data_nascimento.get()
    sexo = s_sexo.get()
    naturalidade = n_naturalidade.get()
    estado_civil = e_estado_civil.get()
    endereco = e_endereco.get()
    telefone_fixo = t_telefone_fixo.get()
    telefone_celular = t_telefone_celular.get()
    nome_empresa = n_nome_empresa.get()
    endereco_empresa = e_endereco_empresa.get()
    telefone_empresa = t_telefone_empresa.get()
    profissao = p_profissao.get()
    valor_colaborar = v_valor_colaborar.get()
    em_que_pode_ajudar_apam = e_em_que_pode_ajudar_apam.get()
    outras_formas_de_ajudar_apam = o_outras_formas_de_ajudar_apam.get()
    expectativa_trabalho_volutario = e_expectativa_trabalho_volutario.get()
    imagem = i_imagem.get()
    
    
       
    lista = [data_registro, email, name, cpf, rg, data_nascimento, sexo, naturalidade, estado_civil, endereco, telefone_fixo, telefone_celular, nome_empresa, endereco_empresa, telefone_empresa, profissao, valor_colaborar, em_que_pode_ajudar_apam, outras_formas_de_ajudar_apam, expectativa_trabalho_volutario, imagem]
    for i in lista:
        if not Validacao.verificarCampo(i):
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    
    # if not Validacao.validarNome(nome):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarCPF(cpf):
    #     messagebox.showerror('Erro', 'CPF inválido')
    #     return
    # if not Validacao.validarEmail(email):
    #     messagebox.showerror('Erro', 'Email inválido')
    #     return
    # if not Validacao.validarCEP(endereco):
    #     messagebox.showerror('Erro', 'CEP inválido')
    #     return
    # if not Validacao.validarTelefone_e_Celular(tel):
    #     messagebox.showerror('Erro', 'Telefone/Celular inválido')
    #     return
    # if not Validacao.validarSexo(sexo):
    #     messagebox.showerror('Erro', 'Sexo inválido')
    #     return
    if not Validacao.validarNome(data_registro):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(email):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(name):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(cpf):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(rg):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(data_nascimento):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(sexo):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(naturalidade):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(estado_civil):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(endereco):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(telefone_fixo):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(nome_empresa):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(nome_empresa):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(endereco_empresa):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(telefone_empresa):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(profissao):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(valor_colaborar):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(em_que_pode_ajudar_apam):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(outras_formas_de_ajudar_apam):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    if not Validacao.validarNome(expectativa_trabalho_volutario):
        messagebox.showerror('Erro', 'Nome inválido')
        return
    
   
    apam = (data_registro, email, name, cpf, rg, data_nascimento, sexo, naturalidade, estado_civil, endereco, telefone_fixo, telefone_celular, nome_empresa, endereco_empresa, telefone_empresa, profissao, valor_colaborar, em_que_pode_ajudar_apam, outras_formas_de_ajudar_apam, expectativa_trabalho_volutario)
    registration_system.register_apam(apam)

    
    # e_nome.delete(0, END)
    # c_cpf.delete(0, END)
    # data_nascimento.delete(0, END)
    # e_email.delete(0, END)
    # e_endereco.delete(0, END)
    # e_matricula.delete(0, END)
    # e_tel.delete(0, END)
    # c_sexo.delete(0, END)
    # t_temperamento.delete(0, END)
    d_data_registro(0, END)
    e_email(0, END)
    n_nome(0, END)
    c_cpf(0, END)
    r_rg(0, END)
    d_data_nascimento(0, END)
    s_sexo(0, END)
    n_naturalidade(0, END)
    e_estado_civil(0, END)
    e_endereco(0, END)
    t_telefone_fixo(0, END)
    t_telefone_celular(0, END)
    n_nome_empresa(0, END)
    e_endereco_empresa(0, END)
    t_telefone_empresa(0, END)
    p_profissao(0, END)
    v_valor_colaborar(0, END)
    e_em_que_pode_ajudar_apam(0, END)
    o_outras_formas_de_ajudar_apam(0, END)
    e_expectativa_trabalho_volutario(0, END)
    
  
    mostrar_tabela()


def procurar():
	global imagem, imagem_string, l_imagem

	
	id_apam = int(e_procurar.get())


	dados = registration_system.search_apam(id_apam)

	
	# e_nome.delete(0,END)
	# c_cpf.delete(0,END)
	# data_nascimento.delete(0,END)
	# e_email.delete(0,END)
	# e_endereco.delete(0,END)
	# e_matricula.delete(0,END)
	# e_tel.delete(0,END)
	# c_sexo.delete(0,END)
	# t_temperamento.delete(0,END)
	d_data_registro.delete(0, END)
	e_email.delete(0, END)
	n_nome.delete(0, END)
	c_cpf.delete(0, END)
	r_rg.delete(0, END)
	d_data_nascimento.delete(0, END)
	s_sexo.delete(0, END)
	n_naturalidade.delete(0, END)
	e_estado_civil.delete(0, END)
	e_endereco.delete(0, END)
	t_telefone_fixo.delete(0, END)
	t_telefone_celular.delete(0, END)
	n_nome_empresa.delete(0, END)
	e_endereco_empresa.delete(0, END)
	t_telefone_empresa.delete(0, END)
	p_profissao.delete.delete(0, END)
	v_valor_colaborar.delete(0, END)
	e_em_que_pode_ajudar_apam.delete(0, END)
	o_outras_formas_de_ajudar_apam.delete(0, END)
	e_expectativa_trabalho_volutario.delete(0, END)

	
	# e_nome.insert(END,dados[1])
	# c_cpf.insert(END,dados[2])
	# data_nascimento(END,dados[3])
	# e_email.insert(END,dados[4])
	# e_endereco.insert(END,dados[5])
	# e_matricula.insert(END,dados[6])
	# e_tel.insert(END,dados[7])
	# c_sexo.insert(END,dados[8])
	# t_temperamento.insert(END,dados[9])
	d_data_registro.insert(END,dados[1])
	e_email.insert(END,dados[2])
	n_nome.insert(END,dados[3])
	c_cpf.insert(END,dados[4])
	r_rg.insert(END,dados[5])
	d_data_nascimento.insert(END,dados[6])
	s_sexo.insert(END,dados[7])
	n_naturalidade.insert(END,dados[8])
	e_estado_civil.insert(END,dados[9])
	e_endereco.insert(END,dados[10])
	t_telefone_fixo.insert(END,dados[11])
	t_telefone_celular.insert(END,dados[12])
	n_nome_empresa.insert(END,dados[13])
	e_endereco_empresa.insert(END,dados[14])
	t_telefone_empresa.insert(END,dados[15])
	p_profissao.delete.insert(END,dados[16])
	v_valor_colaborar.insert(END,dados[17])
	e_em_que_pode_ajudar_apam.insert(END,dados[18])
	o_outras_formas_de_ajudar_apam.insert(END,dados[19])
	e_expectativa_trabalho_volutario.insert(END,dados[20])
	

	imagem = dados[21]
	imagem_string = imagem


	imagem  = Image.open(imagem)
	imagem = imagem.resize((130, 130))
	imagem = ImageTk.PhotoImage(imagem)

	l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
	l_imagem.place(x=755, y=10)



def atualizar():
	global imagem, imagem_string, l_imagem

	# obtendo o id
	id_apam = int(e_procurar.get())

	# obtendo os valores
	# nome = e_nome.get()
	# cpf = c_cpf.get()
	# data = data_nascimento.get()
	# email = e_email.get()
	# endereco = e_endereco.get()
	# matricula = e_matricula.get()
	# tel = e_tel.get()
	# sexo = c_sexo.get()
	# temperamento = t_temperamento.get()
	# img = imagem_string
	data_registro = d_data_registro.get()
	email = e_email.get()
	name = n_nome.get()
	cpf = c_cpf.get()
	rg = r_rg.get()
	data_nascimento = d_data_nascimento.get()
	sexo = s_sexo.get()
	naturalidade = n_naturalidade.get()
	estado_civil = e_estado_civil.get()
	endereco = e_endereco.get()
	telefone_fixo = t_telefone_fixo.get()
	telefone_celular = t_telefone_celular.get()
	nome_empresa = n_nome_empresa.get()
	endereco_empresa = e_endereco_empresa.get()
	telefone_empresa = t_telefone_empresa.get()
	profissao = p_profissao.get()
	valor_colaborar = v_valor_colaborar.get()
	em_que_pode_ajudar_apam = e_em_que_pode_ajudar_apam.get()
	outras_formas_de_ajudar_apam = o_outras_formas_de_ajudar_apam.get()
	expectativa_trabalho_volutario = e_expectativa_trabalho_volutario.get()
	imagem = i_imagem.get()

	# lista = [nome, cpf, data, email, endereco, matricula, tel, sexo, temperamento, img, id_apam]
	lista = [data_registro, email, name, cpf, rg, data_nascimento, sexo, naturalidade, estado_civil, endereco, telefone_fixo, telefone_celular, nome_empresa, endereco_empresa, telefone_empresa, profissao, valor_colaborar, em_que_pode_ajudar_apam, outras_formas_de_ajudar_apam, expectativa_trabalho_volutario, imagem, id_apam]

	# Verificando caso algum campo esteja vazio ou nao
	for i in lista:
		if i == '':
			messagebox.showerror('Erro', 'Preencha todos os campos')
			return

	# atualizar cadastro do apam
	registration_system.update_apam(lista)

	# limpando os campos de entradas
	# e_nome.delete(0,END)
	# c_cpf.delete(0,END)
	# data_nascimento.delete(0,END)
	# e_email.delete(0,END)
	# e_endereco.delete(0,END)
	# e_matricula.delete(0,END)
	# e_tel.delete(0,END)
	# c_sexo.delete(0,END)
	# t_temperamento.delete(0,END)
	d_data_registro.delete(0, END)
	e_email.delete(0, END)
	n_nome.delete(0, END)
	c_cpf.delete(0, END)
	r_rg.delete(0, END)
	d_data_nascimento.delete(0, END)
	s_sexo.delete(0, END)
	n_naturalidade.delete(0, END)
	e_estado_civil.delete(0, END)
	e_endereco.delete(0, END)
	t_telefone_fixo.delete(0, END)
	t_telefone_celular.delete(0, END)
	n_nome_empresa.delete(0, END)
	e_endereco_empresa.delete(0, END)
	t_telefone_empresa.delete(0, END)
	p_profissao.delete.delete(0, END)
	v_valor_colaborar.delete(0, END)
	e_em_que_pode_ajudar_apam.delete(0, END)
	o_outras_formas_de_ajudar_apam.delete(0, END)
	e_expectativa_trabalho_volutario.delete(0, END)

	# abre a imagem
	imagem  = Image.open('assets/logo.png')
	imagem = imagem.resize((130, 130))
	imagem = ImageTk.PhotoImage(imagem)

	i_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
	l_imagem.place(x=755, y=10)

	# mostrando os valores na Tabela
	mostrar_tabela()



# funcao deletar
def deletar():
	global imagem, imagem_string, l_imagem

	# obtendo o id
	id_apam = int(e_procurar.get())

	# deleta o ID do apam
	registration_system.delete_apam(id_apam)

	# limpando os campos de entradas
	# e_nome.delete(0,END)
	# c_cpf.delete(0,END)
	# data_nascimento.delete(0,END)
	# e_email.delete(0,END)
	# e_endereco.delete(0,END)
	# e_matricula.delete(0,END)
	# e_tel.delete(0,END)
	# c_sexo.delete(0,END)
	# t_temperamento.delete(0,END)
	d_data_registro.delete(0, END)
	e_email.delete(0, END)
	n_nome.delete(0, END)
	c_cpf.delete(0, END)
	r_rg.delete(0, END)
	d_data_nascimento.delete(0, END)
	s_sexo.delete(0, END)
	n_naturalidade.delete(0, END)
	e_estado_civil.delete(0, END)
	e_endereco.delete(0, END)
	t_telefone_fixo.delete(0, END)
	t_telefone_celular.delete(0, END)
	n_nome_empresa.delete(0, END)
	e_endereco_empresa.delete(0, END)
	t_telefone_empresa.delete(0, END)
	p_profissao.delete.delete(0, END)
	v_valor_colaborar.delete(0, END)
	e_em_que_pode_ajudar_apam.delete(0, END)
	o_outras_formas_de_ajudar_apam.delete(0, END)
	e_expectativa_trabalho_volutario.delete(0, END)

	e_procurar.delete(0,END)

	# abrindo a imagem
	imagem  = Image.open('assets/logo.png')
	imagem = imagem.resize((130, 130))
	imagem = ImageTk.PhotoImage(imagem)

	l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
	l_imagem.place(x=755, y=10)

	# mostrando os valores na Tabela
	mostrar_tabela()


# criando campos de entrada
l_nome = Label(frame_detalhes, text="NOME *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
n_nome = ttk.Entry(frame_detalhes, width=122, justify='left')
n_nome.place(x=7, y=35)

l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cpf.place(x=4, y=60)
c_cpf = ttk.Entry(frame_detalhes, width=30, justify='left')
c_cpf.place(x=7, y=84)

l_rg = Label(frame_detalhes, text="RG *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_rg.place(x=197, y=60)
e_rg = ttk.Entry(frame_detalhes, width=30, justify='left')
e_rg.place(x=200, y=84)

l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=393, y=60)
d_data_nascimento = DateEntry(frame_detalhes, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
d_data_nascimento.place(x=395, y=84)

l_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=678, y=60)
s_sexo = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 8 bold'), justify='center')
s_sexo['values'] = ('M','F')
s_sexo.place(x=680, y=85)

l_telefone_fixo = Label(frame_detalhes, text="TELEFONE FIXO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone_fixo.place(x=4, y=109)
t_telefone_fixo = ttk.Entry(frame_detalhes, width=30, justify='left')
t_telefone_fixo.place(x=7, y=134)

l_telefone_celular = Label(frame_detalhes, text="TELEFONE MÓVEL *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone_celular.place(x=197, y=109)
e_telefone_celular = ttk.Entry(frame_detalhes, width=30, justify='left')
e_telefone_celular.place(x=200, y=134)

estado_civil_p = ['Solteiro','Casado','União estável']
estado_civil = []

for i in estado_civil_p:
	estado_civil.append(i)

l_estado_civil = Label(frame_detalhes, text="ESTADO CIVIL *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_estado_civil.place(x=530, y=60)
e_estado_civil = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
e_estado_civil['values'] = (estado_civil)
e_estado_civil.place(x=532, y=85)

# funcao para escolher imagem

# def escolher_imagem():
# 	global imagem, imagem_string, l_imagem

	# imagem = fd.askopenfilename()
	# imagem_string = imagem

	# abre a imagem
	# imagem = Image.open(imagem)
	# imagem = imagem.resize((130,130))
	# imagem = ImageTk.PhotoImage(imagem)
	# l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
	# l_imagem.place(x=755, y=10)

	# botao_carregar['text'] = 'Trocar de foto'

# botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar Foto".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
# botao_carregar.place(x=755, y=160)


# Tabela do banco apam
def mostrar_tabela():

	# area do scrollbars
	#list_header = ['id','Nome','email',  'Telefone','sexo','Data', 'Endereço','temperamento']
	list_header = ['id', 'Nome', 'CPF', 'Matricula', 'Email', 'Telefone','Sexo','Data Nascimento', 'Endereço', 'Temperamento']

	# visualiza as informações do banco apam
	df_list = registration_system.view_all_bancoapam()

	global tree_temperamento

	tree_apam = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

	# vertical scrollbar
	vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_apam.yview)
	# horizontal scrollbar
	hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_apam.xview)

	tree_apam.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_apam.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_tabela.grid_rowconfigure(0, weight=12)

	hd=["center","nw","center","center","center","center","center","center","nw","center"]
	h=[116,116,116,116,116,116,60,152,116,136]
	n=0

	for col in list_header:
		tree_apam.heading(col, text=col.title(), anchor=NW)

		# ajustes das colunas dentro do scrollbar
		tree_apam.column(col, width=h[n],anchor=hd[n])

		n += 1

	for item in df_list:
		tree_apam.insert('', 'end', values=item)



# Procura os dados cadastrados

# frame_procurar = Frame(frame_botoes, width=40, height=50, bg=co1, relief=RAISED)
# frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

# l_nome = Label(frame_procurar, text="Realize a Busca pelo  ID ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
# l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
# e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
# e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

# l_cpf = Label(frame_procurar, text="Realize a Busca pelo  ID ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
# l_cpf.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
# e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
# e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

# l_data_nascimento = Label(frame_procurar, text="Realize a Busca pelo  ID ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
# l_data_nascimento.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
# e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
# e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

# botao_procurar = Button(frame_procurar,command=procurar, anchor=CENTER, text="Procurar", width=9, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
# botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botoes

# app_img_adicionar = Image.open('assets/add.png')
# app_img_adicionar = app_img_adicionar.resize((25,25))
# app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
# app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
# app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

# app_img_atualizar = Image.open('assets/update.png')
# app_img_atualizar = app_img_atualizar.resize((25,25))
# app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
# app_atualizar = Button(frame_botoes,command=atualizar, image=app_img_atualizar, text=" Atualizar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
# app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

# app_img_deletar = Image.open('assets/delete.png')
# app_img_deletar = app_img_deletar.resize((25,25))
# app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
# app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, text=" Deletar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
# app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)


# linha separatoria

l_linha = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
l_linha.place(x=265, y=0)


# ver a tabela de cadastro
mostrar_tabela()

janela.mainloop()

if __name__ == '__main__':
    example = Example()
    example.set_theme("adapta")
