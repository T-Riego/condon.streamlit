import copy

APARTAMENTOS = [
    "201", "202", "301", "302",
    "401", "402", "501", "502",
    "601", "602", "701", "702",
    "801", "802",
]

MORADORES = {
    "201": "Lucas",
    "202": "—",
    "301": "—",
    "302": "—",
    "401": "—",
    "402": "—",
    "501": "—",
    "502": "—",
    "601": "—",
    "602": "—",
    "701": "—",
    "702": "—",
    "801": "Alberto J. de Souza",
    "802": "—",
}

# Leituras anteriores (inventadas para permitir cálculo de consumo na tela)
LEITURAS_ANTERIORES = {
    "201": {"agua": 312.114, "gas_apt": 87.000, "gas_piscina": 52.000},
    "202": {"agua": 283.237, "gas": 145.259},
    "301": {"agua": 198.241, "gas": 87.941},
    "302": {"agua": 441.012, "gas": 210.571},
    "401": {"agua": 356.441, "gas": 78.586},
    "402": {"agua": 279.223, "gas": 131.180},
    "501": {"agua": 412.579, "gas": 52.787},
    "502": {"agua": 187.559, "gas": 98.971},
    "601": {"agua": 521.021, "gas": 44.418},
    "602": {"agua": 318.318, "gas": 82.870},
    "701": {"agua": 243.542, "gas": 62.215},
    "702": {"agua": 391.810, "gas": 111.239},
    "801": {"agua": 276.469, "gas": 54.577},
    "802": {"agua": 349.891, "gas": 148.560},
}

# Leituras atuais de Abril/2026 = anterior + consumo
def _atual(ap_key, tipo):
    ant = LEITURAS_ANTERIORES[ap_key]
    consumo_key = tipo if tipo in ant else tipo
    ant_val = ant.get(tipo, 0.0)
    consumo = CONSUMOS_ABRIL_2026[ap_key].get(
        tipo,
        CONSUMOS_ABRIL_2026[ap_key].get("gas", 0.0)
    )
    return round(ant_val + consumo, 3)

CONSUMOS_ABRIL_2026 = {
    "201":  {"agua": 21.886, "gas_apt": 0.000, "gas_piscina": 0.000},
    "202":  {"agua": 16.763, "gas": 2.741},
    "301":  {"agua": 19.759, "gas": 4.059},
    "302":  {"agua": 19.988, "gas": 2.429},
    "401":  {"agua": 25.559, "gas": 1.414},
    "402":  {"agua": 23.777, "gas": 4.820},
    "501":  {"agua": 25.421, "gas": 1.213},
    "502":  {"agua": 13.441, "gas": 1.029},
    "601":  {"agua":  3.979, "gas": 0.582},
    "602":  {"agua":  0.682, "gas": 0.130},
    "701":  {"agua": 13.458, "gas": 0.785},
    "702":  {"agua":  7.190, "gas": 3.761},
    "801":  {"agua":  4.531, "gas": 0.423},
    "802":  {"agua": 14.109, "gas": 2.440},
    "COND": {"agua": 18.457},
}

VALORES_ABRIL_2026 = [
    {"ap": "201", "agua_m3": 21.886, "agua_r": 281.88, "gas_m3": 0.000, "gas_r":   0.00, "rateio": 462.74, "total": 745},
    {"ap": "202", "agua_m3": 16.763, "agua_r": 215.24, "gas_m3": 2.741, "gas_r": 103.82, "rateio": 462.74, "total": 782},
    {"ap": "301", "agua_m3": 19.759, "agua_r": 253.65, "gas_m3": 4.059, "gas_r": 153.73, "rateio": 462.74, "total": 871},
    {"ap": "302", "agua_m3": 19.988, "agua_r": 256.59, "gas_m3": 2.429, "gas_r":  92.00, "rateio": 462.74, "total": 812},
    {"ap": "401", "agua_m3": 25.559, "agua_r": 329.05, "gas_m3": 1.414, "gas_r":  53.56, "rateio": 462.74, "total": 846},
    {"ap": "402", "agua_m3": 23.777, "agua_r": 305.87, "gas_m3": 4.820, "gas_r": 182.56, "rateio": 462.74, "total": 952},
    {"ap": "501", "agua_m3": 25.421, "agua_r": 326.78, "gas_m3": 1.213, "gas_r":  45.94, "rateio": 462.74, "total": 836},
    {"ap": "502", "agua_m3": 13.441, "agua_r": 173.17, "gas_m3": 1.029, "gas_r":  38.97, "rateio": 462.74, "total": 675},
    {"ap": "601", "agua_m3":  3.979, "agua_r":  50.68, "gas_m3": 0.582, "gas_r":  22.04, "rateio": 462.74, "total": 536},
    {"ap": "602", "agua_m3":  0.682, "agua_r":   8.79, "gas_m3": 0.130, "gas_r":   4.92, "rateio": 462.74, "total": 477},
    {"ap": "701", "agua_m3": 13.458, "agua_r": 173.29, "gas_m3": 0.785, "gas_r":  29.73, "rateio": 462.74, "total": 666},
    {"ap": "702", "agua_m3":  7.190, "agua_r":  91.93, "gas_m3": 3.761, "gas_r": 142.45, "rateio": 462.74, "total": 698},
    {"ap": "801", "agua_m3":  4.531, "agua_r":  58.51, "gas_m3": 0.423, "gas_r":  16.02, "rateio": 462.74, "total": 538},
    {"ap": "802", "agua_m3": 14.109, "agua_r": 181.86, "gas_m3": 2.440, "gas_r":  92.42, "rateio": 462.74, "total": 738},
]

COPASA_ABRIL_2026 = {
    "consumo_total_m3": 229.000,
    "valor_agua":        1950.00,
    "valor_esgoto":       620.00,
    "valor_recurso":      187.65,
    "valor_total":       2757.65,
    "custo_por_m3":        12.04,
    "data_vencimento":  "2026-05-15",
}

# Total despesas = R$ 4.065,65
DESPESAS_ABRIL_2026 = [
    {"id": 1, "descricao": "Manutenção Elevador (NF)",  "valor": 1500.00, "tipo": "NF",            "rateavel": True,  "base": 14},
    {"id": 2, "descricao": "Conservadora (NF)",          "valor":  800.00, "tipo": "NF",            "rateavel": True,  "base": 14},
    {"id": 3, "descricao": "CEMIG — Energia Elétrica",   "valor":  542.77, "tipo": "outros",        "rateavel": True,  "base": 14},
    {"id": 4, "descricao": "Seguro Predial",              "valor":  350.00, "tipo": "seguro",        "rateavel": True,  "base": 14},
    {"id": 5, "descricao": "Pró-labore Síndico",          "valor":  290.40, "tipo": "sindico",       "rateavel": False, "base": 13},
    {"id": 6, "descricao": "Fundo de Reserva",            "valor":  150.00, "tipo": "fundo_reserva", "rateavel": True,  "base": 14},
    {"id": 7, "descricao": "Material de Limpeza",         "valor":  182.48, "tipo": "outros",        "rateavel": True,  "base": 14},
    {"id": 8, "descricao": "Dedetização (NF)",            "valor":  250.00, "tipo": "NF",            "rateavel": True,  "base": 14},
]

PAGAMENTOS_ABRIL_2026 = {
    "201": {"pago": True,  "valor_pago": 745,  "data": "2026-04-30", "forma": "pix",  "recibo": "001/2026", "enviado": True},
    "202": {"pago": True,  "valor_pago": 782,  "data": "2026-05-02", "forma": "pix",  "recibo": "002/2026", "enviado": True},
    "301": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "302": {"pago": True,  "valor_pago": 812,  "data": "2026-05-01", "forma": "pix",  "recibo": "004/2026", "enviado": True},
    "401": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "402": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "501": {"pago": True,  "valor_pago": 836,  "data": "2026-04-29", "forma": "pix",  "recibo": "007/2026", "enviado": True},
    "502": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "601": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "602": {"pago": True,  "valor_pago": 477,  "data": "2026-05-03", "forma": "pix",  "recibo": "010/2026", "enviado": False},
    "701": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "702": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "801": {"pago": False, "valor_pago": None, "data": None,         "forma": None,   "recibo": None,        "enviado": False},
    "802": {"pago": True,  "valor_pago": 738,  "data": "2026-05-01", "forma": "pix",  "recibo": "014/2026", "enviado": True},
}

FUNDO_RESERVA_SALDO = 40130.60

HISTORICO = [
    {"ano_mes": "202604", "display": "Abr/2026", "total": 10172, "pagos": 6,  "pendentes": 8,  "status": "aberta"},
    {"ano_mes": "202603", "display": "Mar/2026", "total": 10380, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202602", "display": "Fev/2026", "total": 10210, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202601", "display": "Jan/2026", "total": 10590, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202512", "display": "Dez/2025", "total": 11200, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202511", "display": "Nov/2025", "total": 10820, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202510", "display": "Out/2025", "total": 10650, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202509", "display": "Set/2025", "total": 10430, "pagos": 14, "pendentes": 0,  "status": "fechada"},
    {"ano_mes": "202508", "display": "Ago/2025", "total": 10780, "pagos": 14, "pendentes": 0,  "status": "fechada"},
]

CHECKLIST_ITENS = [
    "Todas as leituras de água registradas (15 medidores)",
    "Todas as leituras de gás registradas (15 medidores)",
    "Conta COPASA lançada",
    "Despesas do mês lançadas",
    "Cálculos conferidos — soma dos totais bate com total geral",
    "Planilhas PDF geradas",
    "Recibos PDF gerados",
    "Pagamentos registrados",
    "Recibos enviados a todos os condôminos",
    "Competência fechada",
]


def init_session_state(state):
    if "leituras" not in state:
        state["leituras"] = copy.deepcopy(CONSUMOS_ABRIL_2026)
    if "despesas" not in state:
        state["despesas"] = copy.deepcopy(DESPESAS_ABRIL_2026)
    if "copasa" not in state:
        state["copasa"] = copy.deepcopy(COPASA_ABRIL_2026)
    if "pagamentos" not in state:
        state["pagamentos"] = copy.deepcopy(PAGAMENTOS_ABRIL_2026)
    if "checklist" not in state:
        state["checklist"] = {item: (i < 3) for i, item in enumerate(CHECKLIST_ITENS)}
    if "competencia_status" not in state:
        state["competencia_status"] = "aberta"
    if "despesa_next_id" not in state:
        state["despesa_next_id"] = len(DESPESAS_ABRIL_2026) + 1
