
from flask import render_template,make_response,jsonify,request
from app import app,db
from app.models import Grupos
from app.serializer import grupos_schema,grupo_schema


@app.route('/')
def index():
    template_name="index.html"
    grupos=Grupos.query.all()
    return render_template(template_name,grupos=grupos)


#todo crear el endpoint para traer todas los grupos
#todo en formato JSON

@app.route("/listar_grupos",methods=["GET"])
def listar_grupos():
    #todo seleccionado todos los objetos de la clase grupos
    grupos=Grupos.query.all()
    #todo serializando y seleccionado los atributos a cast en json
    #todo dump nos permite serializar los objetos de PYTHON 
    result=grupos_schema.dump(grupos)
    
    #todo creando el documento de salida
    data={
        'message':'Todas mis grupos',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@app.route("/detalle_grupo/<int:id>",methods=["GET"])
def detalle_grupo(id):
    #todo para seleccionar solo un objeto por id
    grupo=Grupos.query.get(id)
    if grupo:
        #todo dump permite serializar los objetos en PYTHON
        #todo como por ejemplo convertir un STR en json
        result=grupo_schema.dump(grupo)        
        data= {
        'message':'1',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))

@app.route("/add_grupo",methods=["POST"])
def add_grupo():
    #todo request tomar los parametros qe se insertarn en
    #todo la tablas
    nombre_grupo=request.json['nombre_grupo']
    estado=request.json['estado']
    
    new_grupo = Grupos(nombre_grupo,estado)
    #todo se guarda el objeto en la session del usuario
    db.session.add(new_grupo)
    #todo se guarda fisicamente en la tabla
    db.session.commit()
    #todo esto permitira que el front vea cual es el registro
    #todo que se inserto
    result=grupo_schema.dump(new_grupo)
    
    data = {
        'message':'Se Agrego con exito',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))




    
    
    