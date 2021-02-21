from flask import (
    Blueprint, render_template, request
)
from ComedorManager.models import Comedor, save_item

comedor_heads = {
    "empresa": "Empresa", "semana": "Semana", "gastos": "Gastos",
    "ventas": "Ventas", "impuesto": "Impuesto", "total": "Total Factura"
    }

bp = Blueprint('comedor', __name__)


@bp.route('/')
def comedores():
    comedores = Comedor.query.all()
    
    return render_template(
        'comedor/comedores.html', heads=comedor_heads, comedores=comedores
        )


@bp.route('/add_comedor', methods=('GET', 'POST'))
def add_comedor():
    add_heads = {}
    for head in comedor_heads:
        if head != "semana":
            add_heads[head] = comedor_heads[head]

    if request.method == "POST":
        comedor = Comedor(
            empresa = request.form['empresa'],
            gastos = request.form['gastos'],
            ventas = request.form['ventas'],
            impuesto = request.form['impuesto'],
            total = request.form['total']
        )
        save_item(comedor)

    return render_template(
        'comedor/add_comedor.html', heads=add_heads
    )
