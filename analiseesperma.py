from flask import Flask, render_template

app = Flask(__name__)

contagem_defeitos = {f'defeito{i+1}': 0 for i in range(23)}
contagem_defeitos['sem_defeito'] = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contar_defeito/<defeito_id>")
def contar_defeito(defeito_id):
    contagem_defeitos[defeito_id] += 1
    return ""


@app.route("/terminar_analise")
def terminar_analise():
    total_defeitos = sum(contagem_defeitos.values())
    relatorio = ""
    max_defeitos = max(contagem_defeitos.values())
    defeito_mais_comum = [defeito for defeito, contagem in contagem_defeitos.items(
    ) if contagem == max_defeitos]

   for defeito_id, contagem in contagem_defeitos.items():
    porcentagem = (contagem / total_defeitos) * 100 if total_defeitos > 0 else 0
    relatorio += f"Defeito: {defeito_id}, Quantidade: {contagem}, Porcentagem: {porcentagem:.2f}%\n"


    relatorio += f"\nDefeito(s) mais comum(ns): {', '.join(defeito_mais_comum)}, Quantidade: {
        max_defeitos}, Porcentagem: {(max_defeitos / total_defeitos) * 100 if total_defeitos > 0 else 0:.2f}%\n"

    for defeito_id in contagem_defeitos:
        contagem_defeitos[defeito_id] = 0

    return relatorio


if __name__ == "__main__":
    app.run(debug=True)
