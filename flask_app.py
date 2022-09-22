from flask import Flask


def create_app():
    current_app = Flask(__name__)

    # 注册蓝图
    from views import sugg_blue
    current_app.register_blueprint(sugg_blue)

    return current_app


app = create_app()
