def create_books_2d_list(file_name):

    file = open(file_name).read().splitlines()
    an=[]
    date=[]

    for book in file:
        book=book.split("\t")
        name=book[0].strip()
        author=book[1].strip()
        publisher=book[2].strip()
        date=book[3].strip()

        date=date.split("/")

        day=date[0]
        month=date[1]
        year=date[2]

        findate=year+"-"+month+"-"+day
        date=findate
        genre=book[4].strip()
        
        an.append([date, name, author, publisher, genre])
    return an

def search_by_year(books,year1,year2):

    box=[]
    something = False

    for i in range(year1,year2+1):
        for j in range(len(books)):
            year=books[j][0].split("-")
            if i == int(year[0]):
                box.append(books[j])
                something = True

    print("\nAll titles between ", year1 , " and " , year2 ,":\n")
    if (something == False):
        print("No books found in that range of years")
    else:
        for i in range(0,len(box)):
            print(box[i][1] + ", by "+box[i][2]+" ("+box[i][0]+")")

# testing
# books = create_books_2d_list("NYT_short.txt")
# print(books)

# search_by_year(books,1999,2001)
# search_by_year(books,2050,2060)