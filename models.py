import app

class Bank(app.db.Model):
    __tablename__ = 'banks'

    name = app.db.Column(app.db.String(49))
    id = app.db.Column(app.db.Integer, primary_key = True, nullable = False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def get_id(self):
        return self.id


class Branch(app.db.Model):
    __tablename__ = 'branches'

    ifsc = app.db.Column(app.db.String(11), primary_key = True, nullable = False)
    bank_id = app.db.Column(app.db.Integer)
    branch = app.db.Column(app.db.String(74))
    address = app.db.Column(app.db.String(195))
    city = app.db.Column(app.db.String(50))
    district = app.db.Column(app.db.String(50))
    state = app.db.Column(app.db.String(26))

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
