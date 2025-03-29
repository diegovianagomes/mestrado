
# O que são Dados?

"Dados São partes distintas de informações geralmente formatadas de uma maneira especial"

O dado pode ser mesurado, coletado, registrado e analisado

São frequentemente visualizados por meio de gráficos, imagens ou outras ferramentas de analise.

Dados não processados ou "Dados Bruto", são uma coleção de números ou caracteres antes de ser limpos e corrigidos pelos pesquisadores.

Devem ser corrigidos para que sejam removidos valores discrepantes, instrumentos ou erros de entrada de dados

O Processamento de dados ocorre comumente e estágios e portanto os dados processados de uma estagio podem ser dados brutos de outros estagio subsequente.

Field Data ou Dado de Campo  é um tipo de dado que é coletado em um ambiente "in situ" não controlado.

Experimental Data ou dado experimental é uma tipo de dado que é gerado  a partir de uma observação de uma investigação cientifica.

Os dados podem ser gerados por:

- Humanos
- Maquina
- Combinação Humano Maquina

Podendo ser gerada em qualquer lugar onde qualquer informação é gerada e arquivada em formato estruturado ou não estruturado

# O que é uma Informação

Uma Informação é um dado que foi processada, organizada ou estruturado em uma maneira significativa, valiosa e útil.

São dados que receberam contexto, relevância e proposito.

Dando conhecimento, entendimento e insights que servem de tomada de decisões, resolução de problemas e varios outros propositos


# Por que o dado é importante?

- Ajuda tomar melhores decisões
- Ajuda resolver problemas, encontrando motivo de baixo desempenho
- Ajuda avaliar performance
- Ajuda melhorar processos
- Ajuda entender o mercado consumidor

# Categoria de Dados

Dados podem ser categorizados em duas partes principais

## Dados Estruturados

É um tipo de dado organizado em um formato especifico, sendo facil de ser encontrado, analizado e processado. São encontrados em banco de dados relacionais que incluem informações como números, dados e categoria

## Dados Não Estruturados

Este tipo de dado não está em conformidade com um tipo especifico de estrutura ou formato. Nele podemos incluir alguns textos do documento, imagens, vídeos, e outros dos  que não são facilmente organizados ou analisados sem um processamento adicional.

# Tipos de Dado

Geralmente o dado pode ser classificado em duas partes:

## Dados Categóricos

Neste tipo de dado vemos dados que tem uma categoria definida

- Estado Civil
- Partido Político
- Cor dos Olhos

## Dados Numéricos
Este tipo de dado pode ser classificado em dois tipos:
#### Dados Discretos
Contem o dado que tem um valor numérico discreto por exemplo:
- Numero de filhos
- Erros por hora
### Dados Contínuos
Contem os dados que tem valor numérico continuo, por exemplo:
- Peso
- Voltagem

## Escala Nominal
A escala nominal classifica o dado em varias categorias distintas a qual não é aplicado criterios de ranqueamento, por exemplo:
- Genero
- Estado Civil
## Escala Ordinal
A escala ordinal classifica o dado em categorias distintas onde é aplicado um ranqueamento, por exemplo:
- Posição no corpo docente: 
	- Professor, 
	- Professor Associado, 
	- Professor Assistente
- Notas dos Alunos
	- A
	- B
	- C
	- D
	- E
	- F

## Escala de Intervalo
A escala de intervalo pode ser uma escala ordenada durante a qual a diferença entre as medições é uma quantidade  significativa, mas medições não tem um ponto zero verdadeiro:
- Temperatura
- Anos
## Escala de Razão
A escala de razão pode ser ordenada durante a qual a diferença entre a medição é uma quantidade significativa e portanto as medições tem um ponto zero verdadeiro. Assim podemos realizar operações aritméticas em dados de escala real. Por exemplo:
- Peso
- Idade
- Salario

# Como é o ciclo de processamento de Dados

O ciclo de processamento de dados é iterativo, o que significa que o resultado de um estágio pode se tornar a entrada para outro. Isso permite o refinamento contínuo, a análise mais profunda e a criação de percepções cada vez mais sofisticadas a partir dos dados brutos. Podem ser visualizados em uma pipeline com estágios distintos:

![[Untitled Diagram.svg]]
**Figura 01:** *Processo de descoberta de conhecimento em banco de dados (KDD)*

### Aquisição
Este estágio engloba métodos usados para coletar os dados brutos de varias fontes. Podendo envolver:

> sensores de leitura, 
> raspagem de dados web, ou 
> pegar informações de fontes e logs de aplicações.
### Preparação
O dado bruto é inerentemente bagunçado e requer limpeza e pré-processamento antes da analise. Este estagio envolve:

> tarefas de identificar e manipular valores faltantes,
> corrigir as inconsistências, 
> formatar os dados em uma estrutura consistente e 
> remover outlier potenciais.
### Entrada
O dado pré-processado é carregado em um sistema adequado para a o processamento e a analise. Este envolve:

> converter os dados em formato de leitura da maquina e 
> armazenar em um banco de dados ou do Data warehouse
### Processamento
Aqui, o dado passa por varias manipulações e transformações, para extrair informações valiosas. Podendo incluir: 

> Agregação
> Filtragem
> Classificação
> Engenharia de recursos *( criação de novos recursos a partir de recursos existentes )*
> Aplicar algoritmos de Aprendizado de Maquina para descobrir padrões e relações
### Saída
O dado transformado é analisado usando varias técnicas para gerar insights e conhecimento. Envolve:

> analise estatística, 
> técnicas de visualização ou, 
> construção de modelos preditivos
### Armazenamento
O dado processado e saídas geradas são armazenados e um formato seguro e acessível para uso futuro, referencia ou alimentar outros ciclos de analise



#