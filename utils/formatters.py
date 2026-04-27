def brl(value) -> str:
    """Formata valor como moeda brasileira: R$ 1.234,56"""
    if value is None:
        return "—"
    return f"R$ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def m3(value, decimals=3) -> str:
    """Formata consumo em m³ com vírgula decimal."""
    if value is None:
        return "—"
    fmt = f"{float(value):.{decimals}f}".replace(".", ",")
    return f"{fmt} m³"


def status_badge(status: str) -> str:
    cores = {
        "aberta":    ("🟡", "#F39C12", "Aberta"),
        "conferida": ("🔵", "#2E86AB", "Conferida"),
        "fechada":   ("🟢", "#27AE60", "Fechada"),
    }
    emoji, cor, label = cores.get(status, ("⚪", "#999", status))
    return f'<span style="color:{cor};font-weight:600">{emoji} {label}</span>'


def pagamento_badge(pago: bool) -> str:
    if pago:
        return '<span style="color:#27AE60;font-weight:600">✅ Pago</span>'
    return '<span style="color:#E74C3C;font-weight:600">⏳ Pendente</span>'
