from flask.views import MethodView
from flask import jsonify
from flask import request
from rest.models import db


class ItemAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        pass
        self.model = model

    def _get_item(self, id):
        return self.model.query.get_or_404(id)

    def get(self, id):
        item = self._get_item(id)
        return jsonify(item)

    def patch(self, id):
        item = self._get_item(id)
        errors = self.validator.validate(item, request.get_json)

        if errors:
            return jsonify(errors), 400

        item.update_from_json(request.get_json)
        db.session.commit()
        return jsonify(item)

    def delete(self, id):
        item = self._get_item(id)
        db.session.delete(item)
        db.session.commit()
        return "", 204


class GroupAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self):
        items = self.model.query.all()
        return jsonify([item for item in items])

    def post(self):
        errors = self.model.validate(request.get_data())

        if errors:
            print(errors)
            return jsonify(errors), 400

        db.session.add(self.model.from_json(request.get_json()))
        db.session.commit()

        items = self.model.query.all()
        return jsonify([item for item in items])


def register_api(app, model, name):
    item = ItemAPI.as_view(f"{name}-item", model)
    group = GroupAPI.as_view(f"{name}-group", model)
    app.add_url_rule(f"/{name}/<int:id>", view_func=item)
    app.add_url_rule(f"/{name}/", view_func=group)

# register_api(app, User, "users")
# register_api(app, Story, "stories")
