
class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"[{self.uid}] {self.title} ({self.year})"

    def __eq__(self, other):
        return isinstance(other, ArchiveItem) and self.uid == other.uid

    def is_recent(self, n):
        current_year = 2025
        return (current_year - self.year) <= n


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book [{self.uid}] '{self.title}' by {self.author}, {self.year}, {self.pages} pages"


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article [{self.uid}] '{self.title}' in {self.journal}, {self.year}, DOI: {self.doi}"


class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f"Podcast [{self.uid}] '{self.title}' hosted by {self.host}, {self.year}, {self.duration} min"


def save_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            if isinstance(item, Book):
                line = f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n"
            elif isinstance(item, Article):
                line = f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n"
            elif isinstance(item, Podcast):
                line = f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n"
            else:
                continue
            file.write(line)


def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            type_ = parts[0]
            uid = parts[1]
            title = parts[2]
            year = int(parts[3])

            if type_ == "Book":
                author = parts[4]
                pages = int(parts[5])
                items.append(Book(uid, title, year, author, pages))
            elif type_ == "Article":
                journal = parts[4]
                doi = parts[5]
                items.append(Article(uid, title, year, journal, doi))
            elif type_ == "Podcast":
                host = parts[4]
                duration = int(parts[5])
                items.append(Podcast(uid, title, year, host, duration))
    return items



items = [
    Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
    Book("B002", "AI Basics", 2022, "Alice Johnson", 320),
    Article("A001", "Neural Networks", 2019, "AI Journal", "10.1234/nn5678"),
    Article("A002", "Quantum Computing", 2023, "Physics World", "10.5678/qc1234"),
    Podcast("P001", "TechTalk", 2020, "Jane Doe", 45),
    Podcast("P002", "Science Daily", 2024, "John Smith", 60)
]


save_to_file(items, "archive.txt")


loaded_items = load_from_file("archive.txt")


print(" Loaded Archive Items:\n")
for item in loaded_items:
    print(item)


print("\n Items from the last 5 years:\n")
for item in loaded_items:
    if item.is_recent(5):
        print(item)


print("\n Articles with DOI starting with '10.1234':\n")
for item in loaded_items:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)



   
