# Disponibilização de Dados no Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).


## Entender URIs
---
- Um URI faz referência à localização de seus dados.
- Para que o Azure ML se conecte aos seus dados diretamente, você precisa prefixar o URI com o protocolo apropriado.

|Protocolo|Descrição|Ambiente|
|---|---|---|
|HTTPS| site ou conta de armazenamento do blobstorage ou local público|Outros|
|abfs(s)| referências/caminhos para o Azure Data Lake Gen2|DataLake|
|azureml| Armazenamento de dados do AzureML|Próprio ambiente Azml|

## Armazenamento de dados
---
Benefícios de trazer para dentro do ambiente:
- A informação já fica instanciada dentro do ambiente
- Quem for utilizar já possui acesso, facilita.
- Armazena de forma segura
- E fica disponível para utilização com segurança dentro do modelo/ambiente. (Seja para análise exploratória ou para executar um modelo)
- SQL, Blobstorage, Conta de Armazenamento, etc.

1. Fornecer URIs fáceis de usar para o armazenamento de dados.
2. Facilita a descoberta de dados no Azure Machine Learning.
3. Armazena com segurança informações de conexão, sem expor segredos e chaves a cientistas de dados.

> **Assets > Data > Data assets | Datastores | Dataset monitors**

## Compreender os ativos de dados
---
Benefícios de usar ativos de dados:

- Criar um experimento, fazer uma análise, processar um pipeline: gera artefatos e seus caminhos (ativos de dados) para consumir ou gerar novos
1. Arquivo URI
2. Pasta URI
3. MLTable

- Compartilhar e reutilizar dados com outros membros
- Você pode acessar diretamente os dados durante o treinamento do modelo (em qualquer tipo de computação compatível) sem se preocupar com cadeias de conexão ou caminhos de dados.
- Versão dos metadados do ativo de dados.

> **Assets > Data > workspaceartifactstore > caminhos para os ativos de dados (logs de experimento)**

OU

> **Assets > Jobs > nome_do_model > logs de experimento**

## Materiais de Apoio
---

Os materiais complementares e de apoio que oferecemos têm como objetivo fornecer informações para facilitar e enriquecer a sua jornada de aprendizado no curso **"Disponibilização de Dados no Azure Machine Learning"**. Aqui você encontrará links úteis, como slides, repositórios e páginas oficiais, além de dicas sobre como se destacar na DIO e no mercado de trabalho 😉

### Recursos Adicionais
Durante este conteúdo, compreendemos os **fundamentos da engenharia de prompts**. Para ajudá-lo a aprofundar o conhecimento, disponibilizamos a seguir o material complementar contendo os conteúdos e links apresentados no curso:

> Slide: [Disponibilização de Dados no Azure Machine Learning.pptx](https://hermes.dio.me/files/assets/01eac03c-c8ee-4935-a8ce-615cca43392a.pptx)
