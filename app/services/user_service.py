#!/usr/bin/env python
from models.user import User
from config import db
from werkzeug.exceptions import NotFound
import json

def get(paginate = 1, limit = 20, filter = None):
    '''
    Get all entities
    :returns: all entity
    '''
    if filter is None:
        data = User.query.offset(paginate).limit(limit).all()
    if filter is not None:
        data = User.query.filter(User.name.like('%' + filter + '%')).offset(paginate).limit(limit)

    return data

def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    user = User(**body)
    db.session.add(user)
    db.session.commit()
    return user

def put(body):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    user = User.query.get(body['id'])
    if user:
        user = User(**body)
        db.session.merge(user)
        db.session.flush()
        db.session.commit()
        return user
    raise NotFound('no such entity found with id=' + str(body['id']))

def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))


