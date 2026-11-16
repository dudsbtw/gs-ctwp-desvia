import json

# nomes dos arquivos e limites usados no programa
ARQUIVO_DADOS = "dados_simulados.json"
ARQUIVO_USUARIO = "usuario.json"
ATRASO_MAXIMO = 180
TAG_SIMULADO = "[SIMULADO]"


# le um arquivo json e devolve o conteudo ou None se der erro
def carregar_json(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"O arquivo {caminho} está com formato inválido.")
        return None


# grava um dicionario em arquivo json e avisa se falhar
def salvar_json(caminho, dados):
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("Não foi possível salvar os dados.")
        return False


# carrega o perfil salvo do usuario ou cria um vazio
def carregar_usuario():
    vazio = {"trajeto_id": None, "rota_habitual": None, "relatos": []}
    usuario = carregar_json(ARQUIVO_USUARIO)
    if usuario is None:
        return vazio
    if not isinstance(usuario, dict):
        print(f"O arquivo {ARQUIVO_USUARIO} está com formato inválido.")
        return vazio
    for chave in vazio:
        if chave not in usuario:
            print(f"O arquivo {ARQUIVO_USUARIO} está incompleto.")
            return vazio
    return usuario


# pede um numero inteiro dentro do intervalo permitido
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Digite apenas números inteiros.")
            continue
        if valor < minimo or valor > maximo:
            print(f"Digite um número entre {minimo} e {maximo}.")
        else:
            return valor


# pede um texto com pelo menos 3 caracteres
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if len(texto) < 3:
            print("Escreva pelo menos 3 caracteres.")
        else:
            return texto


# procura um trajeto pelo id
def buscar_trajeto(dados, trajeto_id):
    for trajeto in dados["trajetos"]:
        if trajeto["id"] == trajeto_id:
            return trajeto
    return None


# devolve origem e destino do trajeto como tupla
def obter_par(trajeto):
    return (trajeto["origem"], trajeto["destino"])


# confere se ja existe trajeto cadastrado e devolve ele
def obter_trajeto_usuario(dados, usuario):
    if usuario["trajeto_id"] is None:
        print("Cadastre seu trajeto habitual primeiro (opção 1).")
        return None
    trajeto = buscar_trajeto(dados, usuario["trajeto_id"])
    if trajeto is None:
        print("O trajeto salvo não existe mais. Cadastre de novo.")
    return trajeto


# devolve o maior atraso, o motivo e a fonte das interrupcoes da linha
def calcular_atraso(linha, interrupcoes, relatos):
    atraso = 0
    motivo = ""
    fonte = ""
    for item in interrupcoes + relatos:
        if item["linha"] == linha and item["atraso_min"] > atraso:
            atraso = item["atraso_min"]
            motivo = item["motivo"]
            fonte = item["fonte"]
    return atraso, motivo, fonte


# monta a lista de rotas com o tempo total ja somado ao atraso
def montar_rotas(trajeto, interrupcoes, relatos):
    rotas = []
    for rota in trajeto["rotas"]:
        atraso, motivo, fonte = calcular_atraso(rota["linha"], interrupcoes, relatos)
        rotas.append({
            "nome": rota["nome"],
            "linha": rota["linha"],
            "custo": rota["custo"],
            "chegadas": rota["chegadas_min"],
            "atraso": atraso,
            "motivo": motivo,
            "fonte": fonte,
            "total": rota["tempo_min"] + atraso,
        })
    return rotas


# classifica a rota de acordo com o atraso
def classificar_status(atraso):
    if atraso == 0:
        return "Normal"
    elif atraso <= 10:
        return "Atraso leve"
    else:
        return "Interrompida"


# ordena as rotas pelo tempo total, da mais rapida para a mais lenta
def ordenar_rotas(rotas):
    ordenadas = rotas.copy()
    for i in range(len(ordenadas)):
        for j in range(len(ordenadas) - 1 - i):
            if ordenadas[j]["total"] > ordenadas[j + 1]["total"]:
                ordenadas[j], ordenadas[j + 1] = ordenadas[j + 1], ordenadas[j]
    return ordenadas


# procura uma rota pela linha
def encontrar_rota(rotas, linha):
    for rota in rotas:
        if rota["linha"] == linha:
            return rota
    return None


# monta o texto das proximas chegadas somando o atraso
def formatar_chegadas(chegadas, atraso):
    textos = []
    for minutos in chegadas:
        textos.append(f"{minutos + atraso} min")
    return ", ".join(textos)


# lista as rotas numeradas para o usuario escolher
def mostrar_lista_rotas(rotas):
    numero = 1
    for rota in rotas:
        print(f"{numero} - {rota['nome']}")
        numero += 1


# mostra as opcoes do menu
def mostrar_menu():
    print("\n===== DESVIA =====")
    print("Seu plano B quando o transporte falha")
    print("1 - Cadastrar trajeto habitual")
    print("2 - Ver status e chegadas")
    print("3 - Comparar rotas e ver o desvio")
    print("4 - Registrar interrupção")
    print("5 - Apagar meus relatos")
    print("0 - Sair")


# deixa o usuario escolher o trajeto e a rota que ele costuma fazer
def cadastrar_trajeto(dados, usuario):
    print(f"\nTrajetos disponíveis {TAG_SIMULADO}")
    for trajeto in dados["trajetos"]:
        origem, destino = obter_par(trajeto)
        print(f"{trajeto['id']} - {origem} para {destino}")
    trajeto_id = ler_inteiro("Escolha o trajeto: ", 1, len(dados["trajetos"]))
    trajeto = buscar_trajeto(dados, trajeto_id)
    print("\nQual rota você costuma fazer?")
    mostrar_lista_rotas(trajeto["rotas"])
    escolha = ler_inteiro("Escolha a rota: ", 1, len(trajeto["rotas"]))
    usuario["trajeto_id"] = trajeto_id
    usuario["rota_habitual"] = trajeto["rotas"][escolha - 1]["linha"]
    if salvar_json(ARQUIVO_USUARIO, usuario):
        print("Trajeto habitual salvo!")


# mostra status e proximas chegadas de cada rota do trajeto
def ver_status(dados, usuario):
    trajeto = obter_trajeto_usuario(dados, usuario)
    if trajeto is None:
        return
    origem, destino = obter_par(trajeto)
    rotas = montar_rotas(trajeto, dados["interrupcoes"], usuario["relatos"])
    print(f"\nStatus de {origem} para {destino} {TAG_SIMULADO}")
    for rota in rotas:
        marca = ""
        if rota["linha"] == usuario["rota_habitual"]:
            marca = " (sua rota)"
        print(f"\n{rota['nome']}{marca}")
        print(f"  Status: {classificar_status(rota['atraso'])}")
        print(f"  Próximas chegadas: {formatar_chegadas(rota['chegadas'], rota['atraso'])}")
        if rota["atraso"] > 0:
            print(f"  Motivo: {rota['motivo']} ({rota['fonte']})")


# compara as rotas e sugere o desvio quando a rota habitual esta pior
def comparar_rotas(dados, usuario):
    trajeto = obter_trajeto_usuario(dados, usuario)
    if trajeto is None:
        return
    rotas = montar_rotas(trajeto, dados["interrupcoes"], usuario["relatos"])
    ordenadas = ordenar_rotas(rotas)
    print(f"\nComparação de rotas {TAG_SIMULADO}")
    posicao = 1
    for rota in ordenadas:
        marca = ""
        if rota["linha"] == usuario["rota_habitual"]:
            marca = " (sua rota)"
        print(f"{posicao}º {rota['nome']}{marca}: {rota['total']} min, R$ {rota['custo']:.2f}")
        posicao += 1
    habitual = encontrar_rota(rotas, usuario["rota_habitual"])
    melhor = ordenadas[0]
    economia = habitual["total"] - melhor["total"]
    if economia > 0:
        print(f"\nDESVIE! A rota habitual está {economia} min mais lenta que o {melhor['nome']}.")
    else:
        print("\nSua rota habitual é a mais rápida agora. Não precisa desviar.")


# salva um relato de interrupcao feito pelo usuario
def registrar_interrupcao(dados, usuario):
    trajeto = obter_trajeto_usuario(dados, usuario)
    if trajeto is None:
        return
    print("\nQual rota está com problema?")
    mostrar_lista_rotas(trajeto["rotas"])
    escolha = ler_inteiro("Escolha a rota: ", 1, len(trajeto["rotas"]))
    motivo = ler_texto("O que aconteceu? ")
    atraso = ler_inteiro(f"Atraso estimado em minutos (1 a {ATRASO_MAXIMO}): ", 1, ATRASO_MAXIMO)
    usuario["relatos"].append({
        "linha": trajeto["rotas"][escolha - 1]["linha"],
        "motivo": motivo,
        "atraso_min": atraso,
        "fonte": "relato seu",
    })
    if salvar_json(ARQUIVO_USUARIO, usuario):
        print("Relato salvo. Ele já entra na comparação de rotas.")


# apaga os relatos salvos depois de confirmar
def limpar_relatos(usuario):
    if len(usuario["relatos"]) == 0:
        print("Você não tem relatos salvos.")
        return
    while True:
        resposta = input("Apagar todos os relatos? (s/n): ").strip().lower()
        if resposta == "s":
            usuario["relatos"] = []
            if salvar_json(ARQUIVO_USUARIO, usuario):
                print("Relatos apagados.")
            return
        elif resposta == "n":
            print("Nada foi apagado.")
            return
        else:
            print("Digite s ou n.")


# controla o fluxo principal do programa
def main():
    dados = carregar_json(ARQUIVO_DADOS)
    if dados is None:
        print(f"Não foi possível carregar {ARQUIVO_DADOS}. Encerrando.")
        return
    usuario = carregar_usuario()
    print(f"Atenção: rotas, chegadas e interrupções deste protótipo são {TAG_SIMULADO}.")
    opcao = -1
    while opcao != 0:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opção: ", 0, 5)
        match opcao:
            case 1:
                cadastrar_trajeto(dados, usuario)
            case 2:
                ver_status(dados, usuario)
            case 3:
                comparar_rotas(dados, usuario)
            case 4:
                registrar_interrupcao(dados, usuario)
            case 5:
                limpar_relatos(usuario)
            case 0:
                print("Até a próxima. Bom desvio!")
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma encerrado.")
