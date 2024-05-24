import tkinter as tk
from tkinter import messagebox
from FuncPerfils.data_management import salvar_perfil
from FuncPerfils.carregaPerfil import carrega_perfil
from FuncPerfils.perfilMatri import pesquisar_por_matricula
from FuncPerfils.exporExcel import exportar_para_excel
from FuncPerfils.verperfil import ver_perfil
from FuncPerfils.excluirPerfil import excluir_perfil
from FuncPerfils.editarinfo import editar_info

# Função para salvar as informações editadas
def salvar(perfil, perfis):
    perfil['Nome'] = entries['Nome Completo:'].get()
    perfil['Matricula'] = entries['Matrícula:'].get()
    perfil['Celular'] = entries['Número de Celular:'].get()
    perfil['Número fixo'] = entries['Número fixo:'].get()
    perfil['Telefone da empresa de trabalho'] = entries['Telefone da empresa de trabalho:'].get()
    perfil['Cargo'] = entries['Cargo:'].get()
    perfil['Data de Nascimento'] = entries['Data de Nascimento:'].get()
    perfil['Data'] = entries['Data:'].get()
    perfil['CPF'] = entries['CPF:'].get()
    perfil['RG'] = entries['RG:'].get()
    perfil['Gênero'] = entries['Gênero:'].get()
    perfil['Email'] = entries['Email:'].get()
    perfil['Endereço completo'] = entries['Endereço completo:'].get()
    perfil['Nome da empresa de trabalho'] = entries['Nome da empresa de trabalho:'].get()
    perfil['Profissão'] = entries['Profissão:'].get()
    perfil['Naturalidade'] = entries['Naturalidade:'].get()
    perfil['Endereço da empresa de trabalho'] = entries['Endereço da empresa de trabalho:'].get()
    perfil['Com qual valor mensal poderia colaborar?'] = entries['Com qual valor mensal poderia colaborar?:'].get()
    perfil['Estado Civil'] = entries['Estado Civil:'].get()

    window_editar.destroy()
    exportar_para_excel(perfis)

def adicionar_perfil():
    novo_nome = entries['Nome Completo:'].get()
    novo_perfil = {
        "Nome": novo_nome,
        "Matricula": entries['Matrícula:'].get(),
        "Celular": entries['Número de Celular:'].get(),
        "Número fixo": entries['Número fixo:'].get(),
        "Telefone da empresa de trabalho": entries['Telefone da empresa de trabalho:'].get(),
        "Cargo": entries['Cargo:'].get(),
        "Data de Nascimento": entries['Data de Nascimento:'].get(),
        "Data": entries['Data:'].get(),
        "CPF": entries['CPF:'].get(),
        "RG": entries['RG:'].get(),
        "Gênero": entries['Gênero:'].get(),
        "Email": entries['Email:'].get(),
        "Endereço completo": entries['Endereço completo:'].get(),
        "Nome da empresa de trabalho": entries['Nome da empresa de trabalho:'].get(),
        "Profissão": entries['Profissão:'].get(),
        "Naturalidade": entries['Naturalidade:'].get(),
        "Endereço da empresa de trabalho": entries['Endereço da empresa de trabalho:'].get(),
        "Com qual valor mensal poderia colaborar?": entries['Com qual valor mensal poderia colaborar?:'].get(),
        "Estado Civil": entries['Estado Civil:'].get()
    }
    perfis[novo_nome] = novo_perfil
    listbox_nomes.insert(tk.END, novo_nome)
    salvar_perfil(perfis)
    exportar_para_excel(perfis)

# Função para editar informações do perfil
def editar_informacao():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        editar_info(perfil_selecionado, perfis)

# Inicialização dos perfis
perfis = carrega_perfil()

# Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title('Gerenciador de Perfis')

def create_label_entry(frame, text):
    label = tk.Label(frame, text=text)
    label.pack(anchor='w', pady=2)
    entry = tk.Entry(frame)
    entry.pack(fill='x', pady=2)
    return entry

# Cria os frames para cada coluna
frame_col1 = tk.Frame(janela_principal)
frame_col1.grid(row=0, column=0, padx=10, pady=10, sticky='n')

frame_col2 = tk.Frame(janela_principal)
frame_col2.grid(row=0, column=1, padx=10, pady=10, sticky='n')

frame_col3 = tk.Frame(janela_principal)
frame_col3.grid(row=0, column=2, padx=10, pady=10, sticky='n')

# Adiciona os campos nos frames
fields_col1 = [
    'Nome Completo',
    'Matrícula',
    'Número de Celular',
    'Número fixo',
    'Telefone da empresa de trabalho',
    'Cargo',
    'Estado Civil',
]

fields_col2 = [
    'Data de Nascimento',
    'Data',
    'CPF',
    'RG',
    'Gênero',
    'Email',
]

fields_col3 = [
    'Endereço completo',
    'Nome da empresa de trabalho',
    'Profissão',
    'Naturalidade',
    'Endereço da empresa de trabalho',
    'Com qual valor mensal poderia colaborar?',
    
]

entries = {}

# Adiciona os campos à primeira coluna
for field in fields_col1:
    entries[field] = create_label_entry(frame_col1, field)

# Adiciona os campos à segunda coluna
for field in fields_col2:
    entries[field] = create_label_entry(frame_col2, field)

# Adiciona os campos à terceira coluna
for field in fields_col3:
    entries[field] = create_label_entry(frame_col3, field)

# Adiciona os botões abaixo das colunas
frame_buttons = tk.Frame(janela_principal)
frame_buttons.grid(row=1, column=0, columnspan=3, pady=10)

def pesquisar_matricula():
    def pesquisar():
        matricula = entry_matricula_pesquisa.get()
        perfil_encontrado = pesquisar_por_matricula(matricula, perfis)
        if perfil_encontrado:
            messagebox.showinfo("Perfil Encontrado", f"Nome: {perfil_encontrado}")
        else:
            messagebox.showinfo("Perfil não encontrado", f"Nenhum perfil encontrado para a matrícula {matricula}")

    window_pesquisar = tk.Toplevel()
    window_pesquisar.title('Pesquisar Matrícula')

    tk.Label(window_pesquisar, text='Matrícula:').grid(row=0, column=0)
    entry_matricula_pesquisa = tk.Entry(window_pesquisar)
    entry_matricula_pesquisa.grid(row=0, column=1)

    btn_pesquisar = tk.Button(window_pesquisar, text='Pesquisar', command=pesquisar)
    btn_pesquisar.grid(row=1, column=0, columnspan=2)

frame_buttons = tk.Frame(janela_principal)
frame_buttons.grid(row=1, column=0, columnspan=3, pady=10)

btn_pesquisar_matricula = tk.Button(frame_buttons, text='Pesquisar Matrícula', command=pesquisar_matricula)
btn_pesquisar_matricula.pack(side='left', padx=5)

btn_adicionar = tk.Button(frame_buttons, text='Adicionar', command=adicionar_perfil)
btn_adicionar.pack(side='left', padx=5)

btn_excluir = tk.Button(frame_buttons, text='Excluir', command=lambda: excluir_perfil(listbox_nomes, perfis))
btn_excluir.pack(side='left', padx=5)

btn_ver_perfil = tk.Button(frame_buttons, text='Ver Perfil', command=lambda: ver_perfil(perfis, listbox_nomes))
btn_ver_perfil.pack(side='left', padx=5)

btn_editar_info = tk.Button(frame_buttons, text='Editar Informação', command=editar_informacao)
btn_editar_info.pack(side='left', padx=5)

listbox_nomes = tk.Listbox(janela_principal, width=60, height=15)
listbox_nomes.grid(row=2, column=0, columnspan=3, pady=10)
# Adicionando nomes existentes na Listbox
for nome in perfis.keys():
    listbox_nomes.insert(tk.END, nome)

janela_principal.mainloop()
