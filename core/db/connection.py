from sqlalchemy import create_engine, text, URL
from sqlalchemy.orm import sessionmaker
#from db.models import User

url_object = URL.create(
    "postgresql",
    username="postgres",
    password="artmy278",  # plain (unescaped) text
    host="localhost",
    database="db",
)

# engine = create_engine("postgresql://postgres:atemy278@localhost:5432/db")

#--------
#Не забывай коментить идиотина
#А то потом опять забудешь зачем всё это делал 💀💀💀
#--------


#Database access
engine = create_engine(url_object)

#Interactions with database
session = sessionmaker(
    bind=engine
)



#This function was created for connection testing
'''def check():
    client = session()
    try:
        result = client.execute(text('select 1'))
        for row in result:
                print(row)
    except Exception as eror:
        print(str(eror))

check()'''




