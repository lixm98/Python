# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # TODO: create a class method
    # 这是一个装饰器，告诉 Python：“下面这个方法不是给具体的‘书（实例）’用的，而是给‘书的模板（类）’用的。”
    @classmethod
    # cls 代表“我的种类”（Book 类本身，那个印刷模板）。
    def get_book_types(cls):
        return cls.BOOK_TYPES
    # TODO: create a static method
    def get_booklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("book type", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("title1","HARDCOVER")
b2 = Book("title1","PAPERBACK")

# TODO: Use the static method to access a singleton object
thebooks = Book.get_booklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)