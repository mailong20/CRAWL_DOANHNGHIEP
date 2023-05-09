from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
salt = 'long'
engine = create_engine('mysql+pymysql://root:mailong2000@localhost:3306/facebook')
Session = sessionmaker(bind=engine)