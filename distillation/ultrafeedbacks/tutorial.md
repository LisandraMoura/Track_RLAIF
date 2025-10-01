### [Ultrafeedback](https://arxiv.org/abs/2310.01377)

O UltraFeedback propõe a criação de um dataset robusto de avaliação de modelos de linguagem, indo além da simples comparação binária de respostas (preferida vs rejeitada).

1. Instruções iniciais
    - O dataset parte de prompts variados, cobrindo diferentes domínios e estilos de tarefa.
2. Geração de respostas
    - Para cada instrução, são geradas múltiplas respostas usando diferentes modelos de linguagem (ex.: modelos de porte variado e arquiteturas diferentes).
3. Anotação automática com LLM avaliador
    - Em vez de apenas escolher uma resposta melhor, um LLM “juiz” atribui anotações ricas e estruturadas em várias dimensões:
        - Veracidade (truthfulness)
        - Honestidade (honesty)
        - Utilidade (helpfulness)
        - Seguimento da instrução (instruction following)
        - Crítica
4. Agregação das anotações
    - Cada resposta fica acompanhada de um conjunto de notas e justificativas, tornando o dataset muito mais detalhado do que os típicos pares chosen/rejected.