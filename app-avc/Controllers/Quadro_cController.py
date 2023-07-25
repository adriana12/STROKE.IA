import services.database as db;
import models.Quadro_c as quadro_c;
import models.Paciente as paciente;

def Incluir(quadro_c):
    db.cursor.execute("""""""""
            INSERT INTO Quadro_c (codigo_adm, cpf, data_AT, peso, altura, idade, glicose, SUPSYS16, SUPDIA16,  
                                    DIABETES, BMI, FHSTK, BEAT14, HEAR01, NERV01, DIAG01, HEART01, GEND01, SMOKE,
                                    DIZZYP07, FATIGP07, RECOGN08, CHSTPN07, LEGWLK07, PALPIP07, CONVER08, LIFTNG09, 
                                    STRKBASE, proba_AVC) 
            VALUES ('%s','%s','%s','%f', '%f', '%d', '%f', '%d', '%d', '%d', '%f', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d','%f')
    """"""""" % (quadro_c.codigo_adm, quadro_c.cpf, quadro_c.data_AT, quadro_c.peso, quadro_c.altura, quadro_c.idade, quadro_c.glicose,
                 quadro_c.SUPSYS16, quadro_c.SUPDIA16, quadro_c.DIABETES, quadro_c.BMI, quadro_c.FHSTK, quadro_c.BEAT14,
                 quadro_c.HEAR01, quadro_c.NERV01, quadro_c.DIAG01, quadro_c.HEART01, quadro_c.GEND01, quadro_c.SMOKE,
                  quadro_c.DIZZYP07, quadro_c.FATIGP07, quadro_c.RECOGN08, quadro_c.CHSTPN07, quadro_c.LEGWLK07,
                 quadro_c.PALPIP07, quadro_c.CONVER08, quadro_c.LIFTNG09, quadro_c.STRKBASE, quadro_c.proba_AVC))
    db.con.commit()


def SelecionarQC():
    db.cursor.execute("SELECT data_AT, STRKBASE, idade, proba_AVC FROM Quadro_c")
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

def SelecionarDAT():
    db.cursor.execute("SELECT data_AT FROM Quadro_c")
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows


def Selecionar():
    db.cursor.execute("SELECT * FROM Quadro_c")
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows


def SelecionarProba():
    db.cursor.execute("SELECT proba_AVC FROM Quadro_c")
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

def SelecionarId(cpf):
    db.cursor.execute("select nome, SUPSYS16, SUPDIA16, DIABETES, BMI, FHSTK, BEAT14, HEAR01, NERV01, DIAG01, HEART01, GEND01, SMOKE,"
                      "	DIZZYP07, FATIGP07, RECOGN08, CHSTPN07, LEGWLK07, PALPIP07, CONVER08, LIFTNG09"
                      "proba_AVC from Quadro_c natural join Paciente where cpf = '%s'" % (cpf))
    recset = db.cursor.fetchall()
    costumerList = []
    for rec in recset:
        costumerList.append(rec)
    return costumerList

def retornar_dados_paciente(cpf):
    db.cursor.execute("""""""""
         SELECT data_AT, STRKBASE, idade, proba_AVC FROM Quadro_c WHERE cpf = '%s'
     """"""""" % (cpf))
    recset = db.cursor.fetchall()
    costumerList = []
    for rec in recset:
        costumerList.append(rec)
    return costumerList

