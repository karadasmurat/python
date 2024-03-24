import json
from typing import List # type hints

class MenuItem:
    '''Wrap any class, with a text.
    If the wrapped object is str, then text will have an equal default value'''

    # MenuItem('Menu Item 1')           -> text = 'Menu Item 1'
    # MenuItem(object, 'Menu Item 2')   -> text = 'Menu Item 2' 
    def __init__(self, value: any, text="default"):
        self.value = value
        self.text = text if text != "default" else value

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def from_dict(cls, dict_obj):
        '''Deserialization - Like a named constructor. It takes a dict object, and returns constructor'''
        return cls(dict_obj['make'], dict_obj['model'], dict_obj['year'])

    def to_dict(self):
        '''Serialization - return a dict object representing this'''
        return {'make':self.make, 'model': self.model, 'year':self.year} 
    
    def to_JSON_str(self):
        '''return a JSON string representation of this object 
        by converting it to a dictionary and then dumping to string'''
        return json.dumps(self.to_dict())
    
    # Called by str(object) and the built-in functions format() and print() 
    # to compute the “informal” or nicely printable string representation of an object.
    def __str__(self):
        return f"Car(make={self.make!r}, model={self.model!r}, year={self.year})" 

SQL_CREATE_TABLE_AUTHOR = """CREATE TABLE IF NOT EXISTS Author (
    AuthorID INTEGER NOT NULL,
    FullName TEXT NOT NULL,
    PRIMARY KEY(AuthorID AUTOINCREMENT));"""

SQL_INSERT_AUTHOR = "INSERT INTO Author(FullName) VALUES(?);"

class Author:
    def __init__(self, fullname: str): 
        self.fullname = fullname

    @classmethod
    def from_dict(cls, dict_obj):
        '''Deserialization - Like a named constructor. It takes a dict object, and returns constructor'''
        return cls(dict_obj['fullname'])
    
    def to_dict(self):
        '''Serialization - return a dict object representing this'''
        return {'fullname':self.fullname} 
    
    def __str__(self):
        return f"Author(fullname={self.fullname!r})"

SQL_CREATE_TABLE_BOOK = """CREATE TABLE IF NOT EXISTS Book (
    BookID INTEGER NOT NULL,
    Title TEXT NOT NULL,
    AuthorID INTEGER NOT NULL,
    ISBN INTEGER,
    PRIMARY KEY(BookID AUTOINCREMENT)
    FOREIGN KEY (AuthorID) REFERENCES Department(DEPARTMENT_ID));"""

SQL_INSERT_BOOK = "INSERT INTO Book(Title, AuthorID, ISBN) VALUES(?, ?, ?);"
class Book:
    # type hints: from typing import List
    # def __init__(self, title, authors, year, publisher):
    # def __init__(self, title: str, authors: List[str]):
    def __init__(self, title: str, author: Author, ISBN: str, genres: List[str]):    # single author, multi-genre
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genres = genres    # List[str]
        self.hardcover = False  # default value, not in the constructor parameter list
        self.year = 0


    @classmethod
    def from_dict(cls, dict_obj):
        '''Deserialization - Like a named constructor. It takes a dict object, and returns constructor'''
         # Note that author is of type Author, so it is explicitly deserialized with from_dict()
        author = Author.from_dict(dict_obj['author'])   # Note that author is a user defined type
        return cls(dict_obj['title'], author, dict_obj['ISBN'], dict_obj['genres'])
    
    def to_dict(self):
        '''Serialization - return a dict object representing this'''
        # Note that author is of type Author, so it is explicitly serialized with to_dict()
        return {'title':self.title, 'author': self.author.to_dict(), 'ISBN': self.ISBN, 'genres':self.genres} 

    def __str__(self):
        # Note that author also has a __str__() method, which is called implicitly
        return f"Book(title={self.title!r}, author={self.author}, ISBN={self.ISBN}, Genres={self.genres})"
    
    # Container’s __str__ uses contained objects’ __repr__
    def __repr__(self):
        return self.__str__()

class Department:

    def __init__(self, name: str):
        self.name = name
        self.id = -1         # default id, will be assigned by database.

    def __str__(self):
        # note !r
        return f"Department(id={self.id} name={self.name!r})"   # Department(id=1 name='Technology')
    
    # Container’s __str__ uses contained objects’ __repr__
    def __repr__(self):
        # In this case, __str__ is not a user friendly string, but does what __repr__ is supposed to do, so just redirect
        return self.__str__()  

    
class Employee:

    def __init__(self, lastname: str, salary: float, department: Department):
        self.lastname = lastname
        self.salary = salary
        self.department = department    # instance of Department    
        self.id = -1                    # default id, will be assigned by database.

    def __str__(self):
        return f"Employee(id={self.id}, lastname={self.lastname!r}, salary={self.salary}, department={self.department})"
    
    # Container’s __str__ uses contained objects’ __repr__
    def __repr__(self):
        return self.__str__()
    
class HogwartsStudent:

    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house

    def to_csv(self):
        return self.name + "," + self.house
    
    def __str__(self):
        return f"Student(name={self.name!r}, house={self.house!r}" 
    
class HogwartsHouse:

    def __init__(self, name: str, mascot: str):
        self.name = name
        self.mascot = mascot

    @classmethod
    def from_dict(cls, dict_obj):
        '''Deserialization - Like a named constructor. It takes a dict object, and returns constructor'''
        return cls(dict_obj['name'], dict_obj['mascot'])

    def __str__(self):
        return f"House(name={self.name!r}, mascot: {self.mascot!r}" 