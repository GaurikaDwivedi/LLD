# from database.database import Database
from table.table import Table
from schema.column_data_type import StrDataType, IntDataType
from schema.schema_member import SchemaMember
from schema.table_schema import TableSchema


class Tests:

    @classmethod
    def table_flow(cls):
        # create schema
        user_schema = TableSchema()
        user_schema.add_schema_member(SchemaMember("user_id", StrDataType(0, 10), required=True))
        user_schema.add_schema_member(SchemaMember("user_name", StrDataType(0, 50)))
        user_schema.add_schema_member(SchemaMember("user_age", IntDataType(0, 100), required=False))

        # Create Table
        user_table = Table(table_name="users", table_schema=user_schema, primary_key="user_id")

        # create index
        user_table.create_index("user_name", "FUZZY")

        # insert seed data
        user_table.insert_data({"user_id": "user1", "user_name": "new user", "user_age": 20})
        user_table.insert_data({"user_id": "user2", "user_name": "improved user"})
        user_table.insert_data({"user_id": "user3", "user_name": "diff guy", "user_age": 30})
        print(user_table.filter_data({"user_name": "user"}))
        # out : [{'user_id': 'user1', 'user_name': 'new user', 'user_age': 20},
        # {'user_id': 'user2', 'user_name': 'improved user'}]

        print(user_table.filter_data({"user_name": "user", "user_age": 20}))
        # out : [{'user_id': 'user1', 'user_name': 'new user', 'user_age': 20}]

        user_table.delete_data("user2")
        print(user_table.filter_data({"user_name": "user"}))
        # out : [{'user_id': 'user1', 'user_name': 'new user', 'user_age': 20}]
test = Tests()
test.table_flow()