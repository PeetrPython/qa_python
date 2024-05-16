from main import BooksCollector

class TestBooksCollector:


    def test_books_genre_empty_dict(self):
        books_genre = BooksCollector()
        empty_dict = {}
        assert books_genre.empty_dict == 'Словарь пустой'

    def test_favorite_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == [], 'Список не пустой!'

    def test_books_genre_empty_dict(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}, 'Словарь не пустой'

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Божественная комедия')
        assert 'Божественная комедия' in collector.get_books_genre()

    def test_set_book_genre_true(self):
        new_book = BooksCollector()
        new_book.books_genre = {'1984': 'Фантастика'}
        new_book.genres = ['Фантастика']
        new_book.set_book_genre('1984', 'Фантастика')
        assert new_book.books_genre['1984'] == 'Фантастика'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', "Фантастика")
        assert collector.get_book_genre('Гарри Поттер') == "Фантастика"

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.set_book_genre('Звездные войны', 'Фантастика')
        collector.add_new_book('Кошмары на улице Вязов')
        collector.set_book_genre('Кошмары на улице Вязов', 'Ужасы')
        collector.add_new_book('Остров проклятых')
        collector.set_book_genre('Остров проклятых', 'Детективы')
        children_books = collector.get_books_for_children()
        assert 'Звездные войны' in children_books
        assert 'Кошмары на улице Вязов' not in children_books
        assert 'Остров проклятых' not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_book_in_favorites('Звездные войны')
        assert 'Звездные войны' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_book_in_favorites('Звездные войны')
        collector.delete_book_from_favorites('Звездные войны')
        assert 'Звездные войны' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_book_in_favorites('Звездные войны')
        assert collector.get_list_of_favorites_books() == ['Звездные войны']















