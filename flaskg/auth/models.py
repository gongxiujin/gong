from sqlalchemy.orm import backref
from flaskg.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id', name='fk_user_school'), nullable=False, index=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    banned = db.Column(db.Boolean, default=False)
    user = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

    def __int__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

class School(db.Model):
    __tablename__='school'

    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.Text)
    user=db.relationship('User', backref='school', lazy='dynamic', cascade='delete')

    def __repr__(self):
        return '<School %r>' % self.description

    def __init__(self, description):
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()