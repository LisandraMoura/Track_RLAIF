from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class LocalLLM:
    def __init__(self, 
                 model_name: str = "microsoft/phi-1_5", 
                 device: str = "cpu",
                 max_new_tokens: int = 128,
                 temperature: float = 0.0):
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto" if device != "cpu" else None,
            torch_dtype="auto"
        )
        
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=-1 if device == "cpu" else 0
        )
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

    def generate(self, prompt: str) -> str:
        output = self.pipe(
            prompt,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            do_sample=(self.temperature > 0.0),
        )
        return output[0]["generated_text"][len(prompt):].strip()
    
# if __name__ == "__main__":
#     llm = LocalLLM(model_name="microsoft/phi-1_5")
    
#     prompt = "Explique em duas frases o que é aprendizado por reforço."
#     resposta = llm.generate(prompt)
#     print("Resposta:", resposta)