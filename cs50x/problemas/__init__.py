from flask import Blueprint


problemas_bp = Blueprint(
    'problemas',
    __name__,
    template_folder='templates'
)


from . import rotas