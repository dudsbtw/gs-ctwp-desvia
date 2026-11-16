# Uso de IA no projeto Desvia

Integrantes:

- Eduardo Felix Frois Silva, RM 574103
- Gabriel Henrique Ongarelli Reis, RM 572636
- Lucas Rodrigues dos Santos, RM 571778
- Matheus de Amorim Brito, RM 572435
- Vinicius Scalone Ramires, RM 573783

## Ferramentas utilizadas
 
- Claude (Anthropic): apoio na definição do foco do projeto, em dúvidas de sintaxe, em trechos de código e na revisão dos requisitos da disciplina.

## Prompts utilizados
 
1. "Desenvolva o protótipo de mobilidade CitizenTech que discutimos para a Solução Global da FIAP. Diferencie claramente o conceito do Moovit, concentrando-se na ideia mais específica de CitizenTech do grupo. Crie a menor experiência interativa útil possível, na qual seja possível comparar rotas, visualizar informações simuladas de chegada e interrupções no serviço, e compreender o valor diferenciado do projeto. Nome do projeto: Desvia."
2. "Como funciona o match/case do Python 3.10? Me dá um exemplo simples com um menu de opções."
3. "Como pedir um número inteiro ao usuário e repetir a pergunta enquanto ele digitar algo inválido ou fora de um intervalo?"
4. "Qual a sintaxe para ler e gravar um arquivo JSON em Python? Quais exceções tratar se o arquivo não existir ou estiver corrompido?"
5. "Faça uma análise dos requisitos pedidos no documento e do que foi entregue no projeto, indicando quais foram cumpridos."

## Funcionalidades desenvolvidas com auxílio da IA
 
A IA e o grupo trabalharam juntos na construção do código:
 
- Foco do projeto: a IA ajudou a definir o Desvia como plano B para quem tem trajeto fixo, e o grupo escolheu os trajetos e o público.
- Menu com match/case: a IA sugeriu a estrutura, e o grupo adaptou as opções ao projeto.
- Validação de entradas e tratamento de exceções: a IA mostrou o padrão com while e try/except, e o grupo aplicou nos campos do programa.
- Persistência em JSON: a IA explicou a leitura e a gravação, e o grupo definiu quais dados são salvos.
- Dados simulados: a IA ajudou a estruturar o arquivo, e o grupo revisou rotas, tempos e interrupções.

## Como o grupo verificou, testou e ajustou
 
- O grupo executou o programa e testou opções inválidas, texto no lugar de número, valores fora do intervalo e arquivo JSON ausente ou com formato inválido.
- Trechos que o grupo não entendeu foram refeitos ou explicados com novas perguntas à IA.
- A comparação de rotas foi conferida à mão, somando tempo e atraso de cada rota.

## Análise crítica
 
A IA acelerou a estrutura do programa e a conferência dos requisitos, e ajudou a esclarecer sintaxe nova. As limitações são que os dados de rotas e tempos são inventados e que as sugestões precisaram ser conferidas com o conteúdo visto em aula. A principal dificuldade foi adaptar as respostas ao projeto e entender cada trecho antes de usar.