from connection import session
from models import User
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

'''
user_data = {
    "user_id": 0,
    "name": 'hoek',
    "reg_date": '14.10.2023',
    "up_date": '14.10.2023'
}

userschema = UserSchema.parse_obj(user_data)

print(userschema)'''

# Создаем нового пользователя и сохраняем его в базе данных
def create():
    new_user = User(user_id=123,name='artemy',reg_date=12,up_date=17)
    session.add(new_user)
    session.commit()

# Получаем всех пользователей из базы данных
def read_all():
    users = session.query(User).all()
    print(users)

# Изменяем данные пользователя и сохраняем изменения в базе данных
def update():
    user_to_update = session.query(User).filter_by(name='artemy').first()
    user_to_update.id = 7878
    session.commit()

# Удаляем пользователя из базы данных
def dell():
    user_to_delete = session.query(User).filter_by(name='artemy').first()
    session.delete(user_to_delete)
    session.commit()

create()