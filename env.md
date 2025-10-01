# (opcional) criar venv
python -m venv .venv && .venv\Scripts\Activate.ps1

# libs essenciais
pip install -U transformers accelerate datasets trl peft torch numpy pandas bitsandbytes accelerate
