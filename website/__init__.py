from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'asdasfdgsfadfadgasfgafdbadfvdsvadfvsdAASDFASDFAV'

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
    return app