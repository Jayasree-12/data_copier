# import pandas as pd
# import os
# def main():
#     i="i love u"
#     print('hello papa......'+i)
#     file_path='C:\\Users\\medikurthy.j\\Research\\data\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
#     data = pd.read_json(file_path, lines=True)
#     print(data.count())
#     print(data.describe())
#     print(data.columns)
#     print(data.dtypes)
#     print(data[['order_item_order_id','order_item_subtotal']])
#     print(type(data[['order_item_order_id','order_item_subtotal']]))
#
#print('hii')


# def main():
#      DATABASE_NAME = os.environ.get('retail_db')
#      print(f'hello from {DATABASE_NAME}')
#
# if __name__=="__main__":
#       main()

# import pandas as pd
# import os
# from read import get_json_reader
# from write import load_db_table
#
# def main():
#     BASE_DIR = os.environ.get('BASE_DIR')
#     table_name = os.environ.get('table_name')
#     json_reader = get_json_reader(BASE_DIR, table_name)
#     configs = dict(os.environ.items())
#     conn = f'postgresql://{configs["DATABASE_USER"]}:{configs["DATABASE_PASS"]}@{configs["DATABASE_HOST"]}:{configs["DATABASE_PORT"]}/{configs["DATABASE_NAME"]}'
#     for df in json_reader:
#         load_db_table(df, conn, table_name, df.columns[0])
#
# if __name__=="__main__":
#     main()



####for multiple tables:-
import pandas as pd
import os
import sys
from read import get_json_reader
from write import load_db_table

def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    print("hi this is commited")
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])

def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names=sys.argv[1].split(',')
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DATABASE_USER"]}:{configs["DATABASE_PASS"]}@{configs["DATABASE_HOST"]}:{configs["DATABASE_PORT"]}/{configs["DATABASE_NAME"]}'
    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)

if __name__=="__main__":
     main()
