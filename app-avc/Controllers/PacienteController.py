import services.database as db;
import models.Paciente as paciente;



def Incluir(paciente):
    db.cursor.execute("""""""""
            INSERT INTO Paciente (codigo_adm, nome, cpf, telefone, profissao, estado, cidade, bairro, rua, numero) 
            VALUES ('%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s')
    """"""""" % (paciente.codigo_adm, paciente.nome, paciente.cpf, paciente.telefone, paciente.profissao, paciente.estado, paciente.cidade, paciente.bairro, paciente.rua, paciente.numero))
    db.con.commit()


def Selecionar():
    db.cursor.execute("SELECT * FROM Paciente")
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

def Selecionarnome():
    db.cursor.execute("SELECT nome FROM paciente")
    recset = db.cursor.fetchall()
    costumerList = []
    for rec in recset:
        costumerList.append(rec)
    return costumerList

def Selecionarcpf():
    db.cursor.execute("SELECT nome, cpf FROM paciente")
    recset = db.cursor.fetchall()
    costumerList = []
    for rec in recset:
        costumerList.append(rec)
    return costumerList


def SelecionarId(cpf):
    db.cursor.execute("""""""""
         SELECT * FROM paciente WHERE cpf = '%s'
     """"""""" % (cpf))
    recset = db.cursor.fetchall()
    costumerList = []
    for rec in recset:
        costumerList.append(rec)
    return costumerList

def Alterar(nome, telefone, profissao, estado, cidade, bairro, rua, numero, codigo_p):
    db.cursor.execute("""""""""
        UPDATE paciente
        SET (nome, telefone, profissao, estado, cidade, bairro, rua, numero) = ('%s','%s','%s','%s','%s','%s','%s','%s') WHERE codigo_p = '%s'
     """"""""" % (nome, telefone, profissao, estado, cidade, bairro, rua, numero, codigo_p))
    db.con.commit()

import psycopg2

def verificar_cpf_existente(cpf):
    db.cursor.execute("SELECT cpf FROM paciente WHERE cpf = %s", (cpf,))
    cpf_existente = db.cursor.fetchone()
    if cpf_existente:
        return True
    else:
        return False


