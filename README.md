# Marketing-Clusters-App

# Análise de Segmentação de Usuários para Marketing com K-means

## Visão Geral

Este projeto utiliza o algoritmo de **clusterização K-means** para segmentar usuários em grupos com base em seus interesses, com o objetivo de aprimorar campanhas de marketing. Através da análise de comportamento e preferências dos usuários, podemos identificar diferentes perfis e criar estratégias de marketing mais personalizadas e eficazes.

Com esse modelo, você pode prever a qual grupo um usuário pertence, permitindo o direcionamento de campanhas mais assertivas para públicos segmentados. O modelo foi treinado com base em características como **sexo** e outras variáveis de interesse, e pode ser facilmente aplicado a novos dados com a interface do aplicativo Streamlit.

## Tecnologias Utilizadas

- **Streamlit**: Para criar a interface interativa do usuário.
- **Scikit-learn**: Para o treinamento e aplicação do modelo de clusterização K-means.
- **Joblib**: Para salvar e carregar os modelos e transformadores (como o `scaler` e `encoder`).
- **Pandas**: Para manipulação e análise dos dados.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

.
├── app.py # Arquivo principal que contém a interface do Streamlit.\n
├── encoder.pkl # Modelo de codificação para a variável "sexo".\n
├── modelo_kmeans.pkl # Modelo de clusterização K-means treinado.\n
├── novas_entradas.csv # Arquivo de exemplo com novos dados a serem analisados.\n
├── requirements.txt # Dependências do projeto.\n
├── scaler.pkl # Transformador de escalonamento dos dados.\n
└── pasta/models/ # Contém scripts de carregamento e previsão do modelo.\n
├── init.py\n
├── load_models.py # Função para carregar todos os modelos e transformadores.\n
├── predict.py # Função para processar dados e fazer previsões.\n
└── Desenvolvimento do modelo.ipynb # Documento com a descrição do desenvolvimento do modelo.\n


## Como Funciona

### 1. Carregamento dos Modelos

Ao iniciar o aplicativo, os seguintes modelos e transformadores são carregados:

- **Encoder**: Para codificar a variável categórica "sexo".
- **Scaler**: Para normalizar os dados antes da aplicação do modelo.
- **K-means**: O modelo de clusterização K-means treinado, que segmenta os usuários em diferentes grupos com base nas suas características.

### 2. Interface do Usuário

A interface do Streamlit permite ao usuário:

- Carregar um arquivo CSV com os dados dos usuários.
- Visualizar a descrição dos grupos gerados pelo modelo.
- Obter as previsões de clusterização para os dados carregados.
- Baixar o arquivo com os resultados das previsões.

A segmentação é realizada em três grupos principais:

- **Grupo 0**: Público jovem com forte interesse em moda, música e aparência.
- **Grupo 1**: Associado a esportes e cultura.
- **Grupo 2**: Equilibrado, com interesses em música, dança e moda.

### 3. Previsão de Novos Dados

O usuário pode carregar novos dados, que serão automaticamente processados, e o modelo predirá o grupo ao qual cada usuário pertence. Isso é útil para segmentação de campanhas de marketing, permitindo uma abordagem mais personalizada.

## Como Rodar o Projeto

### Requisitos

Instale as dependências listadas no arquivo `requirements.txt`

## Rodando o Aplicativo

Execute o aplicativo Streamlit com o seguinte comando:

```bash
streamlit run app.py
```

### Arquivo CSV de Exemplo

O arquivo `novas_entradas.csv` contém um exemplo de dados que podem ser carregados para testar o modelo. O arquivo deve ter, pelo menos, a coluna **sexo** (para codificação) e as demais variáveis necessárias para o modelo de clusterização

## Resultados Esperados

O modelo de clusterização K-means segmenta os usuários em três grupos principais, com base nos seguintes interesses:

- **Grupo 0**: Focado em moda, música e estética.
- **Grupo 1**: Interesses em esportes e cultura pop.
- **Grupo 2**: Público diversificado com interesses em música, dança e estilo.

Essa segmentação pode ser usada para direcionar campanhas de marketing mais eficazes, criando anúncios personalizados e focados no comportamento e preferências de cada grupo.

