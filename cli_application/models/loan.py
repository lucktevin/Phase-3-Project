from .database import db

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Loan(user_id={self.user_id}, book_id={self.book_id})>"
