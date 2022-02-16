from flask import Blueprint, render_template
from . import topicos_bp as bp


@bp.route('/')
@bp.route('/index.html')
def topicos():
    return render_template('topicos/index.html')
