from flask import Blueprint, render_template
from . import problemas_bp as bp


@bp.route('/')
@bp.route('/index.html')
def problemas():
    return render_template('problemas/index.html')

#############################################################################
#############################################################################
#############################################################################

@bp.route('/0')
@bp.route('/0.html')
def problemas0():
    return render_template('problemas/0.html')

@bp.route('/0/scratch')
@bp.route('/0/scratch.html')
def scratch():
    return render_template('problemas/scratch.html')


#############################################################################
#############################################################################
#############################################################################


@bp.route('/1')
@bp.route('/1.html')
def problemas1():
    return render_template('problemas/1.html')

@bp.route('/1/ola')
@bp.route('/1/ola.html')
def ola():
    return render_template('problemas/ola.html')

@bp.route('/1/mario/menos')
@bp.route('/1/mario/menos.html')
def mario_menos():
    return render_template('problemas/mario_menos.html')

@bp.route('/1/mario/mais')
@bp.route('/1/mario/mais.html')
def mario_mais():
    return render_template('problemas/mario_mais.html')

@bp.route('/1/dinheiro')
@bp.route('/1/dinheiro.html')
def dinheiro():
    return render_template('problemas/dinheiro.html')

@bp.route('/1/credito')
@bp.route('/1/credito.html')
def credito():
    return render_template('problemas/credito.html')


#############################################################################
#############################################################################
#############################################################################



@bp.route('/2')
@bp.route('/2.html')
def problemas2():
    return render_template('problemas/2.html')


@bp.route('/2/legibilidade')
@bp.route('/2/legibilidade.html')
def legibilidade():
    return render_template('problemas/legibilidade.html')


@bp.route('/2/cesar')
@bp.route('/2/cesar.html')
def cesar():
    return render_template('problemas/cesar.html')


@bp.route('/2/substituicao')
@bp.route('/2/substituicao.html')
def substituicao():
    return render_template('problemas/substituicao.html')


#############################################################################
#############################################################################
#############################################################################


@bp.route('/3')
@bp.route('/3.html')
def problemas3():
    return render_template('problemas/3.html')

@bp.route('/3/pluralidade')
@bp.route('/3/pluralidade.html')
def pluralidade():
    return render_template('problemas/pluralidade.html')


@bp.route('/3/preferencia')
@bp.route('/3/preferencia.html')
def preferencia():
    return render_template('problemas/preferencia.html')

@bp.route('/3/pares_ranqueados')
@bp.route('/3/pares_ranqueados.html')
def pares_ranqueados():
    return render_template('problemas/pares_ranqueados.html')

#############################################################################
#############################################################################
#############################################################################


@bp.route('/4')
@bp.route('/4.html')
def problemas4():
    return render_template('problemas/4.html')

@bp.route('/4/filtro/menos')
@bp.route('/4/filtro/menos.html')
def filtro_menos():
    return render_template('problemas/filtro_menos.html')


@bp.route('/4/filtro/mais')
@bp.route('/4/filtro/mais.html')
def filtro_mais():
    return render_template('problemas/filtro_mais.html')


@bp.route('/4/recuperar')
@bp.route('/4/recuperar.html')
def recuperar():
    return render_template('problemas/recuperar.html')


#############################################################################
#############################################################################
#############################################################################


@bp.route('/5')
@bp.route('/5.html')
def problemas5():
    return render_template('problemas/5.html')
    

@bp.route('/5/corretor')
@bp.route('/5/corretor.html')
def corretor():
    return render_template('problemas/corretor.html')


#############################################################################
#############################################################################
#############################################################################


@bp.route('/6')
@bp.route('/6.html')
def problemas6():
    return render_template('problemas/6.html')
    
@bp.route('/6/ola')
@bp.route('/6/ola.html')
def ola_python():
    return render_template('problemas/ola_python.html')
 
@bp.route('/6/mario/menos')
@bp.route('/6/mario/menos.html')
def mario_menos_python():
    return render_template('problemas/mario_menos_python.html')

@bp.route('/6/mario/mais')
@bp.route('/6/mario/mais.html')
def mario_mais_python():
    return render_template('problemas/mario_mais_python.html')

@bp.route('/6/dinheiro')
@bp.route('/6/dinheiro.html')
def dinheiro_python():
    return render_template('problemas/dinheiro_python.html')

@bp.route('/6/credito')
@bp.route('/6/credito.html')
def credito_python():
    return render_template('problemas/credito_python.html')

@bp.route('/6/legibilidade')
@bp.route('/6/legibilidade.html')
def legibilidade_python():
    return render_template('problemas/legibilidade_python.html')

@bp.route('/6/dna')
@bp.route('/6/dna.html')
def dna():
    return render_template('problemas/dna.html')


#############################################################################
#############################################################################
#############################################################################


@bp.route('/7')
@bp.route('/7.html')
def problemas7():
    return render_template('problemas/7.html')

   
@bp.route('/7/filmes')
@bp.route('/7/filmes.html')
def filmes():
    return render_template('problemas/filmes.html')

   
@bp.route('/7/vila_cinquenta')
@bp.route('/7/vila_cinquenta.html')
def vila_cinquenta():
    return render_template('problemas/vila_cinquenta.html')
   

#############################################################################
#############################################################################
#############################################################################


@bp.route('/8')
@bp.route('/8.html')
def problemas8():
    return render_template('problemas/8.html')
    
   
@bp.route('/8/pagina_inicial')
@bp.route('/8/pagina_inicial.html')
def pagina_inicial():
    return render_template('problemas/pagina_inicial.html')
   

#############################################################################
#############################################################################
#############################################################################


@bp.route('/9')
@bp.route('/9.html')
def problemas9():
    return render_template('problemas/9.html')
   
@bp.route('/9/financas')
@bp.route('/9/financas.html')
def financas():
    return render_template('problemas/financas.html')
   



