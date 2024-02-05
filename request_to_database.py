import psycopg2
import base64
from datetime import datetime
class RequestToDataBase:

    def create_connection(self):
        return psycopg2.connect(
            host="postgres",
            port="5432",
            database="onec_cinfo",
            user="oleg",
            password="Zxcv7890"
        )

    def insert_value(self, list_val: list):
        with self.create_connection() as conn, conn.cursor() as cursor:
            sql_query = """
                INSERT INTO message_data (
                    need_rewrite, 
                    sending_process_status,
                    message_type, 
                    processing_type, 
                    receiver_system, 
                    message_id,
                    sender_system,
                    data,
                    received
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = self.set_elements_for_db(list_val)
            cursor.execute(sql_query, values)

    def request_select(self, column):
        with self.create_connection() as conn, conn.cursor() as cursor:
            # Выборка записей
            select_query = "SELECT * FROM message_data WHERE receiver_system=%s AND received=false;"
            cursor.execute(select_query, (column,))
            rows = cursor.fetchall()


            if rows:
                current_time = datetime.now()
                update_query = "UPDATE message_data SET send_time = %s WHERE receiver_system=%s AND received=false;"
                cursor.execute(update_query, (current_time, column))

            return self.set_output_elements(rows)

    def alter_request_for_database(self, arr_message_id: list):
        with self.create_connection() as conn, conn.cursor() as cursor:
            cursor.execute("SELECT message_id FROM message_data WHERE received=false")
            records = cursor.fetchall()

            # Получаем текущее время
            current_time = datetime.now()

            for record in records:
                record_id = record[0]  # Получаем message_id из кортежа
                value = record_id in arr_message_id
                # Обновляем поле received и arrival_time
                cursor.execute(
                    "UPDATE message_data SET received = %s, arrival_time = %s WHERE message_id = %s",
                    (value, current_time, record_id)
                )

    def set_elements_for_db(self, list_val: list):
        keys = ['need-rewrite', 'sending-process-status', 'message-type', 'processing-type', 'receiver-system',
                'message-id', 'sender-system', 'data', 'received']
        values = {key: False for key in keys}
        values['received'] = False  # default value

        for header in list_val:
            key, val = header
            if key in values:
                if key == 'data' and isinstance(val, bytes):
                    values[key] = val.decode()
                else:
                    values[key] = val

        return tuple(values.values())

    def set_output_elements(self, list_rows: list):
        headers = ['need-rewrite', 'sending-process-status', 'message-type', 'processing-type', 'receiver-system',
                   'message-id', 'sender-system', 'data']
        result = []

        for row in list_rows:
            # Создаем часть header
            header_part = {headers[i]: row[i] for i in range(len(headers)) if headers[i] != 'data'}

            # Обрабатываем часть данных, если она есть
            data_index = headers.index('data')  # Получаем индекс для 'data'
            data_part = row[data_index] if row[data_index] else None

            if isinstance(data_part, memoryview):
                # Если это memoryview, сначала преобразуем в bytes
                data_part = data_part.tobytes()

            if isinstance(data_part, bytes):
                # Конвертируем bytes в base64 encoded string
                data_part = base64.b64encode(data_part).decode('utf-8')

            # Добавляем header
            message_structure = [{"header": header_part}]

            # Добавляем данные, если они есть
            if data_part is not None:
                message_structure.append({"Message": {"data": data_part}})

            result.extend(message_structure)  # Добавляем структуру сообщения в итоговый результат

        return result





