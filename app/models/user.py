#!/usr/bin/env python
from flask import Flask, jsonify, request
from config import db
import yaml
import os


class User(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cell = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    nat = db.Column(db.String(2), nullable=False)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
