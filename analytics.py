ANALYTICS_LIST = {
    "qualAnalytics": [
        {"name": "Código da melhor submissão", "type": "URL"},
        {"name": "Histórico de submissões", "type": "URL"},
        {"name": "Última mensagem de erro", "type": "text/plain"},
    ],
    "quantAnalytics": [
        {"name": "Acedeu à atividade", "type": "boolean"},
        {"name": "Começou a programar", "type": "boolean"},
        {"name": "Desafio concluído", "type": "boolean"},
        {"name": "Execuções de testes públicos", "type": "integer"},
        {"name": "Submissões", "type": "integer"},
        {"name": "Erros de sintaxe/execução", "type": "integer"},
        {"name": "Dicas consultadas", "type": "integer"},
        {"name": "Testes públicos passados (%)", "type": "integer"},
        {"name": "Testes ocultos passados (%)", "type": "integer"},
        {"name": "Pontuação final (%)", "type": "integer"},
        {"name": "Tempo ativo na atividade (min)", "type": "integer"},
    ],
}

_EXEMPLOS = {
    "1001": {
        "quant": [True, True, True, 7, 2, 3, 1, 100, 100, 90, 23],
        "erro": "TypeError: lista.filter is not a function (linha 2)",
    },
    "1002": {
        "quant": [True, False, False, 0, 0, 0, 0, 0, 0, 0, 2],
        "erro": "",
    },
}


def analytics_de_exemplo(base_url: str, activity_id: str) -> list[dict]:
    """Build sample analytics for every student of an activity instance."""
    resultado = []
    for std_id, ex in _EXEMPLOS.items():
        quant = [
            {**definicao, "value": valor}
            for definicao, valor in zip(ANALYTICS_LIST["quantAnalytics"], ex["quant"])
        ]
        prefixo = f"{base_url}/desafio/{activity_id}/analytics/{std_id}"
        qual = [
            {"name": "Código da melhor submissão", "type": "URL", "value": f"{prefixo}/codigo"},
            {"name": "Histórico de submissões", "type": "URL", "value": f"{prefixo}/historico"},
            {"name": "Última mensagem de erro", "type": "text/plain", "value": ex["erro"]},
        ]
        resultado.append({"inveniraStdID": std_id, "quantAnalytics": quant, "qualAnalytics": qual})
    return resultado


_SUBMISSOES = {
    "1001": [
        {
            "data": "2026-11-20 10:12",
            "resultado": "1 de 3 testes ocultos",
            "codigo": "function somaPares(lista) {\n  return lista.filter(n => n % 2 == 0).length;\n}",
        },
        {
            "data": "2026-11-20 10:31",
            "resultado": "3 de 3 testes ocultos",
            "codigo": "function somaPares(lista) {\n  let soma = 0;\n  for (const n of lista) {\n    if (n % 2 === 0) soma += n;\n  }\n  return soma;\n}",
        },
    ],
    "1002": [],
}


def submissoes_de_exemplo(std_id: str) -> list[dict] | None:
    """Return a student's sample submissions, oldest first, or None if unknown."""
    return _SUBMISSOES.get(std_id)
