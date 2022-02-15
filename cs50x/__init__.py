from flask import Blueprint
from .semanas import semanas_bp
from .problemas import problemas_bp
from .anotacoes import anotacoes_bp


cs50x = Blueprint(
    'cs50x',
    __name__,
    template_folder='templates'
)


cs50x.register_blueprint(semanas_bp, url_prefix='/semanas')
cs50x.register_blueprint(problemas_bp, url_prefix='/problemas')
cs50x.register_blueprint(anotacoes_bp, url_prefix='/anotacoes')


from . import rotas