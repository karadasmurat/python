from sqlalchemy import Table, ForeignKey
from collections import namedtuple
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import Optional, List
from sqlalchemy.sql.expression import select, func
import datetime

# declarative base class


class Base(DeclarativeBase):
    pass

# an example mapping using the base


"""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    phone_number TEXT,	-- User's primary phone number
    created_at TEXT DEFAULT CURRENT_TIMESTAMP -- ISO 8601 format
);
"""


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    full_name = mapped_column(sqlalchemy.types.String(50), nullable=False)
    phone_number = mapped_column(sqlalchemy.types.String)
    email: Mapped[str]  # type annotation alone, NOT NULL
    # you probably want to have all datetimes calculated by your DB server, rather than the application server.
    # func.current_date() vs func.current_timestamp()
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.current_timestamp())

    # reference to children. Note that this MUST be kept synchronized
    # Note - this info is NOT kept in parents table in db, only FK in the child table.
    contacts: Mapped[List["Contact"]] = relationship(back_populates="user")

    # how an object of this class should be printed
    # useful as an aid when debugging
    def __repr__(self) -> str:
        return f"User(id={self.user_id}, name={self.full_name})"


"""
CREATE TABLE contacts (
    contact_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL, -- FK
    title TEXT,
    phone_number TEXT,
    address TEXT,
    country TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
"""


class Contact(Base):

    __tablename__ = "contacts"
    contact_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[Optional[str]]
    phone_number: Mapped[Optional[str]]
    address: Mapped[str]
    country: Mapped[str]
    # FK: use the ForeignKey constraint when defining the column
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    # reference to parent
    # it's generally a good practice to include the referenced object
    user: Mapped["User"] = relationship(back_populates="contacts")

    def __repr__(self) -> str:
        return f"Contact(contact_id={self.contact_id}, country={self.country})"


# CREATE TABLE hogwarts_students(
#     student_id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     house_id INTEGER,
#     std_year INTEGER,
#     birthdate DATE,
#     gender TEXT,
#     patronus_form TEXT,
#     FOREIGN KEY(house_id) REFERENCES houses(house_id)
# );

class Wizard(Base):

    __tablename__ = "hogwarts_students"

    student_id = mapped_column(sqlalchemy.types.Integer, primary_key=True)
    first_name: Mapped[str]  # type annotation alone, NOT NULL
    last_name: Mapped[str]

    # use the ForeignKey constraint when defining the column
    house_id = mapped_column(ForeignKey("hogwarts_houses.house_id"))
    # it's generally a good practice to include the referenced object
    house: Mapped["House"] = relationship(back_populates="wizards")

    std_year: Mapped[int]
    birthdate: Mapped[str]
    gender: Mapped[str]
    patronus_form: Mapped[str]

    def __repr__(self) -> str:
        return f"Wizard(student_id={self.student_id}, last_name={self.last_name}), house_id={self.house_id}, house={self.house}"


# CREATE TABLE hogwarts_houses(
#     house_id INTEGER PRIMARY KEY,
#     name TEXT
# )
class House(Base):

    __tablename__ = "hogwarts_houses"

    house_id = mapped_column(sqlalchemy.types.Integer, primary_key=True)
    name: Mapped[str]  # type annotation alone, NOT NULL

    # parent side. Note that this should be synchronized
    # Note - this is not kept in db, only FK in the child table.
    wizards: Mapped[List["Wizard"]] = relationship(back_populates="house")

    def __repr__(self) -> str:
        return f"House(house_id={self.house_id}, name={self.name}"


# class Artist(Base):
#     __tablename__ = "Artist"


#     ArtistId = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#     Name = sqlalchemy.Column(sqlalchemy.String)
DB_PATH = "Users/mk/dev/db/sqlite/profile.db"

# Establishing Connectivity - the Engine
# The purpose of the Engine is to connect to the database by providing a Connection object
engine = sqlalchemy.create_engine("sqlite:////"+DB_PATH, echo=True)

Base.metadata.create_all(engine)

# Getting a Connection
# Committing Changes
# the DBAPI connection doesn’t commit automatically.
# with engine.connect() as conn:
#     conn.execute(sqlalchemy.text(
#         "CREATE TABLE IF NOT EXISTS wizards(wizard_id INTEGER PRIMARY KEY, name TEXT, house TEXT)"))
#     conn.execute(
#         sqlalchemy.text("INSERT INTO wizards (name, house) VALUES (:x, :y)"),
#         [{"x": "Harry", "y": "Gryffindor"}, {"x": "Ron", "y": "Gryffindor"}],
#     )

#     # Committing Changes
#     # the DBAPI connection doesn’t commit automatically.
#     conn.commit()


# Fetching Rows
# with engine.connect() as conn:
#     # running a textual SELECT statement
#     # The object returned is Result (CursorResult)
#     result = conn.execute(sqlalchemy.text("SELECT * FROM wizards"))
#     print(type(result))  # <class 'sqlalchemy.engine.cursor.CursorResult'>
#     for row in result:
#         print(row)
#         print(row.name)
#         print(row.house)

# Executing with an ORM Session
# Once you have the engine, you can use it to create a session and interact with the database:
# Session = sqlalchemy.orm.sessionmaker(bind=engine)
# with Session() as session:
#     # Now you can use the session object to perform database operations like adding, querying, and updating data.
#     # Query for all artists
#     # artists = session.query(Artist).all()
#     # for artist in artists:
#     #     print(artist.Name)

#     # Create an object and persist
# spongebob = User(name="spongebob", username="squarepants", title="Mr.")
# patrick = User(name="patrick", username="star", title="Mr.")

# session.add_all([spongebob, patrick])

# session.commit()

# Query: SELECT
Session = sqlalchemy.orm.sessionmaker(bind=engine)
with Session() as session:
    query0 = select(User)

    # SELECT users.name FROM users
    query1 = select(User.full_name)

    # Select.where()
    query2 = select(User).where(User.full_name == "patrick")

    # AND: Two or more filters can also be given as multiple arguments in a single where()
    # query3 = select(User).where(User.title == "Mr.", User.name == "patrick")

    # OR: or_() function vs Python | operator
    # SELECT users.id FROM users WHERE users.name = ? OR users.title = ?
    # query4 = select(User.id).where((User.name == "patrick") | (User.title == "Mr."))

    # ORDER BY
    # SELECT users.id, users.name FROM users ORDER BY users.name
    # query5 = select(User.id, User.name).order_by(User.name)

    # Aggregation Functions
    # query6 = select(Wizard)

    # SQL code associated with a SQLAlchemy query object can be seen when the query is printed
    print(query0)

    # Query execution
    # res = session.execute(query0) # Rows
    res = session.scalars(query0)   # Objects
    for user in res:
        print(user)
