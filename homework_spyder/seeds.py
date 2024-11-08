import json
from mongoengine import connect
from models import Author, Quote

# MongoDB connection
connect(
    db='homework',
    host='mongodb+srv://goitlearn:FvTP85uVCXJ8443r@cluster0.sdejq.mongodb.net/?retryWrites=true&w=majority'
)

def load_authors():
    with open('authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author(**author_data)
            author.save()
            print(f"Author {author.fullname} saved")

def load_quotes():
    authors_dict = {author.fullname: author for author in Author.objects()}
    
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data.pop('author')
            author = authors_dict.get(author_name)
            if author:
                quote = Quote(author=author, **quote_data)
                quote.save()
                print(f"Quote by {author_name} saved")
            else:
                print(f"Author {author_name} not found")

if __name__ == "__main__":
    load_authors()
    load_quotes()