import re
import sqlite3
from tkinter import messagebox, Tk, Button
from banco import RegistrationSystem


class Validacao:

    @staticmethod
    def tratar_dados(dado):
        return re.sub(r"[\s\-_,\"\'\*\.\!\?\;\:\(\)\[\]\{\}\<\>\|\\\/]", "", dado)

    @staticmethod
    def tratarCPF(cpf):
        return Validacao.tratar_dados(cpf)

    @staticmethod
    def tratarRG(rg):
        return Validacao.tratar_dados(rg)

    @staticmethod
    def tratarCEP(cep):
        return Validacao.tratar_dados(cep)

    @staticmethod
    def tratarTelefone_e_Celular(telefone):
        return Validacao.tratar_dados(telefone)

    @staticmethod
    def validarSexo(sexo):
        return sexo in ["M", "F"]

    @staticmethod
    def validarCPF(cpf):
        cpf = Validacao.tratarCPF(cpf)
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        return True

    @staticmethod
    def validarRG(rg):
        rg = Validacao.tratarRG(rg)
        if len(rg) < 7 or len(rg) > 14 or not rg.isdigit():
            return False
        return True

    @staticmethod
    def validarCEP(cep):
        cep = Validacao.tratarCEP(cep)
        if len(cep) != 8 or not cep.isdigit():
            return False
        return True

    @staticmethod
    def validarNome(nome):
        if not nome or not nome.replace(" ", "").isalpha():
            return False
        return True

    @staticmethod
    def validarEmail(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

    @staticmethod
    def validarTelefone_e_Celular(telefone):
        telefone = Validacao.tratarTelefone_e_Celular(telefone)
        if len(telefone) not in [10, 11] or not telefone.isdigit():
            return False
        return True

    @staticmethod
    def validarUF(uf):
        uf = Validacao.tratarUF(uf).upper()
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE",
                   "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        return uf in estados

    @staticmethod
    def validarIdade(idade):
        return idade.isdigit() and 0 <= int(idade) <= 120

    @staticmethod
    def verificarCampo(campo):
        return campo.strip() != ""




registration_system = RegistrationSystem()



