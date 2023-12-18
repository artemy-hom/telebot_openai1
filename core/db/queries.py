import datetime
from sqlalchemy import Insert, insert, select, and_
from .models import User, Orders

def get_user_query(chat_id):
    query = select(User).where(User.user_id == chat_id)
    return query

def get_order_query(user_id):
    query = select(Orders).where(Orders.user_id == user_id).order_by(Orders.id.desc())
    return query