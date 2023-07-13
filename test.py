from getdata import GetData
import unittest
from unittest.mock import patch
import psycopg2
from request_to_database import RequestTODataBase
class MyTestCase(unittest.TestCase):


    def test_get_data_with_list(self):
        obj = GetData({"key": [1, 2, 3]})
        result, flag = obj.get_data()
        self.assertEqual(result, [1, 2, 3])
        self.assertTrue(flag)

    def test_get_data_without_list(self):
        obj = GetData({"key1": {"subkey1": "value1", "subkey2": "value2"}})
        result, flag = obj.get_data()
        expected_result = [("subkey1", "value1"), ("subkey2", "value2")]
        self.assertEqual(result, expected_result)
        self.assertFalse(flag)


    def test_get_list_data(self):
        obj = GetData({"key": [1, 2, 3]})
        list_data = []
        result = obj.get_list_data(list_data)
        self.assertEqual(result, [])

            # Тестирование списка с несколькими элементами
        list_data = [
        {"status": "success", "message-id": 1},
        {"status": "failed", "message-id": 2},
        {"status": "success", "message-id": 3}
        ]
        result = obj.get_list_data(list_data)
        self.assertEqual(result, [1, 3])

            # Тестирование списка без элементов со статусом "success"
        list_data = [
            {"status": "failed", "message-id": 4},
            {"status": "pending", "message-id": 5}
            ]
        result = obj.get_list_data(list_data)
        self.assertEqual(result, [])

    """@patch('psycopg2.connect')
    def test_insert_value(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value

        # Моделируем успешную вставку значений
        list_val = [1, 2, 3]
        self.obj.insert_value(list_val)
        mock_cursor.execute.assert_called_once()
        mock_connect.return_value.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

        # Моделируем исключение при вставке значений
        mock_cursor.reset_mock()
        mock_connect.return_value.commit.reset_mock()
        mock_cursor.execute.side_effect = psycopg2.DatabaseError("Ошибка базы данных")
        list_val = [4, 5, 6]
        with self.assertRaises(psycopg2.DatabaseError):
            self.obj.insert_value(list_val)
        mock_cursor.execute.assert_called_once()
        mock_connect.return_value.commit.assert_not_called()
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()"""

    def test_set_elements_for_db(self):
        obj = RequestTODataBase()
        list_val = [
            ('need-rewrite', 'true'),
            ('sending-process-status', 'true'),
            ('message-type', 'type1'),
            ('processing-type', 'type2'),
            ('receiver-system', 'system1'),
            ('message-id', 'id1'),
            ('sender-system', 'system2'),
            ('data', 'data1'),
            ('received', 'true')
        ]
        result = obj.set_elements_for_db(list_val)
        expected_result = (True, True, 'type1', 'type2', 'system1', 'id1', 'system2', 'data1', False)
        self.assertEqual(result, expected_result)

        # Тестирование с отсутствующими значениями
        list_val = [
            ('need-rewrite', 'false'),
            ('sending-process-status', 'false'),
            ('message-type', ''),
            ('processing-type', ''),
            ('receiver-system', ''),
            ('message-id', ''),
            ('sender-system', ''),
            ('data', ''),
            ('received', 'false')
        ]
        result = obj.set_elements_for_db(list_val)
        expected_result = (False, False, '', '', '', '', '', '', False)
        self.assertEqual(result, expected_result)

    def test_set_output_elements(self):
        obj = RequestTODataBase()
        list_rows = [
            ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', None]
        ]
        result = obj.set_output_elenents(list_rows)
        expected_result = {
            "Message": [
                {
                    "header": {
                        "need-rewrite": "value1",
                        "sending-process-status": "value2",
                        "message-type": "value3",
                        "processing-type": "value4",
                        "receiver-system": "value5",
                        "message-id": "value6",
                        "sender-system": "value7"
                    }
                },
                {
                    "Message": {
                        "data": None
                    }
                }
            ]
        }
        self.assertEqual(result, expected_result)

        # Тестирование с данными, включая непустое значение для byte_data
        list_rows = [
            ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', b'byte_data']
        ]
        result = obj.set_output_elenents(list_rows)
        expected_result = {
            "Message": [
                {
                    "header": {
                        "need-rewrite": "value1",
                        "sending-process-status": "value2",
                        "message-type": "value3",
                        "processing-type": "value4",
                        "receiver-system": "value5",
                        "message-id": "value6",
                        "sender-system": "value7"
                    }
                },
                {
                    "Message": {
                        "data": "byte_data"
                    }
                }
            ]
        }
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()