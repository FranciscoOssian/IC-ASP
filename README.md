# IC-ASP: Avaliação Experimental de Agentes Inteligentes

Este repositório contém a implementação e avaliação de dois agentes inteligentes em um ambiente simulado do "mundo do aspirador de pó". O objetivo é comparar o desempenho de um agente reativo simples com um agente baseado em modelos em um ambiente parcialmente observável.

## Descrição dos Agentes

- **Agente Reativo Simples**: Este agente toma decisões com base apenas nas células adjacentes à sua posição atual, sem considerar o histórico ou um modelo do ambiente. Suas ações são baseadas em uma abordagem simples e direta.

- **Agente Baseado em Modelos**: Este agente mantém um modelo do ambiente, incluindo a localização das células sujas e obstáculos. Utiliza o algoritmo A* para encontrar o caminho mais eficiente para limpar as células sujas, considerando a localização atual e os obstáculos.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/username/ic-asp.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd ic-asp
    ```

3. Execute o código dos agentes usando Python

4. Caso for preciso use requisiments.txt para rodar em um ambiente virtual.
