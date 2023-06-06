import psycopg2
class RequestTODataBase:

    def insert_value(self, list_val: list):
        conn = psycopg2.connect(
            host="127.0.0.1",
            port="5432",
            database="onec_cinfo",
            user="oleg",
            password="Zxcv7890"
        )
        sql_query = """
            INSERT INTO message_data (sending_process_status,
             need_rewrite, 
             message_type, 
             processing_type, 
             receiver_system, 
             message_id,
             sender_system,
             )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor = conn.cursor()
        values = self.set_elements_for_db(list_val)
        cursor.execute(sql_query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def request_select(self):
        conn = psycopg2.connect(
            host="127.0.0.1",
            port="5432",
            database="onec_cinfo",
            user="oleg",
            password="Zxcv7890"
        )
        sql_query = "SELECT * FROM message_data"
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        list_rows = []
        for row in rows:
            list_rows.append(row)
        cursor.close()
        conn.close()
        return list_rows

    def set_elements_for_db(self, list_val: list):
        need_rewrite: bool = True

        sending_process_status: bool = True

        if list_val[0][1] != 'true':
            need_rewrite = False

        if list_val[1][1] != 'true':
            sending_process_status = False

        message_type = list_val[2][1]

        processing_type = list_val[3][1]

        receiver_system = list_val[4][1]

        message_id = list_val[5][1]

        sender_system = list_val[6][1]

        return need_rewrite, sending_process_status, message_type, processing_type, receiver_system, message_id, sender_system
