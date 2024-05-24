import sqlite3
import pandas as pd
from tkinter import messagebox


class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('bancoAPAM.db')
        self.c = self.conn.cursor()
        self.create_tables()

    def get_columns(self, table: str='bancoapam'):
        self.c.execute(f"PRAGMA table_info({table})")
        db = self.c.fetchall()
        colunas = []
        for coluna_db in db:
            colunas.append(coluna_db[1])
        self.conn.commit()
        colunas.pop(0)
        return colunas

    def create_tables(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS bancoapam
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            cpf TEXT,
                            rg TEXT NOT NULL,
                            email TEXT NOT NULL,
                            estado_civil TEXT NOT NULL,
                            telefone TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data DATE NOT NULL,
                            data_nascimento DATE NOT NULL,
                            naturaliade TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            endereco_empresa TEXT NOT NULL,
                            valor_colaborar REAL NOT NULL,
                            nome_empresa TEXT NOT NULL,
                            profissao TEXT NOT NULL,
                            em_que_pode_ajuar_apam TEXT NOT NULL,
                            outras_formas_de_ajudar_apam TEXT NOT NULL,
                            expectativa_trabalho_voluntario TEXT NOT NULL,
                            imagem TEXT NOT NULL)''')
        self.conn.commit()

    def register_apam(self, values_table: list, table: str='bancoapam'):
        colunas = self.get_columns(table=table)
        inter = ['?'] * len(values_table)  # Use o comprimento de values_table
        query = f"INSERT INTO {table}({', '.join(colunas)}) VALUES ({','.join(inter)})"
        self.c.execute(query, values_table)
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registrado com Sucesso!')
        print("Registrado com Sucesso!")


    def view_all_bancoapam(self, table: str='bancoapam'):
        self.c.execute(f"SELECT * FROM {table}")
        data = self.c.fetchall()
        return data

    def search_apam(self, id, table: str='bancoapam'):
        self.c.execute(f"SELECT * FROM {table} WHERE id=?", (id,))
        data = self.c.fetchone()
        if data:
            return data
        else:
            messagebox.showerror('Erro', f'Nenhum ID {id} encontrado!')

    def update_apam(self, valor_atualizado, table: str='bancoapam'):
        data = valor_atualizado
        colunas = self.get_columns(table=table)
        if data:
            query = f"UPDATE {table} SET name=?, cpf=?, data=?, email=?, endereco=?, endereco_empresa=?, valor_colaborar=?, nome_empresa=?, profissao=?, em_que_pode_ajuar_apam=?, outras_formas_de_ajudar_apam=?, expectativa_trabalho_voluntario=?, imagem=? WHERE id=?"
            self.c.execute(query, valor_atualizado)
            self.conn.commit()
            messagebox.showinfo('Sucesso', f'Informação do ID {valor_atualizado[0]} foi atualizada!')
        else:
            messagebox.showerror('Erro', f"Nenhum ID {valor_atualizado[0]} encontrado!")

    def delete_apam(self, id, table: str='bancoapam'):
        self.c.execute(f"SELECT * FROM {table} WHERE id=?", (id,))
        data = self.c.fetchone()
        if data:
            self.c.execute(f"DELETE FROM {table} WHERE id=?", (id,))
            self.conn.commit()
            messagebox.showinfo('Sucesso', f"Informação do ID {id} foi deletada!")
        else:
            messagebox.showerror('Erro', f"Nenhum ID {id} encontrado!")

    def export_to_excel(self, table: str):
        self.c.execute(f"SELECT *, oid FROM {table}")
        to_excel = self.c.fetchall()
        colunas = self.get_columns(table=table)
        to_excel = pd.DataFrame(to_excel, columns=colunas)
        to_excel.to_excel(f'{table}.xlsx')
        self.conn.commit()


# create a registration system instance
registration_system = RegistrationSystem()
