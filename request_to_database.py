import psycopg2
class RequestTODataBase:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="1CINFO",
        user="",
        password=""
    )

    def insert_value(self, list_val: list):
        sql_query = """
            INSERT INTO YourTable (column1, column2)
            VALUES (%s, %s)
        """
        cursor = self.conn.cursor()
        values = ('value1', 'value2')
        cursor.execute(sql_query, values)
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def request_select(self):
        sql_query = "SELECT * FROM YourTable"
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        list_rows = []
        for row in rows:
            list_rows.append(row)
        cursor.close()
        self.conn.close()
        return list_rows
