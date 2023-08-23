from typing import Any
from http import HTTPStatus

from flask import Flask, make_response, request, Response


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users: dict = {}

        @app.route("/user", methods=["POST"])
        def create_user() -> Response:
            data: dict[str, Any] = request.get_json()
            name: str = data.get("name")
            if name:
                users[name] = data.get("age")
                return make_response(
                    {"data": f"User {name} is created!"},
                    HTTPStatus.CREATED,
                )
            else:
                return make_response(
                    {"errors": {"name": "This field is required"}},
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

        @app.route("/user/<username>", methods=["GET"])
        def get_user(username: str) -> Response:
            if username not in users.keys():
                return make_response("", HTTPStatus.NOT_FOUND)
            return make_response({"data": f"My name is {username}"})

        @app.route("/user/<username>", methods=["PATCH"])
        def update_user(username: str) -> Response:
            data: dict[str, Any] = request.get_json()
            name: str = data.get("name")
            if not name or not username:
                return make_response("", HTTPStatus.NOT_FOUND)

            users[name] = data.get("age")
            del users[username]
            return make_response({"data": f"My name is {name}"})

        @app.route("/user/<username>", methods=["DELETE"])
        def delete_user(username: str) -> Response:
            if not username:
                return make_response("", HTTPStatus.UNPROCESSABLE_ENTITY)
            del users[username]
            return make_response("", HTTPStatus.NO_CONTENT)
