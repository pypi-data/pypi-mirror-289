from multi_db_query_builder.database_object_handler import DatabaseObjectHandler


def check_if_table_exists(data_store, db_session, schema_name, table_name):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.check_if_table_exists(db_session, schema_name, table_name)
    return res


def check_if_column_exists(
    data_store, db_session, schema_name, table_name, column_name
):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.check_if_column_exists(
        db_session, schema_name, table_name, column_name
    )
    return res


def get_schemas_like_pattern(data_store, db_session, schema_name=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.get_schemas_like_pattern(db_session, schema_name)
    return res


def fetch_column_name(data_store, db_session, schema_name, table_name):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.fetch_column_name(db_session, schema_name, table_name)
    return res


def fetch_column_name_datatype(
    data_store, db_session, schema_name, table_name, filter_val="fivetran"
):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.fetch_column_name_datatype(
        db_session, schema_name, table_name, filter_val
    )
    return res


def fetch_single_column_name_datatype(
    data_store, db_session, schema_name, table_name, column_name
):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.fetch_single_column_name_datatype(
        db_session, schema_name, table_name, column_name
    )
    return res


def fetch_all_tables_in_schema(data_store, db_session, schema_name, pattern=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.fetch_all_tables_in_schema(db_session, schema_name, pattern)
    return res


def fetch_all_views_in_schema(data_store, db_session, schema_name, pattern=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.fetch_all_views_in_schema(db_session, schema_name, pattern)
    return res


def fetch_table_type_in_schema(data_store, db_session, schema_name, table_name):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.fetch_table_type_in_schema(
        db_session, schema_name, table_name
    )
    return res


def enclose_reserved_keywords(data_store, query):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.enclose_reserved_keywords(query)
    return res


def enclose_reserved_keywords_v2(data_store, columns_string):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.enclose_reserved_keywords_v2(columns_string)
    return res


def handle_reserved_keywords(data_store, query_string):

    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.handle_reserved_keywords(query_string)
    return res


def get_tables_under_schema(data_store, db_session, schema):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.get_tables_under_schema(db_session, schema)
    return res


#  OPERATIONS


def mode_function(data_store, column, alias=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.mode_function(column, alias)
    return res


def median_function(data_store, column, alias=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.median_function(column, alias)
    return res


def concat_function(data_store, column, alias, separator):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.concat_function(column, alias, separator)
    return res


def pivot_function(data_store, fields, column_list, schema, table_name):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.pivot_function(fields, column_list, schema, table_name)
    return res


def trim_function(data_store, column, value, condition, alias=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.trim_function(column, value, condition, alias)
    return res


def split_function(data_store, column, delimiter, part, alias=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.split_function(column, delimiter, part, alias)
    return res


def timestamp_to_date_function(data_store, column, alias=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.timestamp_to_date_function(column, alias)
    return res


def substring_function(data_store, column, start, end):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.substring_function(column, start, end)
    return res


def table_rename_query(data_store, schema_name, old_table_name, new_table_name):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.table_rename_query(
        schema_name, old_table_name, new_table_name
    )
    return res


def date_diff_in_hours(data_store, start_date, end_date, table_name):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.date_diff_in_hours(start_date, end_date, table_name)
    return res


def date_substraction(data_store, date_part, start_date, end_date, alias=None):
    data_store_object = DatabaseObjectHandler.get_data_object(data_store)
    res = data_store_object.date_substraction(date_part, start_date, end_date, alias)
    return res
