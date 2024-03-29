import click
from cli_application.library_manager import LibraryManager

@click.group()
def cli():
    pass

@cli.command()
def list_books():
    manager = LibraryManager()
    manager.list_books()

@cli.command()
@click.argument('book_id', type=int)
def borrow_book(book_id):
    manager = LibraryManager()
    manager.borrow_book(book_id)

if __name__ == '__main__':
    cli()
