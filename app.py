import os

from flask import Flask, Response, jsonify, render_template, request

from analytics import ANALYTICS_LIST, analytics_de_exemplo
from configuracao import JSON_PARAMS
from repositorio import RepositorioInstancias

app = Flask(__name__)
instancias = RepositorioInstancias()

REGISTO = {
    "name": "Desafio de Programação",
    "config_url": "/desafio/configuracao",
    "json_params_url": "/desafio/json-params",
    "user_url": "/desafio/deploy",
    "analytics_url": "/desafio/analytics",
    "analytics_list_url": "/desafio/analytics-list",
}


def base_url() -> str:
    """Return the public base URL, honouring the hosting HTTPS proxy."""
    proto = request.headers.get("X-Forwarded-Proto", request.scheme)
    return f"{proto}://{request.host}"


@app.after_request
def cors(resp: Response) -> Response:
    """Allow Inven!RA to call the services from the teacher's browser."""
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return resp


@app.get("/")
def indice():
    """Return the activity registration file with absolute URLs."""
    base = base_url()
    return jsonify({k: (base + v if k != "name" else v) for k, v in REGISTO.items()})


@app.get("/desafio/configuracao")
def configuracao():
    """config_url: configuration page embedded by Inven!RA."""
    return render_template("configuracao.html")


@app.get("/desafio/json-params")
def json_params():
    """json_params_url: fields Inven!RA reads from the configuration page."""
    return jsonify(JSON_PARAMS)


@app.route("/desafio/deploy", methods=["GET", "POST"])
def deploy():
    """user_url: create the activity instance and return the student access URL."""
    activity_id = request.args.get("activityID")
    if activity_id is None and request.is_json:
        activity_id = (request.get_json(silent=True) or {}).get("activityID")
    if not activity_id:
        return jsonify({"erro": "Falta o parâmetro activityID"}), 400
    instancias.criar_instancia(activity_id)
    return Response(f"{base_url()}/desafio/{activity_id}", mimetype="text/plain")


@app.get("/desafio/analytics-list")
def analytics_list():
    """analytics_list_url: analytics collected by the activity."""
    return jsonify(ANALYTICS_LIST)


@app.post("/desafio/analytics")
def analytics():
    """analytics_url: analytics of every student in an activity instance."""
    dados = request.get_json(silent=True) or {}
    activity_id = dados.get("activityID")
    if not activity_id:
        return jsonify({"erro": "Falta o campo activityID no corpo JSON"}), 400
    return jsonify(analytics_de_exemplo(base_url(), activity_id))


@app.route("/desafio/<activity_id>", methods=["GET", "POST"])
def acesso(activity_id):
    """Student access ("Provide activity"), not implemented yet."""
    estado = "registada" if instancias.existe_instancia(activity_id) else "desconhecida"
    return jsonify({
        "activityID": activity_id,
        "instancia": estado,
        "mensagem": "O serviço 'Provide activity' será implementado numa fase posterior.",
    }), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
