#!/usr/bin/env python
from snowflake_utils import connect, general_information


connection = connect()
general_information(connection)
