from flask_restful import Resource, abort
from flask import request
from users import users


class UserList(Resource):
    def get(self):
        return {"results": users}

    def post(self):
        data = request.json
        last_user_id = users[-1].get("id")
        new_user = {"id": last_user_id + 1, **data}
        users.append(new_user)

        return {"msg": "user created", "user": new_user}, 201


class UserResource(Resource):
    def get(self, user_id):
        user = next(filter(lambda u:u.get("id") == user_id, users), None)

        if user is None:
            abort(404)

        return {"user": user}

    def put(self, user_id):
        data = request.json

        user = None

        for i, u in enumerate(users):
            if u.get("id") == user_id:
                users[i] = {**u, **data}
                user = users[i]

        if user is None:
            abort(404)

        return {"msg": "user updated", "user": user}, 200

    def delete(self, user_id):
        user = None

        for i, u in enumerate(users):
            if u.get("id") == user_id:
                user = u
                users.pop(i)

        if user is None:
            abort(404)

        return {"msg": "user deleted"}, 204
