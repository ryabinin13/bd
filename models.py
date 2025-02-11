from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date

class Base(DeclarativeBase): pass

class Genre(Base):
    __tablename__ = "genre"
 
    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str]

class Author(Base):
    __tablename__ = "author"
 
    author_id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str]

class City(Base):
    __tablename__ = "city"
 
    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str]
    days_delivery: Mapped[int]

class Book(Base):
    __tablename__ = "book"
 
    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.author_id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.genre_id"))
    price: Mapped[float]
    amount: Mapped[int]

class Client(Base):
    __tablename__ = "client"
 
    client_id: Mapped[int] = mapped_column(primary_key=True)
    name_client: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.city_id"))
    email: Mapped[str]

class Buy(Base):
    __tablename__ = "buy"
 
    buy_id: Mapped[int] = mapped_column(primary_key=True)
    buy_description: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("client.client_id"))

class Step(Base):
    __tablename__ = "step"
 
    step_id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str]

class BuyBook(Base):
    __tablename__ = "buy_book"
 
    buy_book_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("book.book_id"))
    amount: Mapped[int]

class BuyStep(Base):
    __tablename__ = "buy_step"
 
    buy_step_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"))
    date_step_beg: Mapped[date]
    date_step_end: Mapped[date]