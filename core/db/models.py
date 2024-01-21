import datetime
from sqlalchemy import ForeignKey, String, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import BigInteger

Base = declarative_base()


# Table with users in it
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    # Telegram unique user id
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, unique=True)
    # Telegram user name
    username: Mapped[str] = mapped_column(String(30))
    # Register date
    reg_date: Mapped[DATE] = mapped_column(DATE, default=datetime.date.today())
    # Last update date
    up_date: Mapped[DATE] = mapped_column(DATE, onupdate=datetime.date.today())

    # Just debug function
    def __str__(self) -> str:
        return f"<User:{self.user_id}"


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    order_title: Mapped[str] = mapped_column(String(length=255), nullable=False)
    order_date: Mapped[DATE] = mapped_column(DATE, default=datetime.datetime.now())
    status: Mapped[str] = mapped_column(String(length=255), default="PENDING")
