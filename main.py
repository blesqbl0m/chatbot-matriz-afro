from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <title>Chatbot – Protótipo de Pesquisa</title>
  <style>
    body { font-family: Arial, sans-serif; background:#f5f5f5; padding:40px; }
    #chat { background:white; padding:20px; border-radius:8px; max-width:600px; margin:auto; }
    .msg { margin:10px 0; }
    .bot { color:#444; }
    .user { text-align:right; color:#000; }
  </style>
</head>
<body>
<div id="chat">
  <div class="msg bot">Olá. Este é um protótipo de chatbot para pesquisa.</div>
</div>
<input id="input" placeholder="Digite aqui..." style="width:80%">
<button onclick="send()">Enviar</button>

<script>
function send(){
  const input = document.getElementById("input");
  fetch("/chat", {
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({message:input.value})
  }).then(r=>r.json()).then(data=>{
    const chat = document.getElementById("chat");
    chat.innerHTML += `<div class='msg user'>${input.value}</div>`;
    chat.innerHTML += `<div class='msg bot'>${data.reply}</div>`;
    input.value="";
  });
}
</script>
</body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message","").lower()

    respostas = {
        "milagre": "A ideia de milagre varia conforme contexto cultural, religioso e histórico.",
        "cemiterio": "Cemitérios também podem ser vistos como espaços simbólicos e sociais.",
        "fe": "A fé costuma atravessar experiências individuais e coletivas.",
    }

    for chave in respostas:
        if chave in user_message:
            return jsonify(reply=respostas[chave])

    return jsonify(reply="Interessante. Você pode falar mais sobre isso?")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)