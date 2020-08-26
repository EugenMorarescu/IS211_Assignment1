class Book:
    author=""
    title=""
    
    def __init__(self,author,title):
        self.author=author
        self.title=title
    def Display(self):
        print(self.author + " Written by " + self.title)
        
book1 = Book("Of Mice and Men","John Steinbeck")
book2 = Book("To Kill a Mockingbird","Harper Lee")

book1.Display()
book2.Display()