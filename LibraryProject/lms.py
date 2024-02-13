class Library:
    def show_menu(self):
        print("\n*** Menu ***")
        print("1. List Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("q. Quit")
        print("************")
        print("Enter your choice: ",end=" ") 
        choice = input()
        return choice

    def add_book_panel(self):
        print("Enter the book title: ",end=" ")
        title = input().capitalize()
        print("Enter the author: ",end=" ")
        author = input().capitalize()
        year = ""
        while not year.isdigit():
           print("Enter the release year: ", end=" ")
           year = input()
           if not year.isdigit():
               print("Invalid input. Please enter a valid year.")
        pages = ""
        while not pages.isdigit():
           print("Enter the number of pages: ", end=" ")
           pages = input()
           if not pages.isdigit():
               print("Invalid input. Please enter a valid number of pages.")
        return title, author, year, pages

    def add_book(self):
        book_title, book_author, book_year, book_pages = self.add_book_panel()
        with open("books.txt", "a") as file:
            file.writelines(f'{book_title},{book_author},{book_year},{book_pages}\n')
        print(f"Book {book_title} added successfully")

    def list_books(self):
        print("\n************")
        with open("books.txt", "r") as file:
            for line in file:
                 parts = line.strip().split(',')
                 if len(parts) == 4:
                    title, author, year, pages = parts
                    print(f"Book: {title}, Author: {author}")
        print("************")

    def remove_book(self):
        print("Enter the book title to remove: ",end=" ")
        title = input().capitalize()
        with open("books.txt", "r") as file:
            books = file.readlines()
        with open("books.txt", "w") as file:
           for book in books:
               if book.strip() and book!= book.split(',')[0] != title:
                   file.write(book)
        print(f"Book {title} removed successfully")

def main():
    lib =  Library()
    while True:
        choice = lib.show_menu()
        if choice == "1":
            lib.list_books()
        elif choice == "2":
             lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "q":
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()