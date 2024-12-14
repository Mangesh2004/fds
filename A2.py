# Function to delete duplicate books
def delete_duplicates(books):
    unique_books = []
    for book in books:
        if book not in unique_books:
            unique_books.append(book)
    return unique_books

# Function to display books in ascending order of cost
def display_sorted_books(books):
    sorted_books = sorted(books, key=lambda x: x[1])
    print("\nBooks in ascending order of cost:")
    for book in sorted_books:
        print(f"Title: {book[0]}, Cost: ${book[1]}")

# Function to count books with cost more than 500
def count_expensive_books(books):
    count = 0
    for book in books:
        if book[1] > 500:
            count += 1
    print(f"\nNumber of books with cost more than $500: {count}")

# Function to create new list of books with cost less than 500
def copy_cheap_books(books):
    cheap_books = []
    for book in books:
        if book[1] < 500:
            cheap_books.append(book)
    print("\nBooks with cost less than $500:")
    for book in cheap_books:
        print(f"Title: {book[0]}, Cost: ${book[1]}")
    return cheap_books

# Main program
n = int(input("Enter the number of books: "))

# Create empty list to store books
books = []

# Input book details
for i in range(n):
    print(f"\nEnter details for book {i+1}")
    title = input("Enter book title: ")
    cost = float(input("Enter book cost: $"))
    books.append((title, cost))

# Menu driven program
while True:
    print("\n=== Library Management System ===")
    print("1. Delete duplicate entries")
    print("2. Display books in ascending order of cost")
    print("3. Count books with cost more than $500")
    print("4. Copy books with cost less than $500")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        books = delete_duplicates(books)
        print("Duplicates removed successfully!")
    
    elif choice == '2':
        display_sorted_books(books)
    
    elif choice == '3':
        count_expensive_books(books)
    
    elif choice == '4':
        copy_cheap_books(books)
    
    elif choice == '5':
        print("Thank you for using the Library Management System!")
        break
    
    else:
        print("Invalid choice! Please try again.")