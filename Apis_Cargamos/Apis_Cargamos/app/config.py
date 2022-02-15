#pip install psycopg2-binary
class Config(object):
    #todo conectado a la base de datos de MYSQL
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bdcargamos'
    
    #todo conectand a la base de datos de POSTGRESS modificado el dialecto
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:rioazulq12@localhost:5432/bdcargamos'
    SQLALCHEMY_DATABASE_URI = 'postgresql://diyxzlwffdlmos:12a6f68c61bb4a5885a574cc2aab95c2d35d0af89b82e2455ea33da38b111351@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d7c9o55evbgsl5'
    SQLALCHEMY_TRACK_MODIFICATIONS = True