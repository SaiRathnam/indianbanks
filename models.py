from app import db

class Bank(db.Model):
    __tablename__ = 'banks'

    name = db.Column(db.String(49))
    id = db.Column(db.Integer, primary_key = True, nullable = False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def get_id(self):
        return self.id


class Branch(db.Model):
    __tablename__ = 'branches'

    ifsc = db.Column(db.String(11), primary_key = True, nullable = False)
    bank_id = db.Column(db.Integer)
    branch = db.Column(db.String(74))
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))

    def __repr__(self):
        return '<IFSC {}>'.format(self.ifsc)

    def get_bank_id(self):
        return self.bank_id

    def serialize(self):
        return {
                'ifsc': self.ifsc,
                'bank_id': self.bank_id,
                'branch': self.branch,
                'address': self.address,
                'city': self.city,
                'district': self.district,
                'state': self.state
        }
