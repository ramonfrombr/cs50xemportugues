from flask import Blueprint, render_template


topicos_bp = Blueprint(
    'topicos',
    __name__,
    template_folder='templates'
)


from . import rotas