from flask import Flask, render_template, request

app = Flask(__name__)

def teorema_de_bayes(p_a, p_b_dado_a, p_b_dado_nao_a):
    p_nao_a = 1 - p_a
    numerador = p_b_dado_a * p_a
    denominador = (p_b_dado_a * p_a) + (p_b_dado_nao_a * p_nao_a)
    if denominador == 0:
        return 0
    return round(numerador / denominador, 4)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            tipo_investimento = request.form["tipo_investimento"]
            perfil_risco = request.form["perfil_risco"]
            tempo = int(request.form["tempo"])
        except (ValueError, KeyError):
            resultado = {"erro": "Dados inválidos. Verifique e tente novamente."}
            return render_template("index.html", resultado=resultado)

        # Probabilidades base (poderiam vir de um banco de dados ou IA real)
        # Vamos simular com dados hipotéticos

        # Probabilidade do investimento ser bom (com base no tipo escolhido)
        prob_bom_investimento = {
            "Ações": 0.6,
            "Criptoativos": 0.4,
            "Tesouro Direto": 0.75,
            "Fundos Imobiliários": 0.7
        }.get(tipo_investimento, 0.5)

        # Probabilidade de "sucesso no retorno" dado perfil e tempo
        if perfil_risco == "Conservador":
            p_sucesso_dado_bom = 0.5 if tempo < 12 else 0.7
            p_sucesso_dado_ruim = 0.2
        elif perfil_risco == "Moderado":
            p_sucesso_dado_bom = 0.65 if tempo < 12 else 0.8
            p_sucesso_dado_ruim = 0.3
        else:  # Agressivo
            p_sucesso_dado_bom = 0.8 if tempo < 12 else 0.9
            p_sucesso_dado_ruim = 0.4

        # Aplicação do Teorema de Bayes
        probabilidade_final = teorema_de_bayes(
            p_a=prob_bom_investimento,
            p_b_dado_a=p_sucesso_dado_bom,
            p_b_dado_nao_a=p_sucesso_dado_ruim
        )

        resultado = {
            "tipo_investimento": tipo_investimento,
            "perfil_risco": perfil_risco,
            "tempo": tempo,
            "probabilidade_retorno": probabilidade_final
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
