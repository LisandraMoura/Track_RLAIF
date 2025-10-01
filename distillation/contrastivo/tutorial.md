### [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://arxiv.org/html/2307.12950v3)


O artigo apresenta o RLCD (Reinforcement Learning from Contrastive Distillation) como uma alternativa ao RLHF e ao RLAIF para alinhar modelos de linguagem. A motivação é que os métodos tradicionais dependem de julgamentos humanos ou de um LLM maior atuando como “juiz” para criar dados de preferência, o que é custoso.

O RLCD muda esse paradigma:

1. Em vez de amostrar duas respostas do mesmo prompt e pedir que um juiz escolha a melhor, ele constrói contrastes por design.
2. Para cada entrada, gera duas variantes de prompt: uma positiva (induzindo uma propriedade desejada, como ser útil, correto, educado) e outra negativa (induzindo o oposto).
3. O mesmo modelo base gera respostas para cada variante.
4. O par de saídas resultante é automaticamente rotulado: a saída do prompt positivo é o “chosen” e a saída do prompt negativo é o “rejected”.


![imagem](https://arxiv.org/html/2307.12950v3/x1.png)


A implementação em [example.ipynb](distillation/contrastivo/example.ipynb) segue a estrutura descrita, sendo uma simplificação do processo apresentado no artigo.
