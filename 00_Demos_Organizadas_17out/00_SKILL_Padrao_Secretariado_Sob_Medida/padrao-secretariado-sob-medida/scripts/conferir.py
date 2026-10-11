#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conferências rápidas e exatas para documentos de secretariado.

Datas, somas e horários não devem depender da "intuição" do modelo:
este script faz a conta e mostra o resultado para citar no documento.

Uso:
  python scripts/conferir.py dia 09/03/2027 12/03/2027
      -> dia da semana de cada data
  python scripts/conferir.py soma 4200 950 --teto 5000
      -> total, e folga ou excesso em relação ao teto
  python scripts/conferir.py horarios 10:10-10:40 11:30-12:00 --fixo 11:00-11:30 --limite 12:00
      -> duração de cada bloco, sobreposições e se tudo termina até o limite
"""
import argparse
import re
import sys
from datetime import date

DIAS = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]


def brl(valor):
    inteiro, centavos = f"{valor:,.2f}".split(".")
    return "R$ " + inteiro.replace(",", ".") + "," + centavos


def numero(texto):
    """Aceita 4200, 4.200, 4.200,00, R$ 4.200 e 4200.50."""
    t = texto.replace("R$", "").replace(" ", "")
    if "," in t:
        t = t.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", t):
        t = t.replace(".", "")
    return float(t)


def minutos(texto):
    """Aceita 10:10, 10h10, 11h e 11."""
    m = re.fullmatch(r"\s*(\d{1,2})(?:[:h](\d{2})?)?\s*", texto)
    if not m:
        raise ValueError(f"horário inválido: {texto}")
    return int(m.group(1)) * 60 + int(m.group(2) or 0)


def hhmm(total):
    return f"{total // 60:02d}h{total % 60:02d}"


def intervalo(texto):
    ini, fim = texto.split("-")
    a, b = minutos(ini), minutos(fim)
    if b <= a:
        raise ValueError(f"intervalo inválido: {texto}")
    return a, b


def cmd_dia(args):
    for d in args.datas:
        dd, mm, aa = (int(x) for x in d.split("/"))
        print(f"{d} = {DIAS[date(aa, mm, dd).weekday()]}")


def cmd_soma(args):
    valores = [numero(v) for v in args.valores]
    total = sum(valores)
    print(" + ".join(brl(v) for v in valores) + f" = {brl(total)}")
    if args.teto is not None:
        teto = numero(args.teto)
        diff = teto - total
        if diff >= 0:
            print(f"Dentro do teto de {brl(teto)}: folga de {brl(diff)}")
        else:
            print(f"ACIMA do teto de {brl(teto)}: excesso de {brl(-diff)}")


def cmd_horarios(args):
    blocos = [(t, *intervalo(t)) for t in args.blocos]
    fixos = [(t, *intervalo(t)) for t in (args.fixo or [])]
    problemas = 0
    for nome, a, b in blocos:
        print(f"Bloco {hhmm(a)}–{hhmm(b)}: {b - a} min")
    todos = blocos + [(f"FIXO {n}", a, b) for n, a, b in fixos]
    for i in range(len(todos)):
        for j in range(i + 1, len(todos)):
            n1, a1, b1 = todos[i]
            n2, a2, b2 = todos[j]
            if a1 < b2 and a2 < b1:
                problemas += 1
                print(f"SOBREPOSIÇÃO: {n1} e {n2} se sobrepõem")
    if args.inicio:
        ini = minutos(args.inicio)
        for nome, a, b in blocos:
            if a < ini:
                problemas += 1
                print(f"ANTES DO PERMITIDO: {nome} começa antes de {hhmm(ini)}")
    if args.limite:
        lim = minutos(args.limite)
        for nome, a, b in blocos:
            if b > lim:
                problemas += 1
                print(f"DEPOIS DO LIMITE: {nome} termina depois de {hhmm(lim)}")
    print("OK: nenhum conflito encontrado" if problemas == 0 else f"ATENÇÃO: {problemas} problema(s)")
    return problemas


def main():
    for fluxo in (sys.stdout, sys.stderr):  # acentos certos no terminal do Windows e em saídas redirecionadas
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="Conferências exatas de datas, valores e horários.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("dia", help="dia da semana de datas dd/mm/aaaa")
    p.add_argument("datas", nargs="+")
    p.set_defaults(f=cmd_dia)
    p = sub.add_parser("soma", help="soma valores e compara com um teto")
    p.add_argument("valores", nargs="+")
    p.add_argument("--teto")
    p.set_defaults(f=cmd_soma)
    p = sub.add_parser("horarios", help="duração, sobreposição e limites de blocos HH:MM-HH:MM")
    p.add_argument("blocos", nargs="+")
    p.add_argument("--fixo", action="append", help="compromisso que não pode ser sobreposto (repita se houver vários)")
    p.add_argument("--inicio", help="horário a partir do qual os blocos podem começar")
    p.add_argument("--limite", help="horário até o qual todos os blocos devem terminar")
    p.set_defaults(f=cmd_horarios)
    a = ap.parse_args()
    r = a.f(a)
    sys.exit(1 if r else 0)


if __name__ == "__main__":
    main()
