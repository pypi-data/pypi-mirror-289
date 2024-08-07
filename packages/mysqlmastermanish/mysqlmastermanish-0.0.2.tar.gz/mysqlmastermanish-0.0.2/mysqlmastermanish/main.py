import mysql.connector
import json
import pandas as pd

class MySqlConnection:
    def __init__(self):
        pass
        
    def get_connection(self, host, user, password):
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password)
        print('connect successfully!!!')
        return connection

    def get_connection_by_json(self, json_file):
        with open(json_file, 'r') as file:
            auth = json.load(file)
        connection = self.get_connection(auth['host'], auth['user'], auth['password'])
        return connection

    def get_database_names(self, connection, with_default_database = False):
        if with_default_database:
            cursor = connection.cursor()
            cursor.execute('show databases')
            databases = [database[0] for database in cursor.fetchall()]
        else:
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES WHERE `Database` NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')")
            databases = [database[0] for database in cursor.fetchall()]
            
        return databases

    def get_table_names(self, connection, database):
        try:
            if type(database) == list:
                table_list = {}
                for db in database:
                    cursor = connection.cursor()
                    cursor.execute(f'use {db}')
                    cursor.execute('show tables')
                    tables = [table[0] for table in cursor.fetchall()]
                    table_list[db] = tables
            return table_list
        except Exception as e:
            return f'connection problem: {e}'
 
    def get_table_df(self, table_dict):
        try:
            table_data = []
            for database, tables in table_dict.items():
                for table in tables:
                    table_data.append([database, table])
            df = pd.DataFrame(table_data, columns=['database_name', 'table_name'])
            return df
        except Exception as e:
            return f'problem: {e}'
        
        