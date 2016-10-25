# -*- coding: utf-8 -*-
from datetime import date, timedelta


def _calcular_pascoa(ano: int) -> date:
    a = ano % 19
    b = ano >> 2
    c = b // 25 + 1
    d = (c * 3) >> 2
    e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
    e += (29578 - a - e * 32) >> 10
    e -= ((ano % 7) + b - d + e + 2) % 7
    d = e >> 5
    day = e - d * 31
    month = d + 3
    return date(ano, month, day)


def dia_util(data: date, feriados_opcionais=None, eliminar_dias=[6, 7]) -> bool:
    """Os dias passados na variável eliminar_dias devem obedecer o padrão date
    do Python onde 1 -> Domingo, 2 -> Segunda-feira, etc"""
    pascoa = _calcular_pascoa(data.year)
    ano_novo = date(data.year, 1, 1)
    tiradentes = date(data.year, 4, 21)
    trabalhador = date(data.year, 5, 1)
    independencia = date(data.year, 9, 7)
    n_s_aparecida = date(data.year, 10, 12)
    finados = date(data.year, 11, 2)
    republica = date(data.year, 11, 15)
    natal = date(data.year, 12, 25)
    carnaval_segunda = pascoa - timedelta(days=48)
    carnaval_terca = carnaval_segunda + timedelta(days=1)
    sexta_feira_santa = pascoa - timedelta(days=2)
    corpus_christi = pascoa + timedelta(days=60)
    feriados = feriados_opcionais if feriados_opcionais else []
    feriados += [pascoa,
                 ano_novo,
                 tiradentes,
                 trabalhador,
                 independencia,
                 n_s_aparecida,
                 finados,
                 republica,
                 natal,
                 carnaval_segunda,
                 carnaval_terca,
                 sexta_feira_santa,
                 corpus_christi]
    if eliminar_dias:
        return not (data in feriados or data.isoweekday() in eliminar_dias)
    else:
        return not (data in feriados)
