import services.database as db;
import models.Base as base


def Atualiza(base):
    db.cursor.execute("""""""""
            INSERT INTO Base (SUPSYS16, SUPDIA16, DIABETES, BMI, FHSTK, BEAT14, HEAR01, NERV01, DIAG01, 
                                HEART01, GEND01, SMOKE, DIZZYP07, FATIGP07, RECOGN08, CHSTPN07, LEGWLK07, PALPIP07, 
                                CONVER08, LIFTNG09, STRKBASE) 
            VALUES ('%d', '%d',  '%d', '%f', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d','%d', '%d', '%d', '%d', '%d', '%d', '%d')
    """"""""" % (base.SUPSYS16, base.SUPDIA16, base.DIABETES, base.BMI, base.FHSTK, base.BEAT14,
                 base.HEAR01, base.NERV01, base.DIAG01, base.HEART01, base.GEND01, base.SMOKE,
                 base.DIZZYP07, base.FATIGP07, base.RECOGN08, base.CHSTPN07, base.LEGWLK07,
                 base.PALPIP07, base.CONVER08, base.LIFTNG09, base.STRKBASE))
    db.con.commit()

def RecuperaBase():
    db.cursor.execute("SELECT * FROM Base")
    recset = db.cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows