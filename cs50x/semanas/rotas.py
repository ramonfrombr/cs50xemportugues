from flask import Blueprint, render_template
from . import semanas_bp as bp


@bp.route('/')
@bp.route('/index.html')
def semanas():
    return render_template('semanas/index.html')


@bp.route('/0')
@bp.route('/0.html')
def semana0():
    return render_template('semanas/0.html')


@bp.route('/1')
@bp.route('/1.html')
def semana1():
    return render_template('semanas/1.html')


@bp.route('/2')
@bp.route('/2.html')
def semana2():
    return render_template('semanas/2.html')
    
    
@bp.route('/3')
@bp.route('/3.html')
def semana3():
    return render_template('semanas/3.html')
    

@bp.route('/4')
@bp.route('/4.index.html')
def semana4():
    return render_template('semanas/4.html')
    

@bp.route('/5')
@bp.route('/5.html')
def semana5():
    return render_template('semanas/5.html')
    

@bp.route('/6')
@bp.route('/6.html')
def semana6():
    return render_template('semanas/6.html')
    

@bp.route('/7')
@bp.route('/7.html')
def semana7():
    return render_template('semanas/7.html')
    
    
@bp.route('/8')
@bp.route('/8.html')
def semana8():
    return render_template('semanas/8.html')
    
@bp.route('/9')
@bp.route('/9.html')
def semana9():
    return render_template('semanas/9.html')
    
