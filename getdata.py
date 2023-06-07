class GetData:
    dictionary: dict
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def get_data(self):
        data_for_database = []
        for k, v in self.dictionary.items():
            for t in v.items():
                data_for_database.append(t)

        return data_for_database[0:-1]
