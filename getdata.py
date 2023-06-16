class GetData:
    dictionary: dict
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def get_data(self):
        data_for_database = []
        for k, v in self.dictionary.items():
            if type(v) == list:
                return v
            for t in v.items():
                data_for_database.append(t)

        return data_for_database

    def get_list_data(self, list_data: list):
        arr_message_id = []
        for iter_dict in list_data:
            if iter_dict["status"] == "success":
                arr_message_id.append(iter_dict["message-id"])
        return arr_message_id
