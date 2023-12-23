import datetime
import pytz
from db.connection import session
from db.models import User, Orders
from db.queries import get_user_query, get_order_query
from yoomoney import Quickpay


def create(user_id, username):
    user1 = User(
        user_id=user_id,
        username=username,
        reg_date=datetime.date.today(),
        up_date=datetime.date.today(),
    )

    session.add(user1)
    session.commit()

def create_order(rand_string ,user_id):
    new_order = Orders(
        user_id=user_id,
        order_title=rand_string,
    )

    session.add(new_order)
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

def id_finder(an_user_id):
    parts = session.query(User).filter(User.user_id==an_user_id).first()
    return parts

def get_user(chat_id: str):
    query = get_user_query(chat_id)
    user = session.execute(query)
    data = user.first()
    return data

def get_order(user_id: int):
    try:
        query = get_order_query(user_id)
        order = session.execute(query)
        data = order.scalars().first()
        return data
    except Exception as ex:
        print(ex)
        return None

def make_order_paid(order):
    order.status = "PAID"
    session.commit()
    session.refresh(order)

def plus_month(user):
    now = datetime.date.today()
    user_end_date = user.up_date
    if user_end_date < now:
        end = now + datetime.timedelta(days=31)
    else:
        end = user_end_date + datetime.timedelta(days=31)
    user.up_date = end
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_all_user_id():
    all_user_id = session.query(User.user_id).all()
    return all_user_id


def create_payment(rand_string):
    quickpay = Quickpay(
        receiver="4100118429702668",
        targets="tg_try1_bot",
        quickpay_form="shop",
        paymentType="SB",
        sum=2,
        label=rand_string
    )
    return quickpay
