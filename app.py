from flask import Flask,render_template,session,g
import config
from exts import db
from blueprints import content_bp
from blueprints import user_bp
from flask_mail import Mail
from flask_migrate import Migrate
from models import UserModel
mail = Mail()
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app,db)
app.register_blueprint(content_bp)
app.register_blueprint(user_bp)


# @app.route('/')
# def home():
#     return render_template("index.html")

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个user的变量
            setattr(g,"user",user)
            g.user = user
        except:
            g.user = None


# 请求 ->before_request ->视图函数 ->context_processor
@app.context_processor
def context_processor():
    if hasattr(g,"user"):
        return {"user":g.user}
    else:
        return {}


if __name__ == "__main__":
    app.debug = True
    app.run()