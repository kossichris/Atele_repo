from flask import request
from flask_restful import Resource
from Models.Client import db, Client,ClientSchema

clients_schema = ClientSchema(many=True)
client_schema = ClientSchema()

class ClientLogic(Resource):
    def get(self):
        clients = Client.query.all()
        clients = clients_schema.dump(clients).data
        return {'status': 'success', 'data': clients}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = client_schema.load(json_data)
        if errors:
            return errors, 422
        client = Client.query.filter_by(nom=data['nom']).first()
        if client:
            return {'message': 'Client already exists'}, 400
        client = Client(
            nom=json_data['nom'],
            prenom=json_data['prenom'],
            date_naissance=json_data['date_naissance'],
            situation_matrimonial=json_data['situation_matrimonial'],
            entreprise=json_data['entreprise'],
            longitude=json_data['longitude'],
            latitude=json_data['latitude'],
            forme_juridique=json_data['forme_juridique'],
            adresse=json_data['adresse'],
            fonction=json_data['fonction'],
            domaine_activite=json_data['domaine_activite']
        )

        db.session.add(client)
        db.session.commit()

        result = client_schema.dump(client).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = client_schema.load(json_data)
        if errors:
            return errors, 422
        client = Client.query.filter_by(id=data['id']).first()
        if not client:
            return {'message': 'Client does not exist'}, 400
        client = Client(
            nom=json_data['nom'],
            prenom=json_data['prenom'],
            date_naissance=json_data['date_naissance'],
            situation_matrimonial=json_data['situation_matrimonial'],
            entreprise=json_data['entreprise'],
            longitude=json_data['longitude'],
            latitude=json_data['latitude'],
            forme_juridique=json_data['forme_juridique'],
            adresse=json_data['adresse'],
            fonction=json_data['fonction'],
            domaine_activite=json_data['domaine_activite']
        )
        db.session.commit()

        result = client_schema.dump(client).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = client_schema.load(json_data)
        if errors:
            return errors, 422
        client = Client.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = client_schema.dump(client).data

        return {"status": 'success', 'data': result}, 204