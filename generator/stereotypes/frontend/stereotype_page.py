
class StereotypePage:

    def __init__(self, create: bool = True, update: bool = True,
                 get_all: bool = True, get_by_id: bool = True,
                 singular_label: str = '', plural_label: str = '', accusative_label: str = ''):
        self.create = create
        self.update = update
        self.get_all = get_all
        self.get_by_id = get_by_id
        self.singular_label = singular_label
        self.plural_label = plural_label
        self.accusative_label = accusative_label

    def __str__(self):
        return '[StereotypePage] Create = {}; Update = {}; GetAll = {}; GetById = {}; SingularLabel = {}; PluralLabel = {}; AccusativeLabel = {}'\
            .format(self.create, self.update, self.get_all, self.get_by_id, self.singular_label, self.plural_label, self.accusative_label)
