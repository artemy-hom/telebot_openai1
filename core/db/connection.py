from sqlalchemy import create_engine, text, URL, Date
from sqlalchemy.orm import sessionmaker, query
from db.models import User
import datetime

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
Session = sessionmaker(
    bind=engine
)
session = Session()



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

def create(user_id, username):
    user1 = User(
        user_id = user_id,
        username = username,
        reg_date = datetime.date.today(),
        up_date = datetime.date.today()
    )


    session.add(user1)
    session.commit()

def read():
    read_db = session.query(User.user_id, User.username).all()
    return read_db

def update(user_id, username):
    update_obj = session.query(User).filter_by(user_id = user_id).one()
    update_obj.username = username


    session.add(update_obj)
    session.commit()

def delete(user_id):
    delete_obj = session.query(User).filter_by(user_id = user_id).one()
    session.delete(delete_obj)
    session.commit()
