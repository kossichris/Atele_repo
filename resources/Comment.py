from flask import jsonify, request
from flask_restful import Resource
from Model import db, Comment, Category, CommentSchema

comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()

class CommentResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema.dump(comments).data
        return {"status":"success", "data":comments}, 200

    def post(self):
        print('hello post function')
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = comment_schema.load(json_data)
        if errors:
            return errors, 422
        category_id = Category.query.filter_by(id=data['category_id']).first()
        print(category_id)
        if not category_id:
            return {'status': 'error', 'message': 'comment category not found'}, 400
        comment = Comment(
           category_id = json_data['category_id'],
            comment = json_data['comment']
            )
        print(comment)
        db.session.add(comment)
        db.session.commit()

        result = comment_schema.dump(comment).data
        print(result)

        return {'status': "success", 'data': result}, 201
