from flaskg.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, index=True, primary_key=True, nullable=False)
    name = db.Column(db.String(length=40), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
