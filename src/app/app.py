from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Função para listar as marcas de veículos
def listar_marcas(tipo_veiculo=None):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas" if tipo_veiculo else "https://parallelum.com.br/fipe/api/v1/carros/marcas"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return {'erro': f"Erro ao consultar a API. Código de status: {response.status_code}"}
    except Exception as e:
        return {'erro': f"Ocorreu um erro ao consultar as marcas: {e}"}

# Função para listar os modelos de um veículo baseado na marca
def listar_modelos(tipo_veiculo, codigo_marca):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get('modelos', [])
        else:
            return {'erro': f"Erro ao consultar os modelos. Código de status: {response.status_code}"}
    except Exception as e:
        return {'erro': f"Ocorreu um erro ao consultar os modelos: {e}"}

# Função para listar os anos de um modelo
def listar_anos(tipo_veiculo, codigo_marca, codigo_modelo):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return {'erro': f"Erro ao consultar os anos. Código de status: {response.status_code}"}
    except Exception as e:
        return {'erro': f"Ocorreu um erro ao consultar os anos: {e}"}

# Função para listar os preços de um veículo baseado no ano escolhido
def listar_precos(tipo_veiculo, codigo_marca, codigo_modelo, codigo_ano):
    try:
        url = f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return {'erro': f"Erro ao consultar os preços. Código de status: {response.status_code}"}
    except Exception as e:
        return {'erro': f"Ocorreu um erro ao consultar os preços: {e}"}

@app.route('/')
def home():
    return "Ufa! Estou funcionando."

@app.route('/marcas', methods=['GET'])
def api_marcas():
    tipo_veiculo = request.args.get('tipo_veiculo', 'carros')  # Default para 'carros'
    marcas = listar_marcas(tipo_veiculo)
    return jsonify(marcas)

@app.route('/modelos', methods=['GET'])
def api_modelos():
    tipo_veiculo = request.args.get('tipo_veiculo', 'carros')
    codigo_marca = request.args.get('codigo_marca')
    if not codigo_marca:
        return jsonify({"erro": "Código da marca é necessário."}), 400
    
    modelos = listar_modelos(tipo_veiculo, codigo_marca)
    return jsonify(modelos)

@app.route('/anos', methods=['GET'])
def api_anos():
    tipo_veiculo = request.args.get('tipo_veiculo', 'carros')
    codigo_marca = request.args.get('codigo_marca')
    codigo_modelo = request.args.get('codigo_modelo')
    if not codigo_marca or not codigo_modelo:
        return jsonify({"erro": "Código da marca e modelo são necessários."}), 400
    
    anos = listar_anos(tipo_veiculo, codigo_marca, codigo_modelo)
    return jsonify(anos)

@app.route('/precos', methods=['GET'])
def api_precos():
    tipo_veiculo = request.args.get('tipo_veiculo', 'carros')
    codigo_marca = request.args.get('codigo_marca')
    codigo_modelo = request.args.get('codigo_modelo')
    codigo_ano = request.args.get('codigo_ano')
    
    if not codigo_marca or not codigo_modelo or not codigo_ano:
        return jsonify({"erro": "Código da marca, modelo e ano são necessários."}), 400
    
    precos = listar_precos(tipo_veiculo, codigo_marca, codigo_modelo, codigo_ano)
    return jsonify(precos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
