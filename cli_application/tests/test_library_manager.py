import pytest
from cli_application.library_manager import LibraryManager

@pytest.fixture
def manager():
    return LibraryManager()

def test_list_books(capsys, manager):
    manager.list_books()
    captured = capsys.readouterr()
    assert 'List of books' in captured.out

def test_borrow_book(capsys, manager):
    manager.borrow_book(1)
    captured = capsys.readouterr()
    assert 'Book borrowed successfully' in captured.out
