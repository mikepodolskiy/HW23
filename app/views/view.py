# import required libraries and modules
from flask import request, Blueprint, jsonify
from marshmallow import ValidationError

from app.funcs.functions import filter_data, map_data, read_file, sort_data, limit_data, unique_data
from app.model.model import RequestSchema

# creating blueprint
main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query():
    # getting data from request
    req_data = request.json

    # checking data correctness using marshmallow
    try:
        RequestSchema().load(req_data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    # checking file existence, otherwise throwing exception
    try:
        data = read_file("".join(['data/', req_data['file_name']]))
    except FileNotFoundError:
        return 'File not found, check file path', 404

    # check received data, applying relative function, forming data
    if req_data['cmd1'] == 'filter':
        output_data = filter_data(data, req_data['value1'])

    elif req_data['cmd1'] == 'map':
        output_data = map_data(data, req_data['value1'])

    elif req_data['cmd1'] == 'sort':
        output_data = sort_data(data, req_data['value1'])

    elif req_data['cmd1'] == 'limit':
        output_data = limit_data(data, req_data['value1'])

    elif req_data['cmd1'] == 'unique':
        output_data = unique_data(data)

    # check second pair of received data, applying relative function to the previously formed data
    if req_data['cmd2'] == 'filter':
        output_data = filter_data(output_data, req_data['value2'])

    elif req_data['cmd2'] == 'map':
        output_data = map_data(output_data, req_data['value2'])

    elif req_data['cmd2'] == 'sort':
        output_data = sort_data(output_data, req_data['value2'])

    elif req_data['cmd2'] == 'limit':
        output_data = limit_data(output_data, req_data['value2'])

    elif req_data['cmd2'] == 'unique':
        output_data = unique_data(output_data)

    # return result of function applying
    return jsonify(list(output_data)), 200
