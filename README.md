# Desvia

Global Solution 2026.2 | CitizenTech | Computational Thinking with Python | FIAP

## Ficha da CitizenTech

| Campo | Resposta |
|---|---|
| Nome da CitizenTech | Desvia |
| Cidade e bairro | São Paulo, região da Paulista |
| Cidadão beneficiado | Quem usa transporte público todo dia no mesmo trajeto, como estudantes e trabalhadores |
| Problema, em uma frase | Quando o transporte do trajeto habitual falha, a pessoa descobre tarde e não sabe qual alternativa é a melhor |
| Como funciona | A pessoa cadastra o trajeto e a rota que costuma fazer. O Desvia compara essa rota com as alternativas, considerando atrasos e interrupções, e avisa quando vale desviar |
| O que cada parte faz | Python: lógica, comparação de rotas e persistência em JSON |
| Link do repositório | https://github.com/dudsbtw/gs-ctwp-desvia |
| Indicador de impacto | Minutos economizados por desvio sugerido |
| ODS conectados | ODS 11 (cidades e comunidades sustentáveis), pela mobilidade urbana acessível e eficiente |

Integrantes:

- Eduardo Felix Frois Silva, RM 574103
- Gabriel Henrique Ongarelli Reis, RM 572636
- Lucas Rodrigues dos Santos, RM 571778
- Matheus de Amorim Brito, RM 572435
- Vinicius Scalone Ramires, RM 573783

## Diferença para apps como o Moovit

O Desvia não planeja viagens do zero. Ele parte do trajeto fixo da pessoa e só entra em ação quando o serviço falha, mostrando o plano B.

## Dados simulados

Não existe feed em tempo real neste protótipo. Rotas, chegadas e interrupções estão em `dados_simulados.json` e aparecem marcados como `[SIMULADO]` no programa. Os relatos digitados pelo usuário ficam em `usuario.json` e são identificados como "relato seu".

## Como rodar

Precisa do Python 3.10 ou superior (usa `match/case`). Sem bibliotecas externas.

```
python desvia.py
```

Mantenha `desvia.py` e `dados_simulados.json` na mesma pasta.

## Menu

1. Cadastrar trajeto habitual
2. Ver status e chegadas
3. Comparar rotas e ver o desvio
4. Registrar interrupção
5. Apagar meus relatos
0. Sair

## Requisitos da disciplina

| Requisito | Onde aparece |
|---|---|
| Menu de opções | `main` e `mostrar_menu` |
| Validação de entradas | `ler_inteiro` e `ler_texto` |
| try/except | leitura de números, `carregar_json` e `salvar_json` |
| if/elif/else e match/case | `classificar_status` e menu em `main` |
| while e for | menu e leituras com while, listagens com for |
| Funções com parâmetros e retorno | todas as funções de apoio |
| Listas, tuplas e dicionários | rotas (lista), `obter_par` (tupla), trajetos e relatos (dicionários) |
| JSON | `dados_simulados.json` (leitura) e `usuario.json` (leitura e gravação) |

Uso de IA documentado em `prompts.md`.