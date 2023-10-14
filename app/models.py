from app import db

class Dentists(db.Model):
    __tablename__ = 'dentists'

    # primary key
    id = db.Column(db.Integer, primary_key=True)

    # columns
    initials = db.Column(db.String(16), index=True, nullable=False)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(64), index=True, nullable=False)

    # relations
    patients = db.relationship('Patients', back_populates='dentist')

    # unique constraint
    __table_args__ = (db.UniqueConstraint('initials', 'last_name'),)

    def __repr__(self):
        return '<Dentist {} {}>'.format(self.initials, self.last_name)

class Patients(db.Model):
    __tablename__ = 'patients'

    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # foreign keys
    dentist_id = db.Column(db.Integer, db.ForeignKey('dentists.id'), nullable=False)

    # columns
    initials = db.Column(db.String(16), index=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    date_of_birth = db.Column(db.Date)

    # relations
    dentist = db.relationship('Dentists', back_populates='patients')