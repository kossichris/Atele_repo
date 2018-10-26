from flask import Flask
from sqlalchemy import create_engine
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import sqlite3

ma = Marshmallow()
db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), unique=True, nullable=False)
    prenom = db.Column(db.String(150), unique=True, nullable=False)
    date_naissance = db.Column(db.String(150), unique=True, nullable=False)
    situation_matrimonial = db.Column(db.String(150), unique=True, nullable=False)
    entreprise = db.Column(db.String(150), unique=True, nullable=False)
    longitude = db.Column(db.Float, unique=True, nullable=False)
    latitude = db.Column(db.Float, unique=True, nullable=False)
    forme_juridique = db.Column(db.String, unique=True, nullable=False)
    adresse = db.Column(db.String, unique=True, nullable=False)
    fonction = db.Column(db.String, unique=True, nullable=False)
    domaine_activite = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, nom,prenom,date_naissance,situation_matrimonial,entreprise,longitude,latitude,forme_juridique,adresse,fonction,domaine_activite):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.situation_matrimonial = situation_matrimonial
        self.entreprise = entreprise
        self.longitude = longitude
        self.latitude = latitude
        self.forme_juridique = forme_juridique
        self.adresse = adresse
        self.fonction = fonction
        self.domaine_activite = domaine_activite

class ClientSchema(ma.Schema):
    id = fields.Integer()
    nom = fields.String(required=True)
    prenom = fields.String(required=True)
    date_naissance = fields.String(required=True)
    situation_matrimonial = fields.String(required=True)
    entreprise = fields.String(required=True)
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
    forme_juridique = fields.String(required=True)
    adresse = fields.String(required=True)
    fonction = fields.String(required=True)
    domaine_activite = fields.String(required=True)





