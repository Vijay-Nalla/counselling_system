from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attendance = db.Column(db.Float, nullable=False)
    grades = db.Column(db.Float, nullable=False)
    fees_paid = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Student {self.name}>'
