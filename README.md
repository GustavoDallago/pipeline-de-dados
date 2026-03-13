# Pipeline de Dados: Integração de Vendas

Este projeto foi desenvolvido como parte do curso de Pipeline de Dados da **Alura**. O objetivo principal é simular um cenário real de engenharia de dados, onde precisamos extrair, transformar e carregar (ETL) dados provenientes de fontes e formatos distintos.

## 🎯 Propósito do Projeto
O foco deste repositório é o estudo prático de:
* **Arquitetura de Pipeline:** Como estruturar o fluxo de dados do bruto (*raw*) ao processado (*processed*).
* **Programação Orientada a Objetos (POO):** Organização do código em classes para facilitar a manutenção e escalabilidade.
* **Interoperabilidade:** Uso do **WSL2 (Ubuntu)** como ambiente de desenvolvimento integrado ao Windows.
* **Tratamento de Dados:** Manipulação de arquivos JSON e CSV utilizando **Python** e **Pandas**.

## 🛠️ Tecnologias Utilizadas
* **Python 3.10+**
* **Pandas:** Para manipulação e limpeza de DataFrames.
* **WSL2 (Ubuntu 22.04):** Ambiente de execução Linux.
* **VS Code:** Editor de código com extensões para Jupyter Notebook e WSL.

## 📂 Estrutura do Repositório
* `scripts/processamento_dados.py`: Contém a classe `Dados` com toda a lógica OO de leitura e transformação.
* `scripts/fusao_empresas_fev.py`: Script principal de execução que utiliza a classe para realizar a fusão.
* `notebooks/`: Contém os estudos iniciais em formato Jupyter (`csv.ipynb` e `json.ipynb`).
* `data_raw/`: (Pasta local) Destinada aos arquivos brutos de entrada.
* `data_processed/`: (Pasta local) Destinada ao arquivo final unificado gerado pelo script.

## ⚙️ Como o Código Funciona
A pipeline segue os seguintes passos:
1.  **Leitura (Extract):** A classe `Dados` identifica o tipo de arquivo e realiza a leitura.
2.  **Mapeamento (Transform):** As colunas do CSV são renomeadas através de um dicionário de mapeamento para coincidirem com as do JSON.
3.  **Unificação (Join):** Os dados são combinados. Campos inexistentes em uma das fontes (como colunas que só existem no CSV) são preenchidos com o valor `'Indisponível'`.
4.  **Carregamento (Load):** O resultado final é exportado como um novo arquivo CSV padronizado.

## 🚀 Como Executar
1. Clone o repositório.
2. Certifique-se de que a pasta `data_processed` existe para receber a saída.
3. Execute o script de fusão.
