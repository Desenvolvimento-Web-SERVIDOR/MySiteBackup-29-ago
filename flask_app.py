from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1><strong>Avaliação contínua: Aula 030</strong></h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/user/Rogerio%20Santos%20Barbosa/PT3032051/IFSP">Identificação</a></li>
        <li><a href="/contextorequisicao">Contexto da Requisição</a></li>
    </ul>

    '''

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):

    return f'''
        <h1><strong>Avaliação contínua: Aula 030</strong></h1>
        <h2><strong>Aluno: {nome}</strong></h2>
        <h2><strong>Prontuário: {prontuario}</strong></h2>
        <h2><strong>Instituição: {instituicao}</strong></h2>
        <br>
        <a href="/">Voltar à página inicial</a>
    '''

@app.route('/contextorequisicao')
def contextorequisicao():
    # 1. Obtendo as informações do objeto 'request'
    user_agent = request.headers.get('User-Agent') # Pega a string do navegador (ex: Chrome, Firefox)
    user_ip = request.remote_addr 
    host = request.host # Pega o domínio onde a aplicação está rodando
    
    # 2. Injetando as informações no HTML com uma f-string
    return f'''
        <h1><strong>Avaliação contínua: Aula 030</strong></h1>
        <h2><strong>Seu navegador é:</strong> {user_agent}</h2>
        <h2><strong>O IP do computador remoto é:</strong> {user_ip}</h2>
        <h2><strong>O host da aplicação é:</strong> {host}</h2>
        <br>
        <a href="/">Voltar à página inicial</a>
    '''