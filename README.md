# Activity Provider "Desafio de Programação" (Inven!RA)

Projeto da UC Arquitetura e Padrões de Software (UAb, 2026). Semana 1 do Tópico 4: Web services RESTful que respondem, com dados de exemplo, aos cinco pedidos da Inven!RA.

| Pedido | Método | URL |
|---|---|---|
| Ficheiro de registo | GET | `/` |
| config_url | GET | `/desafio/configuracao` |
| json_params_url | GET | `/desafio/json-params` |
| user_url (deploy) | GET | `/desafio/deploy?activityID=<id>` |
| analytics_list_url | GET | `/desafio/analytics-list` |
| analytics_url | POST | `/desafio/analytics` com `{"activityID": "<id>"}` |

O serviço "Provide activity" (`/desafio/<activityID>`) ainda não está implementado nesta fase.

Executar localmente: `pip install -r requirements.txt` e depois `python app.py`.
