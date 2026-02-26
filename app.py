from flask import Flask, send_file
from docx import Document

app = Flask(__name__)

@app.route("/gerar-prontuario", methods=["POST"])
def gerar_prontuario():
    doc = Document()
    
    doc.add_heading('PRONTUÁRIO MÉDICO', 0)

    campos = [
        "IDENTIFICAÇÃO DO PACIENTE",
        "Nome:",
        "Data de Nascimento:",
        "Sexo:",
        "CPF:",
        "Telefone:",
        "Endereço:",
        "",
        "ANAMNESE",
        "Queixa Principal:",
        "História da Doença Atual:",
        "",
        "ANTECEDENTES PESSOAIS",
        "Doenças prévias:",
        "Cirurgias:",
        "Alergias:",
        "Medicações em uso:",
        "",
        "ANTECEDENTES FAMILIARES",
        "",
        "EXAME FÍSICO",
        "",
        "HIPÓTESE DIAGNÓSTICA",
        "",
        "PLANO TERAPÊUTICO",
        "",
        "PRESCRIÇÃO",
        "",
        "EVOLUÇÃO",
        "",
        "OBSERVAÇÕES ADICIONAIS"
    ]

    for campo in campos:
        doc.add_paragraph(campo)

    caminho = "prontuario.docx"
    doc.save(caminho)

    return send_file(caminho, as_attachment=True)

app.run(host="0.0.0.0", port=10000)
