from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP


def excel_round(value, decimals: int) -> Decimal:
    """Equivalente ao ROUND() do Excel."""
    v = Decimal(str(value))
    q = Decimal(10) ** -decimals
    return v.quantize(q, rounding=ROUND_HALF_UP)


def excel_rounddown(value, decimals: int) -> Decimal:
    """Equivalente ao ROUNDDOWN() do Excel — trunca."""
    v = Decimal(str(value))
    q = Decimal(10) ** -decimals
    return v.quantize(q, rounding=ROUND_DOWN)


def excel_roundup(value, decimals: int) -> Decimal:
    """Equivalente ao ROUNDUP() do Excel — arredonda para cima."""
    v = Decimal(str(value))
    q = Decimal(10) ** -decimals
    return v.quantize(q, rounding=ROUND_UP)


def calc_total(agua_esgoto, gas, rateio) -> Decimal:
    """Total a pagar = ROUNDUP(agua_esgoto + gas + rateio, 0) — sem centavos."""
    soma = Decimal(str(agua_esgoto)) + Decimal(str(gas)) + Decimal(str(rateio))
    return excel_roundup(soma, 0)


def calc_rateio(total_despesas, fundo_reserva=Decimal("150.00")):
    """Retorna (parcial, sindico, fundo, final)."""
    parcial = excel_round(Decimal(str(total_despesas)) / 14, 2)
    sindico = excel_round(parcial / 13, 2)
    fundo = Decimal(str(fundo_reserva))
    final = parcial + sindico + fundo
    return parcial, sindico, fundo, final
