"""
add new book
get list of books with authors and number of books read

inputs:
add
get books
done

get list of books read
get list of authors
get number of books read
"""

books = {
    'book 1': 'author 1',
    'book 2': 'author 1',
    'book 3': 'author 2',
}


OPTIONS = (
    'add',
    'get books',
    'done',
)


def print_options():
    print('Your options are:')
    for option in OPTIONS:
        print(option.title())


request = ''
while request != 'done':
    print_options()
    request = input('What do you want to do?\t').lower()
    if request == 'add':
        new_book_title = input('What book title do you want to add?\t')
        new_book_author = input('What author wrote that book?\t')
        books[new_book_title] = new_book_author
        print('Book added!')
    elif request == 'get books':
        for book in books:
            print(f'{book}, {books[book]}')
        print(len(books))
