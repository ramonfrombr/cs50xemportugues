from flask import Blueprint, render_template
from . import anotacoes_bp as bp


@bp.route('/')
@bp.route('/index.html')
def anotacoes():
    return render_template('anotacoes/index.html')


@bp.route('/0')
@bp.route('/0.html')
def anotacoes0():
    return render_template('anotacoes/0.html')


@bp.route('/1')
@bp.route('/1.html')
def anotacoes1():
    return render_template('anotacoes/1.html')
    

@bp.route('/2')
@bp.route('/2.html')
def anotacoes2():
    return render_template('anotacoes/2.html')


@bp.route('/3')
@bp.route('/3.html')
def anotacoes3():
    return render_template('anotacoes/3.html')
    

@bp.route('/4')
@bp.route('/4.html')
def anotacoes4():
    return render_template('anotacoes/4.html')


@bp.route('/5')
@bp.route('/5.html')
def anotacoes5():
    return render_template('anotacoes/5.html')


@bp.route('/6')
@bp.route('/6.html')
def anotacoes6():
    return render_template('anotacoes/6.html')


@bp.route('/7')
@bp.route('/7.html')
def anotacoes7():
    return render_template('anotacoes/7.html')


@bp.route('/8')
@bp.route('/8.html')
def anotacoes8():
    return render_template('anotacoes/8.html')


@bp.route('/9')
@bp.route('/9.html')
def anotacoes9():
    return render_template('anotacoes/9.html')


