"""Dump and Load PostgreSQL/SQLAlchemy from/to json file"""

import sys
sys.path.append("../..")

import json

from databases.postgres import engine, drop_create, session
from models import datum, filter, user

classes = [datum.DatumGroup, datum.DatumType, datum.ElementType]
json_file = "populate_sa_pg.json"

def sqlalchemy_json_dump(classes, json_file_name):

    print(">>>>>>>>>>Dumping data to {}<<<<<<<<<<".format(json_file_name))

    output = {}
    for cls in classes:
        class_name = cls.__name__
        if session.query(cls).count() > 0:
            model_data = session.query(cls).order_by("sort").all()
            rows_count = len(model_data)
            rows = []
            for datum_group in model_data:
                row = {}
                for col in cls.__table__.c:
                    if col.name is not "id":
                        row[col.name] = getattr(datum_group, col.name)
                rows.append(row)

            output[class_name] = rows
            print("{} - {} rows dumped.".format(class_name, rows_count))

    output_json = json.dumps(output)

    with open(json_file_name, "w") as f :
        f.write(output_json)

    print(">>>>>>>>>>Data dumped to {}<<<<<<<<<<".format(json_file_name))


def sqlalchemy_json_load(classes, json_file_name, sqlalchemy_engine):

    print(">>>>>>>>>>Loading data from {}<<<<<<<<<<".format(json_file_name))

    model_data = ""
    with open(json_file_name) as f :
        model_data = json.load(f)

    for cls in classes:
        class_name = cls.__name__
        if class_name in model_data.keys():
            table = cls.__table__
            ins = table.insert().values(model_data[class_name])
            sqlalchemy_engine.execute(ins)
            rows_count = len(model_data[class_name])
            print("{} - {} rows loaded.".format(class_name, rows_count))

    print(">>>>>>>>>>Data loaded from {}<<<<<<<<<<".format(json_file_name))


if __name__ == "__main__":

    input = input("(D)ump to json file\n"
                  "(L)oad from json file - will drop/create database\n"
                  "(R)eset - drop/create database\n"
                  "-->  ")
    input = input.lower()

    if input == "d":
        sqlalchemy_json_dump(classes, json_file)
    elif input == "l":
        drop_create()
        sqlalchemy_json_load(classes, json_file, engine)
    elif input == "r":
        drop_create()
    else:
        print("No action taken")