from flask import render_template
from . import cs50x as bp



@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('index.html')


@bp.route('/perguntas_frequentes')
@bp.route('/perguntas_frequentes.html')
def perguntas_frequentes():
    return render_template('perguntas_frequentes.html')


@bp.route('/certificado')
@bp.route('/certificado.html')
def certificado():
    return render_template('certificado.html')


@bp.route('/curriculo')
@bp.route('/curriculo.html')
def curriculo():
    return render_template('curriculo.html')


@bp.route('/equipe')
@bp.route('/equipe.html')
def equipe():
    return render_template('equipe.html')


@bp.route('/obrigado')
@bp.route('/obrigado.html')
def obrigado():
    return render_template('obrigado.html')


@bp.route('/projeto_final')
@bp.route('/projeto_final.html')
def projeto_final():
    return render_template('projeto_final.html')


@bp.route('/secoes')
@bp.route('/secoes.html')
def secoes():
    return render_template('secoes.html')


@bp.route('/tutorias')
@bp.route('/tutorias.html')
def tutorias():
    return render_template('tutorias.html')


@bp.route('/especializacoes')
@bp.route('/especializacoes.html')
def especializacoes():
    return render_template('especializacoes.html')


@bp.route('/guiadeestilo')
@bp.route('/guiadeestilo.html')
def guia_de_estilo():
    return render_template('guiadeestilo.html')
