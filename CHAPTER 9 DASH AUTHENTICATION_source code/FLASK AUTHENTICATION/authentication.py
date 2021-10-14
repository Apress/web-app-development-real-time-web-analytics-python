import flask
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
from user_profile import users_details
user_password, user_names = users_details()
app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])
CONTENT_STYLE = {"margin-left": "16rem",
                 "padding": "0.5rem 0.5rem",
                 "color": "gray"}
sign_in_form = html.Div([
    html.Form([
        dcc.Input(placeholder="Enter username",
                  name="username"),
        dcc.Input(placeholder="Enter password",
                  name="password",
                  type="password"),
        html.Button("Login", type='submit')],
        action="/login",
        method="post")])
_app_route = "/"
@app.server.route("/login", methods=["POST"])
def routes():
    data = flask.request.form
    username = data.get("username")
    password = data.get("password")
    if username not in user_password.keys() or  user_password[username] != password:
        return flask.redirect("/login")
    else:
        return_sess = flask.redirect(_app_route)
        return_sess.set_cookie("custom-auth-session", username)
        return return_sess
content = html.Div(id="page-content",
                   style=CONTENT_STYLE)
app.layout = html.Div([sign_in_form,
                       content])
app.run_server(mode='external',
               dev_tools_ui=False,
               dev_tools_props_check=False)
