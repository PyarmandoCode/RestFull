from app import db

class Grupos(db.Model):
    codgrupo=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_grupo=db.Column(db.String(50))
    estado=db.Column(db.Integer)
    
    #todo crear constructor cuando se desea pasar valores
    #todo al servicio
    def __init__(self,nombre_grupo,estado):
        self.nombre_grupo=nombre_grupo
        self.estado=estado 
