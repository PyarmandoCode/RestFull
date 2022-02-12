from pyexpat import model
from app import app

from app.models import Grupos
from flask_marshmallow import Marshmallow

ma= Marshmallow(app)


class GrupoSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Grupos
        fields=('codgrupo','nombre_grupo','estado')
        
        
grupo_serializer=GrupoSerializer()
grupos_schema=GrupoSerializer(many=True)
        