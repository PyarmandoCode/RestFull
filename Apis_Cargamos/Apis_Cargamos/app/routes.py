from flask import render_template,make_response,jsonify
from app import app,db
from app.models import Grupos
from app.serializer import grupos_schema,grupo_schema
from flask import request

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
    




    
    
    