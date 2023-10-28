import datetime

from db.connection import session
from db.models import User


def create(user_id, username):
    user1 = User(
        user_id=user_id,
        username=username,
        reg_date=datetime.date.today(),
        up_date=datetime.date.today(),
    )

    session.add(user1)
    session.commit()


def read():
    read_db = session.query(User.user_id, User.username).all()
    return read_db


def update(user_id, username):
    update_obj = session.query(User).filter_by(user_id=user_id).one()
    update_obj.username = username

    session.add(update_obj)
    session.commit()


def delete(user_id):
    delete_obj = session.query(User).filter_by(user_id=user_id).one()
    session.delete(delete_obj)
    session.commit()
