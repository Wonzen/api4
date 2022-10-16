class Users():

    def __init__(self, idd, full_name=None, gender=None, date_birthday=None, path_avatar=None,
                 residential_address=None):
        self.id = idd
        self.full_name = full_name
        self.gender = gender
        self.date_birthday = date_birthday
        self.path_avatar = path_avatar
        self.residential_address = residential_address

    def to_Json(self):
        return {
            'id': self.idd,
            'full_name': self.full_name,
            'gender': self.gender,
            'date_birthday': self.date_birthday,
            'path_avatar': self.path_avatar,
            'residential_address': self.residential_address,

        }
