### [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267)

O artigo compara humanos e IA como anotadores. O processo com IA é análogo ao humano, mas a escolha é feita pela probabilidade de o modelo preferir uma resposta. Conclui-se que tanto RLHF quanto RLAIF superam STF e melhoram significativamente o modelo.

1. Entrada (instrução + duas respostas)
    - Parte-se de um prompt original (ex.: “Resuma este texto”).
    - Para esse prompt, existem duas respostas candidatas (geradas por modelos diferentes ou amostras diferentes do mesmo modelo).

2. Construção do prompt para o anotador
    - O anotador IA recebe o texto formatado em um prompt específico (Tabela 15 do paper).
    - Esse prompt termina com: "Preferred Summary="

3. Decisão de preferência
    - Se o anotador for IA verificamos a probabilidade da resposta 1 e da resposta 2
    - Calcula-se P(1) e P(2) via softmax.
    - A resposta com maior probabilidade é a escolhida.

![imagem](https://arxiv.org/html/2309.00267v3/x4.png)

No paper há outros passos importantes para viéses e algumas variações de prompts. No [example.ipynb](distillation\RLAIFvsRLHF\example.ipynb) seguimos o passo a passo descrito. 