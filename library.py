# Initialize the library's books collection
books = {
    "Fiction": {
        "Thriller": {
            "The Girl on the Train": {
                "author": "Paula Hawkins",
                "year": 2015,
                "pages": 328,
                "available": True
            },
            "Gone Girl": {
                "author": "Gillian Flynn",
                "year": 2012,
                "pages": 432,
                "available": False
            }
        },
        "Romance": {
            "The Notebook": {
                "author": "Nicholas Sparks",
                "year": 1996,
                "pages": 214,
                "available": True
            },
            "The Fault in Our Stars": {
                "author": "John Green",
                "year": 2012,
                "pages": 313,
                "available": True
            }
        }
    },
    "Non-Fiction": {
        "Science": {
            "A Brief History of Time": {
                "author": "Stephen Hawking",
                "year": 1988,
                "pages": 198,
                "available": False
            },
            "The Selfish Gene": {
                "author": "Richard Dawkins",
                "year": 1976,
                "pages": 308,
                "available": True
            }
        },
        "Business": {
            "Good to Great": {
                "author": "Jim Collins",
                "year": 2001,
                "pages": 312,
                "available": True
            },
            "The Lean Startup": {
                "author": "Eric Ries",
                "year": 2011,
                "pages": 272,
                "available": False
            }
        }
    }
}

# Function to search for a book
def search_book(title):
    for genre in books.keys():
        for sub_genre in books[genre].keys():
            for book in books[genre][sub_genre].keys():
                if book == title:
                    return books[genre][sub_genre][book]
    return "Book not found"

# Function to check the availability of a book
def check_availability(title):
    book_info = search_book(title)
    if book_info == "Book not found":
        return book_info
    else:
        return book_info["available"]

# Function to check out a book
def check_out(title):
    book_info = search_book(title)
    if book_info == "Book not found":
        return book
    elif book_info["available"] == False:
        return "Book not available"
    else: 
        books[genre][sub_genre][title]["available"] = False
        return "Book checked out successfully"

def check_in(title):
book_info = search_book(title)
if book_info == "Book not found":
return book_info
elif book_info["available"] == True:
return "Book already available"
else:
books[genre][sub_genre][title]["available"] = True
return "Book checked in successfully"

print(search_book("The Girl on the Train"))


# Function to add a book
def add_book(title, author, year, pages, genre, sub_genre):
    if genre not in books.keys():
        books[genre] = {}
    if sub_genre not in books[genre].keys():
        books[genre][sub_genre] = {}
    books[genre][sub_genre][title] = {
        "author": author,
        "year": year,
        "pages": pages,
        "available": True
    }
    return "Book added successfully"

# Test the function
print(add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, 309, "Fiction", "Fantasy"))
# Output: "Book added successfully"

print(books)
# Output: { "Fiction": { "Thriller": { ... }, "Romance": { ... }, "Fantasy": { "Harry Potter and the Sorcerer's Stone": { "author": "J.K. Rowling", "year": 1997, "pages": 309, "available": True } } }, "Non-Fiction": { ... } }




# Function to print all books in nested list format
def print_all_books():
    books_list = []
    for genre, sub_genres in books.items():
        for sub_genre, titles in sub_genres.items():
            for title, book_info in titles.items():
                if book_info["available"]:
                    books_list.append([title, book_info["author"], book_info["year"], book_info["pages"]])
    return books_list

# Test the function
print(print_all_books())
# Output: [["The Notebook", "Nicholas Sparks", 1996, 214], ["The Fault in Our Stars", "John Green", 2012, 313], ["The Selfish Gene", "Richard Dawkins", 1976, 308], ["Good to Great", "Jim Collins", 2001, 312]]

