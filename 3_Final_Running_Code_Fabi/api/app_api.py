
# -*- coding: utf-8 -*-
"""
AI Finance Incidents Analysis API
API RESTful para análise de incidentes de IA em serviços financeiros
"""

import pandas as pd
import numpy as np
import sqlite3
import joblib
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# =========================
# CONFIGURAÇÕES
# =========================
DATABASE = 'ai_finance_incidents.db'
MODELS_PATH = r'C:\Users\PP\OneDrive - Fundação São Paulo\PUC-SP\5 Semestre\SEGURANÇA CIBERNÉTICA E ENGENHARIA SOCIAL\PROJETO01\models\\'
PORT = int(os.getenv("PORT", 5000))

# =========================
# INICIALIZAÇÃO
# =========================
app = Flask(__name__)
CORS(app)

app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# =========================
# CARREGAMENTO MODELOS ML
# =========================
try:
    severity_model = joblib.load(f'{MODELS_PATH}severity_classifier.pkl')
    investigation_model = joblib.load(f'{MODELS_PATH}investigation_classifier.pkl')
    features_severity = joblib.load(f'{MODELS_PATH}features_severity.pkl')
    features_investigation = joblib.load(f'{MODELS_PATH}features_investigation.pkl')

    models_loaded = True
    print("✅ Modelos carregados com sucesso")

except Exception as e:
    print(f"⚠️ Erro ao carregar modelos: {e}")
    models_loaded = False


# =========================
# BANCO DE DADOS
# =========================
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def query_db(query, args=(), one=False):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        rv = cursor.fetchall()
        conn.close()
        results = [dict(row) for row in rv]
        return results[0] if results and one else results

    except Exception as e:
        print(f"Erro na query: {e}")
        return None


# =========================
# ENDPOINT: HOME
# =========================
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'api': 'AI Finance Incidents Analysis API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'GET /api/incidents': 'Lista incidentes',
            'GET /api/incidents/<id>': 'Detalhe incidente',
            'GET /api/stats/by-application': 'Stats por aplicação',
            'GET /api/stats/by-segment': 'Stats por segmento',
            'GET /api/stats/temporal': 'Stats temporal',
            'GET /api/stats/governance': 'Governança',
            'POST /api/predict/severity': 'Predição severidade',
            'POST /api/predict/investigation': 'Predição investigação'
        }
    })


# =========================
# INCIDENTES
# =========================
@app.route('/api/incidents', methods=['GET'])
def get_incidents():
    try:
        application_type = request.args.get('application_type')
        severity_level = request.args.get('severity_level')
        year = request.args.get('year')
        limit = min(request.args.get('limit', 50, type=int), 100)

        query = "SELECT * FROM incidents WHERE 1=1"
        params = []

        if application_type:
            query += " AND application_type = ?"
            params.append(application_type)

        if severity_level:
            query += " AND severity_level = ?"
            params.append(severity_level)

        if year:
            query += " AND year = ?"
            params.append(year)

        query += f" LIMIT {limit}"

        incidents = query_db(query, params)

        return jsonify({
            'total': len(incidents) if incidents else 0,
            'incidents': incidents
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/incidents/<int:incident_id>', methods=['GET'])
def get_incident_detail(incident_id):
    try:
        incident = query_db(
            "SELECT * FROM incidents WHERE incident_id = ?",
            [incident_id],
            one=True
        )

        if not incident:
            return jsonify({'error': 'Incidente não encontrado'}), 404

        financial = query_db(
            "SELECT * FROM financial_impacts WHERE incident_id = ?",
            [incident_id],
            one=True
        )

        regulatory = query_db(
            "SELECT * FROM regulatory_responses WHERE incident_id = ?",
            [incident_id],
            one=True
        )

        return jsonify({
            'incident': incident,
            'financial_impact': financial,
            'regulatory_response': regulatory
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# =========================
# ESTATÍSTICAS
# =========================
@app.route('/api/stats/by-application', methods=['GET'])
def stats_by_application():
    query = """
    SELECT application_type, COUNT(*) as total
    FROM incidents
    GROUP BY application_type
    """
    return jsonify(query_db(query))


@app.route('/api/stats/by-segment', methods=['GET'])
def stats_by_segment():
    query = """
    SELECT customer_segment, COUNT(*) as total
    FROM incidents
    GROUP BY customer_segment
    """
    return jsonify(query_db(query))


@app.route('/api/stats/temporal', methods=['GET'])
def stats_temporal():
    query = """
    SELECT year, COUNT(*) as total
    FROM incidents
    GROUP BY year
    ORDER BY year
    """
    return jsonify(query_db(query))


@app.route('/api/stats/governance', methods=['GET'])
def stats_governance():
    query = """
    SELECT COUNT(*) as total
    FROM regulatory_responses
    """
    return jsonify(query_db(query, one=True))


# =========================
# PREDIÇÃO
# =========================
@app.route('/api/predict/severity', methods=['POST'])
def predict_severity():
    if not models_loaded:
        return jsonify({'error': 'Modelos não carregados'}), 503

    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON inválido'}), 400

        df = pd.DataFrame([data])
        df = pd.get_dummies(df)

        for col in features_severity:
            if col not in df:
                df[col] = 0

        X = df[features_severity]

        pred = severity_model.predict(X)[0]
        prob = severity_model.predict_proba(X)[0]

        return jsonify({
            'prediction': int(pred),
            'probability': float(max(prob))
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/predict/investigation', methods=['POST'])
def predict_investigation():
    if not models_loaded:
        return jsonify({'error': 'Modelos não carregados'}), 503

    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON inválido'}), 400

        df = pd.DataFrame([data])
        df = pd.get_dummies(df)

        for col in features_investigation:
            if col not in df:
                df[col] = 0

        X = df[features_investigation]

        pred = investigation_model.predict(X)[0]
        prob = investigation_model.predict_proba(X)[0]

        return jsonify({
            'prediction': int(pred),
            'probability': float(prob[1])
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# =========================
# RUN
# =========================
if __name__ == '__main__':
    print("="*60)
    print(f"🚀 API rodando em http://localhost:{PORT}")
    print("="*60)

    app.run(host='0.0.0.0', port=PORT, debug=True)
