#  Entender mais sobre o serviço do Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).


## Explorar os recursos e ativos do workspace do Azure Machine Learning

[Portal Azure](https://portal.azure.com/)

- Dar acesso de autorização para uso dos recursos

## Entender mais sobre o serviço do Az Machine Learning
_____
1. Acesso ao Azure
2. Uma assinatura do Azure
3. Criar um grupo de recursos.
4. Criar um serviço do Az ML, que terá:
- Conta de Armazenamento
- Azure Key Vault -> Senhas e segredos
- Application Insights -> Insights de metadados
- Um registro de Contêiner do Azure -> armazena o Deploy (criar um endpoint e jogar para o conteiner)

## Criar o Workspace
_____

1. Direto no portal da Azure

2. Crie um modelo do ARM (Azure Resource Manager)
- Especificações com base em código e gera um modelo > base em um template

3. Use a CLI
- Power Shell


4. Use o SDK do Python do Azure Machine Learning
>Python
```py
from azure.ai.ml.entities import Workspace
workspace_namo = "mlw-example"
ws-basic = Workspace (
    name=workspace_name,
    location-"eastus",
)
ml_client.workspaces.begin_create(ws_basic)
```

## Explorar Workspace no portal do Azure
____
- Dentro do recurso > IAM (Controle de Acesso)
- Visão Geral > Launch Studio

## Conceder acesso ao Workspace do Azure ML
___
Três funcões internas gerais
- **Proprietário / Owner** : Pode fazer tudo, não tem limite de acessos. Pode dar acesso a terceiros
- **Colaborador** : Tem acesso a tudo, mas não pode promover acesso a outros.
- **Leitor**: somente pode visualizar o que está sendo feito. Não pode interagir e nem criar.

Az Machine Learning tem funções específicas
- **Cientista de dados do AzureML** : Responsável por criar o processo e modelos de ml
- **Operador de Serviços de Computação** : Responsável por infraestrutura / computing

|Perfil|Descrição|
|----|----|
|Proprietário / Owner|Não possui limitações de acesso e pode dar acesso a terceiros|
|Contribuidor|Não possui limitação de acessos e **não** pode dar acesso a terceiros|
|Leitor|Exibe todos os recursos, mas não permite que você faça nenhuma alteração.|
|Cientista de Dados Azure ML|É possível executar todas as ações em um workspace Azure Machine Learning, exceto para criar ou excluir recursos de computação e modificar o workspace|
|AzureML Compute Operator|Can access and perform CRUD operations on Machine Learning Services managed compute resources (including Notebook VMs).|
|Criar Funções Personalizadas|Gerencie as permissões de maneira personalizada.|


## Identificar recursos e ativos do AZ ML
___
### Recursos

1. **Workspace** - O recurso de nível superior do Azure ML.

2. **Recursos de computação**
>- instâncias de computação
>- clusters de computação
>- clusters do Kubernetes
>- computação anexada
>- computação sem servidor

3. **Armazenamento de dados**: Todos os dados são armazenados em armazenamento de dados, que são referências aos serviços de dados do Azure

### Ativos

1. **Modelos**: é o modelo de machine learning (em geral empacotado em arquivo pickle *.pkl* do Python)
2. **Ambientes / Environments**: Específicos para rodar modelos especificar variáveis de ambiente, configurações de software para executar os scripts.
3. **Dados**: Usados para acessar facilmente os dados, sem precisar autenticar todas as vezes. **Acesso via notebook, direto da workspace, permitindo o consumo do ativo.
4. **Componentes**: Reutilizar componentes nos processos de ML, por exemplo, em testes, em notebooks ou no processo de criação do modelo de ML.

## Algortimos e valores de hiperparâmetro com o Auto ML
___

Hiperparâmetros de tempo, série temporal, classificação, regressão, etc.


## Executar um Notebook
___
Notebooks: toda a parte de execução do modelo.
Training, teste, execução do modelo, etc.

Notebooks > Samples > SDK > how-to-use-azure-ml 
ou outros exemplos. 


## Executar um script como um trabalho
___

Como se comportam os trabalhos dentro do Azure Machine Learning.

Cada script loga um job/experimento, todas as entradas e saídas são armazenadas no workspace.

|Jobs/Ações/Experimentos|Descrição|
|--|--|
|Comando|Clique em célula, treinar um modelo, verificação, guarda a informação, etc. por evento|
|Varredura|Processo de ponta a ponta, faz a varredura geral no processo.|
|Pipeline|Pipeline de execução do notebook|

## Materiais de Apoio
____
Os materiais complementares e de apoio que oferecemos têm como objetivo fornecer informações para facilitar e enriquecer a sua jornada de aprendizado no curso "Trabalhando com Workspaces no Azure Machine Learning". Aqui você encontrará links úteis, como slides, repositórios e páginas oficiais, além de dicas sobre como se destacar na DIO e no mercado de trabalho 😉

### Recursos Adicionais
___

Durante este conteúdo, compreendemos os fundamentos da engenharia de prompts. Para ajudá-lo a aprofundar o conhecimento, disponibilizamos a seguir o material complementar contendo os conteúdos e links apresentados no curso:

- Slide: [Trabalhando com Workspaces no Azure Machine Learning.pptx](https://hermes.dio.me/files/assets/7c71dbc8-1b65-41c6-b264-3bec230f6787.pptx)

### Dicas e Links Úteis
___

Para se desenvolver ainda mais e se destacar na DIO e no mercado de trabalho, sugerimos os seguintes recursos:

> [Artigos e Fórum da DIO](https://web.dio.me/articles): Compartilhe seus conhecimentos e dúvidas através dos artigos (visíveis globalmente na plataforma da DIO) e nos fóruns específicos para cada experiência educacional, como nossos Bootcamps.

> Rooms: Participe do Rooms, uma ferramenta de bate-papo em tempo real onde você pode interagir com outros participantes dos nossos Bootcamps, compartilhando dúvidas, dicas e snippets de código.

> Exploração na Web: Utilize motores de busca para aprofundar seu conhecimento sobre temas específicos. Páginas como o [StackOverflow](https://stackoverflow.com/) são recursos valiosos para encontrar soluções e expandir seu entendimento.

Com esses materiais complementares, você estará bem equipado para explorar todo o potencial e se destacar em suas iniciativas. Continue aproveitando as oportunidades de aprendizado, e não hesite em buscar mais conhecimento e compartilhar suas descobertas com a comunidade!
