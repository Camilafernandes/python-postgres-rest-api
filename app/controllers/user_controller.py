#!/usr/bin/env python
from flask import Blueprint, jsonify, request
import services.user_service as user_service
from models.user import User
from werkzeug.exceptions import HTTPException
import json

api = Blueprint('users', 'users')

@api.route('/users', methods=['GET'])
def api_get():
    ''' Get entities with filter or not'''

    users = user_service.get(request.args.get('start'), request.args.get('limit'), request.args.get('name'))

    return jsonify([user.as_dict() for user in users])

@api.route('/users', methods=['POST'])
def api_post():
    ''' Create entity'''
    user = user_service.post(request.json)
    return jsonify(user.as_dict())

@api.route('/users/<string:id>', methods=['PUT'])
def api_put(id):
    ''' Update entity by id'''
    body = request.json
    body['id'] = id
    res = user_service.put(body)
    return jsonify(res.as_dict()) if isinstance(res, User) else jsonify(res)

@api.route('/users/<string:id>', methods=['DELETE'])
def api_delete(id):
    ''' Delete entity by id'''
    res = user_service.delete(id)
    return jsonify(res)

@api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON format for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        'success': False,
        "message": e.description
    })
    response.content_type = "application/json"
    return response


def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj