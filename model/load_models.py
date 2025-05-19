import joblib

def load_all_models():
    encoder = joblib.load('encoder.pkl')
    scaler = joblib.load('scaler.pkl')
    kmeans = joblib.load('modelo_kmeans.pkl')
    return encoder, scaler, kmeans
