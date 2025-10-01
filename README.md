# Experimentos em RLAIF

Este repositório reúne experimentos, receitas simples e documentação sobre o uso de Reinforcement Learning from AI Feedback (RLAIF) e suas principais abordagens.
A proposta é explorar ferramentas, reproduzir artigos importantes da área e organizar práticas para quem deseja estudar ou aplicar RLAIF em LLMs.

## Estrutura do repositório

```
track_RLAIF/
│
├── datasets/                  # Documentação e scripts para uso de datasets
│   ├── anthropic_hh/          # Helpful & Harmless (humano)
│   ├── tldr/                  # TL;DR Summarization (humano)
│   ├── lm_human_prefs/        # OpenAI LM Human Preferences
│   ├── ultrafeedback/         # UltraFeedback (feedback IA - GPT-4)
│   └── helpsteer2/            # HelpSteer2 (ratings + preferências humanas)
│
├── distillation/              # Experimentos de destilação de datasets
│   ├── rlaif_basic/           # Pipeline simples de anotação com LLM-as-a-Judge
│   ├── ultrafeedback_style/   # Como reproduzir a ideia do UltraFeedback
│   └── critique_models/       # Experimentos com feedback textual
│
├── recipes/                   # Receitas curtas para uso prático
│   ├── train_rm_trl.md        # Como treinar um Reward Model no TRL
│   ├── dpo_recipe.md          # Rodando DPO com dataset de preferências
│   ├── ppo_recipe.md          # Pipeline básico de PPO
│   └── direct_rlaif.md        # Prompting direto como recompensa
│
├── frameworks/                # Ferramentas exploradas
│   ├── huggingface_trl.md     # Guia do TRL
│   ├── openrlhf.md            # Guia do OpenRLHF
│   └── vllm_judge.md          # Avaliação com vLLM + LLM-as-a-Judge
│
├── reproductions/             # Tentativas de reproduzir artigos
│   ├── rlaif_vs_rlhf/         # Experimento baseado em Lee et al. (2023)
│   ├── ultrafeedback/         # Experimento baseado em Cui et al. (2023)
│   └── helpsteer2/            # Experimento baseado em 2024
│
└── README.md                  # Este documento
```

### Como usar este repositório

- Navegue em recipes/ para ver tutoriais simples (ex.: treinar um RM com TRL).

- Consulte datasets/ para instruções de download e formatação.

- Explore distillation/ para exemplos práticos de geração de datasets artificiais.

- Veja reproductions/ para comparações com artigos da área.
