import os
from flask import request, Blueprint, jsonify
from app.funcs.functions import filter_data, map_data, read_file, sort_data, limit_data, unique_data

# creating blueprint
main_blueprint = Blueprint('main_blueprint', __name__)

BASE_DIR = os.path.dirname(os.path.abspath('apache_logs.txt'))
DATA_DIR = os.path.join(BASE_DIR, "data")


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    data = request.json

    # input validation of data
    # fieldnames, quantity etc.
    cmd1 = data['cmd1']
    value1 = data['value1']
    cmd2 = data['cmd2']
    value2 = data['value2']
    # filter, map, unique, limit

    data = read_file('data/apache_logs.txt')

    if cmd1 == 'filter':
        output_data = filter_data(data, value1)

    elif cmd1 == 'map':
        output_data = map_data(data, value1)

    elif cmd1 == 'sort':
        output_data = sort_data(data, value1)

    elif cmd1 == 'limit':
        output_data = limit_data(data, value1)

    elif cmd1 == 'unique':
        output_data = unique_data(data)

    # if cmd2:

    if cmd2 == 'filter':
        output_data = filter_data(output_data, value2)

    elif cmd2 == 'map':
        output_data = map_data(output_data, value2)

    elif cmd2 == 'sort':
        output_data = sort_data(output_data, value2)

    elif cmd2 == 'limit':
        output_data = limit_data(output_data, value2)

    elif cmd2 == 'unique':
        output_data = unique_data(output_data)

    return jsonify(list(output_data)), 200
