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
                    received,
                    date_time,
                    arrival_time,
                    send_time
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                'message-id', 'sender-system', 'data', 'received', "date_time", "arrival_time", "send_time"]
        values = {key: False for key in keys}
        values['received'] = False  # default value
        print(list_val)
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
                   'message-id', 'sender-system', 'data', 'date-time']
        result = []

        for row in list_rows:
            print(row[11])
            header_part = {}
            for i, header in enumerate(headers):
                if header == 'data':
                    # Пропускаем обработку 'data' здесь, так как это бинарные данные
                    continue
                elif header == 'date_time':
                    header_part[header] = row[11].strftime('%Y-%m-%d %H:%M:%S') if isinstance(row[11], datetime) else None

                else:
                    # Для всех остальных полей просто копируем значение
                    header_part[header] = row[i]

            # Добавляем обработку для 'data'
            data_index = headers.index('data')
            data_part = base64.b64encode(row[data_index]).decode('utf-8') if row[data_index] else None

            # Формируем и добавляем структуру сообщения в итоговый результат
            result.append({"header": header_part})
            if data_part:
                result.append({"Message": {"data": data_part}})
        return result
