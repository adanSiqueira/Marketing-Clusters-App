import pandas as pd

def processar_prever(df, encoder, scaler, kmeans):
    encoded_sexo = encoder.transform(df[['sexo']])
    encoded_df = pd.DataFrame(encoded_sexo, columns=encoder.get_feature_names_out(['sexo']))
    dados = pd.concat([df.drop('sexo', axis=1), encoded_df], axis=1)
    dados_escalados = scaler.transform(dados)
    cluster = kmeans.predict(dados_escalados)
    return cluster
