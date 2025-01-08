searched_book = input()
books_count = 0
curr_book = input()
book_found = bool(False)
while curr_book != 'No More Books':
    if curr_book == searched_book:
        book_found = bool(True)
        break
    books_count += 1
    curr_book = input()

if book_found == bool(False):
    print('The book you search is not here!')
    print(f'You checked {books_count} books.')
else:
    print(f'You checked {books_count} books and found it.')