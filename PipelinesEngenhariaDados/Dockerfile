# Imagem base do Airflow
FROM apache/airflow:2.9.3

# Atualize pip e instale bibliotecas Python necessárias
RUN pip install --upgrade pip \
    && pip install apache-airflow-providers-papermill xlrd

# Copie o diretório 'bombril' para o diretório /bombril no container
#COPY diretorio /opt/airflow/diretorio

# Defina o diretório de trabalho
#WORKDIR /diretorio

# Comando padrão (opcional, pode ser definido conforme necessário)
CMD ["bash"]

