import psycopg2
class RequestTODataBase:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="1CINFO",
        user="oleg",
        password="Zxcv7890"
    )

    def insert_value(self, list_val: list):

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
        cursor = self.conn.cursor()
        values = self.set_elements_for_db(list_val)
        cursor.execute(sql_query, values)
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def request_select(self):
        sql_query = "SELECT * FROM message_data"
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        list_rows = []
        for row in rows:
            list_rows.append(row)
        cursor.close()
        self.conn.close()
        return list_rows

    def set_elements_for_db(self, list_val: list):
        need_rewrite = list_val[0][1]
        sending_process_status = list_val[1][1]
        message_type = list_val[2][1]
        processing_type = list_val[3][1]
        receiver_system = list_val[4][1]
        message_id = list_val[5][1]
        sender_system = list_val[6][1]
        return need_rewrite, sending_process_status, message_type, processing_type, receiver_system, message_id, sender_system
