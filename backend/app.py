from flask import Flask, render_template, send_from_directory
import json
import os

app = Flask(
    __name__,
    template_folder=os.path.abspath("templates"),
    static_folder=os.path.abspath("static"),
)

app.add_url_rule(
    "/build/<path:filename>",
    endpoint="build",
    view_func=lambda filename: send_from_directory("build", filename),
)


def get_asset_path(entry):
    try:
        with open('build/.vite/manifest.json', 'r') as f:
            manifest = json.load(f)
            return manifest[f'src/{entry}/main.jsx']['file']
    except:
        return f'assets/{entry}.js'


@app.route("/")
def landing():
    asset_path = get_asset_path("landing")
    return render_template(
        "index.html", app_name="landing", debug=app.debug, asset_path=asset_path
    )


@app.route("/protected")
def protected():
    asset_path = get_asset_path("protected")
    return render_template(
        "index.html", app_name="protected", debug=app.debug, asset_path=asset_path
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
