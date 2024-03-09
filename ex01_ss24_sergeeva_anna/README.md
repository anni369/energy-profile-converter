# Homework 01

Download or clone the project to your local PC.

> TIP: With [`git clone`](https://www.git-scm.com/docs/git-clone) you can define the name of the destination directory. Per default, the name of the remote-repository is used.

```console
$ git clone https://git-iit.fh-joanneum.at/swd23-sodevel2/homeworks/ex01_ss24_lastname_firstname.git
```

> **Attention:** When you Download the repository as ZIP, you have to initialize a new git-repository!  
> Do NOT push your changes back to the [original remote repository](https://git-iit.fh-joanneum.at/swd23-sodevel2/homeworks/ex01_ss24_lastname_firstname)!

**Also using `git` _(locally)_ is part of this assignment! Create at least after each class you created/implemented a commit with an appropriate message. Feel free to do as many commits as you want. Don't forget to do a final commit!**

## Part1: 12 Points

Create the following classes by interpreting the UML diagrams.

```plantuml
class Bookshelf {
  -books: Book[*]
  -owner: Person
  +<<create>> init(o: Person)
  +getBooks(): Book[]
  +addBook(b: Book): None
  +removeBook(title: str): Book
}
class Book {
  -pages: Page[1..*]
  -title: string
  -author: Person
  +<<create>> init(p: Page[], t: string, a: Person)
  +getAuthor(): Person
  +getPages(): Page[]
  +getTitle(): string
}
class Page {
  -content: string
  +<<create>> init(c: string)
  +getContent(): string
  +setContent(c: string)
}
note right: you should not be able\n to set an empty content
class Person {
  -name: string
  +<<create>> init(n: string)
  +getName(): string
}
Bookshelf o-- "*" Book: books
Book *-- "1..*" Page: pages
Book o-- "1" Person: author
Bookshelf o-- "1" Person: owner
```

> In this class diagrams, you find on each class an `init`-method, prepend with `<<create>>`. This stands for the `constructor` method. Keep to the parameter list of the `init`-method in the diagram on your implementation! The names of the parameter in the methods only have one letter because or reasons of space.  
> To get all points, stick to the conventions and typical way to implement classes in Python! Use the manuscript (moodle/gitlab) as reference!

### Person

Find the [Person](person.py) class as an example already implemented.

### Page (2 points)

A `Page` is a representation of a page in a book. It simple has a `content` that should be able to _set_ and _get_. It should **not** be able to set an empty page! In such case, an `Exception` should be raised!

### Book (4 points)

A `Book` is a representation of a book, containing `pages` (_at least one!_),  has a `title` and an `author`. The properties of the `Book` class should be **readonly**. Because a book without pages makes no sense, an `Exception` should be raised, when someone tries to create such a book.

### Bookshelf (6 points)

A `Bookshelf` is a representation of a bookshelf, with an `owner` and some `books` in it. A `Bookshelf` may contain no books. While the getter of `books` simple returns a "listing" of the available books, you should be able to **add** new books to the shelf with the `add_book` method (_one by one_) and **remove** books from it with the `remove_book` method by its title. This method also `return`s the removed book.

- Adding a book means, it is now part of the collection of books of this shelf.
- Removing a book means, it is no longer part of the collection of books of this shelf.
  - Removing a book, that is not part of the shelf should raise an `Exception`
  - Identify a book by it's `title` to remove it

> **How could you useful test your implementation?** Simple create in each file a `if __name__ == '__main__':` block and inside of it, create objects/run code to check if your implementation works. That way, you can simple implement and manually test each class on it's one, simple execute `python3 person.py` directly. When you `import Person`, that code would not be executed!

## Part2 (Bonus): 3 Points

Create a `DataReader` class that could read the given [CSV files](data) (the columns are delimited by `;` (semicolon)).

> You can use the [CSV module](https://docs.python.org/3/library/csv.html#module-csv) or simple [`readlines()`](https://docs.python.org/3/tutorial/inputoutput.html#tut-files) and [`split(';')`](https://docs.python.org/3/library/stdtypes.html?highlight=str%20split#str.split) the given data up your self.


```plantuml
class DataReader {
  -owner: Person
  -bookshelf: Bookshelf
  +<<create>> init(o: Person)
  +load(files: string[1..*]) -> None
  +display() -> None
}
```

The `load`-Method of the `DataReader` should read the given `files` and create a `Bookshelf` of it's content. (_[books.csv](data/books.csv) contains the book information, [pages.csv](data/pages.csv) contain the "pages" of the books_).
The `display`-Method should print out the information about the bookshelf. The output could look like the following.

```text
--- Martha's Bookshelf ---
> The Hitchhiker's Guide to the Galaxy by Douglas Adams with 6 pages.
> Nineteen Eighty-Four by George Orwell with 4 pages.
> The Hobbit by J.R.R. Tolkien with 3 pages.
```

You can use the provided [main.py](main.py) that already contains code that will create such bookshelf with an datareader. It is on you to implement the datareader to work with the code.

> _PS: This **Bonus** part will you enable to gather additional points. **However**, the time and effort required is not in any way related to the possible points!_

---

## HINTS

- create each class in a separate file - therefore use the provided (empty) files in this repository
- which values has to be set via constructor, which could be created directly from the class itself?
- use git and make useful commits
- keep on the conventions Python provides for encapsulation
- use decorators to create getters and setters and name them relating to Pythons convention
- when an `Exception` should be raised, simple use the generic [Exception](https://docs.python.org/3/library/exceptions.html#Exception), do not use a specific Error/Exception!
- **REMOVE all `# TODO` comments after they are done!**

## CoC - Code of Conduct

- When you use code that you found on the internet (_e.g. Stack Overflow or ChatGPT_), identify it with the link to the origin as comment! **BUT** - only use such code when you understand what it does!
  - Code that is simple generated using an AI like ChatGPT will be considered as plagiarism and will be graded with 0 points accordingly!
  - The same applies to copies of similar exercises from the internet!
- **Only use build in functions that we have discussed in class (1st and 2nd semester) so far (`print`, `input`, `...`). Variables, `if`/`else` statements, `loops` and `list`s. `class`es etc. Do not use any unknown functions that you might find on the internet! Do not use imports with the exception of `import sys` and `import random` or `import math` (if needed), as well as `import`s of your own modules. Create your own functions and classes or use at least the provided functions and classes from the template.**
- When you do the exercise as group, add a comment at the beginning of your code with the members that worked together. Generally, homework is considered as individual work! Expect to get fewer points for a working solution! **BUT** - if a "copied"/"collaborate" work will be identified that is not marked as that, 0 points will be granted! Everyone has to submit the solution on Moodle individually!
- Your solution has to run as expected (_see description above_). You're welcome to add additional functionality, but that will not lead to additional points!
- You are not sure about your code or have explicit questions about alternatives? Add a comment in the format `# Q: <Your question>` and I will try to answer them in the review. Otherwise, I may oversee such questions! e.g.:

  ```python
  x = "something" # Q: Wie könnte ich das anders lösen?
  ```

Assign the project folder, following the name schema **ex01_ss24_\<YOUR-LASTNAME\>_\<YOUR-FIRSTNAME\>**, containing your whole solution (_including .git repository!_) as ZIP. The ZIP to assign has to follow the same naming schema: **ex01_ss24_\<YOUR-LASTNAME\>_\<YOUR-FIRSTNAME\>.zip**, e.g. **ex01_ss24_schwab_harald.zip**.

> _If the assignment does not follow the naming scheme there will be a point reduction!_

```tree
ex01_ss24_schwab_harald.zip
└── ex01_ss24_schwab_harald
    ├── .git
    │   └── ...
    ├── data
    ├── book.py
    ├── bookshelf.py
    ├── ...
    ├── page.py
    └── person.py
```

**Assignments without a git-repository containing some commits will result in 30% loss of possible points!**
