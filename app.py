from flask import Flask, request, abort, Response
from container import user_request
from marshmallow_dataclass import class_schema
from models import RequestArgs

app = Flask(__name__)



@app.route("/perform_query/", methods=['POST'])
def perform_query() -> Response:

    args = request.values
    RequestSchema = class_schema(RequestArgs)


    try:
        request_args = RequestSchema().load(args)
        result = user_request.execute(request_args)

    except Exception as e:
        abort(400)


    if not result:
        abort(404)

    return app.response_class(result, content_type="text/plain")

if __name__ == '__main__':
    app.run()
