from flask import Flask, make_response, request, jsonify
from DB.db_access import insert_url, get_url
import webbrowser
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Insert original URL & return shortened URL
@app.route("/generate", methods=["POST"])
def generate_url():
    if "url" in request.form:
        resp = insert_url(request.form["url"])
        if resp is not None:
            short_url = request.base_url.replace('generate','') + str(resp)
            return make_response(jsonify({"data":short_url}), 200)
        else:
            return make_response("Error: Invalid URL", 200)
    else:
        return make_response("Error: URL not provided", 400)

# Using the given ID and base URL, return the original URL
@app.route("/<string:id>", methods=["GET"])
def navigate_to_original_url(id):
    try:
        url = get_url(id)
    except:
        return make_response("Error: Invalid URL", 200)
    if url is not None:
        webbrowser.open(url)
        return
    else:
        return make_response("Error: ID not found", 404)


if __name__ == "__main__":
    app.run(debug=True)