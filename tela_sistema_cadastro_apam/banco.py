import sqlite3
import pandas as pd
from tkinter import messagebox


class RegistrationSystem:
    def __init__(self):
        self.create_tables()


    def db_execute(self, query, param = []):
        with sqlite3.connect('bancoAPAM.db') as conn:
            c = conn.cursor()
            c.execute(query, param)
            conn.commit()
            return c.fetchall()


    def get_columns(self, table: str='bancoapam'):
        db = self.db_execute(f"PRAGMA table_info({table})")
        colunas = []
        for coluna_db in db:
            colunas.append(coluna_db[1])
        colunas.pop(0)
        return colunas


    def create_tables(self):
        self.db_execute('''CREATE TABLE IF NOT EXISTS bancoapam
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            data_registro DATE NOT NULL,
                            email TEXT NOT NULL,
                            name TEXT NOT NULL,
                            cpf TEXT,
                            rg TEXT NOT NULL,
                            data_nascimento DATE NOT NULL,
                            sexo TEXT NOT NULL,
                            naturaliade TEXT NOT NULL,
                            estado_civil TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            telefone_fixo TEXT,
                            telefone_celular TEXT NOT NULL,
                            nome_empresa TEXT,
                            endereco_empresa TEXT NOT NULL,
                            telefone_empresa TEXT,
                            profissao TEXT NOT NULL,
                            valor_colaborar REAL NOT NULL,
                            em_que_pode_ajuar_apam TEXT,
                            outras_formas_de_ajudar_apam TEXT,
                            expectativa_trabalho_voluntario TEXT)''')


    def register_apam(self, values_table: list, table: str='bancoapam'):
        colunas = self.get_columns(table=table)
        inter = ['?'] * len(colunas)  # Use o comprimento de colunas
        query = f"INSERT INTO {table}({', '.join(colunas)}) VALUES ({','.join(inter)})"
        self.db_execute(query=query, param=values_table)
        messagebox.showinfo('Sucesso', 'Registrado com Sucesso!')
        print("Registrado com Sucesso!")


    def view_all_bancoapam(self, table: str='bancoapam'):
        data = self.db_execute(f"SELECT * FROM {table}")
        return data


    def search_apam(self, id, table: str='bancoapam'):
        data = self.db_execute(f"SELECT * FROM {table} WHERE id=?", (id,))
        if data:
            return data
        else:
            messagebox.showerror('Erro', f'Nenhum ID {id} encontrado!')


    def update_apam(self, valor_atualizado, table: str='bancoapam'):
        data = valor_atualizado
        colunas = self.get_columns(table=table)
        if data:
            #ajuste os campos da linha abaixo conforme as talbelas
            query = f"UPDATE {table} SET data_registro=?, email=?, name=?, cpf=?, rg=?, data_nascimento=?, sexo=?, naturaliade=?, estado_civil=?, endereco=?, telefone_fixo=?, telefone_celular=?, nome_empresa=?, endereco_empresa=?, telefone_empresa=?, profissao=?, valor_colaborar=?, em_que_pode_ajuar_apam=?, outras_formas_de_ajudar_apam=?, expectativa_trabalho_voluntario=? WHERE id=?"
            self.db_execute(query, valor_atualizado)
            messagebox.showinfo('Sucesso', f'Informação do ID {valor_atualizado[0]} foi atualizada!')
        else:
            messagebox.showerror('Erro', f"Nenhum ID {valor_atualizado[0]} encontrado!")


    def delete_apam(self, id, table: str='bancoapam'):
        data = self.db_execute(f"SELECT * FROM {table} WHERE id=?", (id,))
        if data:
            self.db_execute(f"DELETE FROM {table} WHERE id=?", (id,))
            messagebox.showinfo('Sucesso', f"Informação do ID {id} foi deletada!")
        else:
            messagebox.showerror('Erro', f"Nenhum ID {id} encontrado!")


    def get_name(self, table: str='bancoapam'):
        data = self.db_execute(f'SELECT name, oid FROM {table}')
        return data


    def export_to_excel(self, table: str='bancoapam'):
        try:
            to_excel = self.db_execute(f"SELECT * FROM {table}")
            colunas = self.get_columns(table=table)
            colunas.insert(0,'id')
            to_excel = pd.DataFrame(to_excel, columns=colunas)
            to_excel.to_excel(f'{table}.xlsx')
            messagebox.showinfo('Sucesso', 'Exportado com sucesso!')
        except Exception as e:
            messagebox.showerror('Erro', f"Falha ao exportar: {e}")


# create a registration system instance
registration_system = RegistrationSystem()
