from flask import Blueprint, render_template


semanas_bp = Blueprint(
    'semanas',
    __name__,
    template_folder='templates'
)


from . import rotas