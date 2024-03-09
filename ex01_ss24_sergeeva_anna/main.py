from person import Person
from datareader import DataReader

if __name__ == "__main__":
    owner = Person("Martha")
    dr = DataReader(owner)
    dr.load("data/books.csv", "data/pages.csv")
    dr.display()
