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
             data 
             )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = conn.cursor()
        values = self.set_elements_for_db(list_val)
        cursor.execute(sql_query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def request_select(self, column):
        conn = psycopg2.connect(
            host="127.0.0.1",
            port="5432",
            database="onec_cinfo",
            user="oleg",
            password="Zxcv7890"
        )
        sql_query = f"SELECT * FROM message_data WHERE receiver_system='{str(column)}';"
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        list_rows = []
        for row in rows:
            list_rows.append(row)
        print(list_rows)
        out_dict = self.set_output_elenents(list_rows)
        cursor.close()
        conn.close()
        return out_dict

    def set_elements_for_db(self, list_val:list):
        need_rewrite: bool = True
        sending_process_status: bool = True
        message_type: str = ""
        processing_type: str = ""
        receiver_system: str = ""
        message_id: str = ""
        sender_system: str = ""
        data: str = ""

        for header in list_val:

            if header[0] == 'need-rewrite':
                if header[1] != 'true':
                    need_rewrite = False

            if header[0] == 'sending-process-status':
                if header[1] != 'true':
                    sending_process_status = False

            if header[0] == 'message-type':
                message_type = header[1]

            if header[0] == 'processing-type':
                processing_type = header[1]

            if header[0] == 'receiver-system':
                receiver_system = header[1]

            if header[0] == 'message-id':
                message_id = header[1]

            if header[0] == 'sender-system':
                sender_system = header[1]

            if header[0] == 'data':
                data = header[1]

        return need_rewrite, sending_process_status, message_type, processing_type, receiver_system, message_id, sender_system, data

    def set_output_elenents(self, list_rows: list):
        arr_row = ['need-rewrite',
         'sending-process-status',
         'message-type',
         'processing-type',
         'receiver-system',
         'message-id',
         'sender-system',
         'data']
        dict_message = {"Message": ""}

        array_dict = []
        for row in list_rows:
            dict_out = {"header": ""}
            dict_val = {}
            dict_val[arr_row[0]] = row[0]
            dict_val[arr_row[1]] = row[1]
            dict_val[arr_row[2]] = row[2]
            dict_val[arr_row[3]] = row[3]
            dict_val[arr_row[4]] = row[4]
            dict_val[arr_row[5]] = row[5]
            dict_val[arr_row[6]] = row[6]
            byte_data = row[7]
            dict_out["header"] = dict_val
            array_dict.append(dict_out)
            if byte_data == None:
                d_mess = {"Message": {arr_row[7]: None}}
                array_dict.append(d_mess)
            else:
                byte_data_bytes = bytes(byte_data)
                decode_data = byte_data_bytes.decode()
                d_mess = {"Message": {arr_row[7]: decode_data}}
                array_dict.append(d_mess)


        dict_message["Message"] = array_dict
        return dict_message




