
class GetData:
    def __init__(self, dictionary: dict):
        """Инициализация с входным словарем."""
        self.dictionary = dictionary

    def get_data(self) -> (list, bool):
        """
        Обрабатывает словарь для получения данных для базы данных.
        Возвращает кортеж, содержащий данные и булевый флаг.
        Флаг True, если в словаре найден список.
        """
        data_for_database = []

        for key, value in self.dictionary.items():
            if isinstance(value, list):
                # Возвращает список напрямую, если значение является списком
                return value, True
            elif isinstance(value, dict):
                # Распаковывает словарь в список кортежей
                data_for_database.extend(value.items())

        return data_for_database, False

    def get_list_data(self, list_data: list) -> list:
        """
        Извлекает идентификаторы сообщений из списка словарей.
        Возвращает список идентификаторов сообщений.
        """
        return [item["message-id"] for item in list_data if item.get("status") == "success"]
