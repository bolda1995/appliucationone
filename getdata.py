from datetime import datetime
import pytz
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

        moscow_tz = pytz.timezone('Europe/Moscow')
        data_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        arrival_time = '1970-01-01 00:00:00'  # Unix-эпоха
        send_time = '1970-01-01 00:00:00'
        data_for_database = []

        for key, value in self.dictionary.items():
            if isinstance(value, list):
                # Возвращает список напрямую, если значение является списком
                return value, True
            elif isinstance(value, dict):
                # Распаковывает словарь в список кортежей
                unpacked_items = value.items()
                data_for_database.extend(unpacked_items)

        if data_for_database:
            data_for_database.append(("date_time", data_time))
            data_for_database.append(("arrival_time",arrival_time))
            data_for_database.append(("send_time",send_time))

        return data_for_database, False
    def get_list_data(self, list_data: list) -> list:
        """
        Извлекает идентификаторы сообщений из списка словарей.
        Возвращает список идентификаторов сообщений.
        """
        return [item["message-id"] for item in list_data if item.get("status") == "success"]
