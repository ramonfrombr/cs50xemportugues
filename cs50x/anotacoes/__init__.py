from flask import Blueprint, render_template


anotacoes_bp = Blueprint(
    'anotacoes',
    __name__,
    template_folder='templates'
)


from . import rotas