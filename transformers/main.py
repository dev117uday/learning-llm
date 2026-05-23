from transformers import pipeline, AutoTokenizer

model_name = "distilgpt2"


def create_simple_llm():
    return pipeline("text-generation", model=model_name, pad_token_id=50256)


def generated_text(prompt, length):
    generator = create_simple_llm()
    result = generator(prompt, max_length=length, do_sample=True, temperature=0.3)
    return result[0]["generated_text"]


def explain_process():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    text = "Hello World !"
    tokens = tokenizer.encode(text)
    decoded = tokenizer.decode(tokens)

    print(f"text : {text}")
    print(f"tokens : {tokens}")
    print(f"decoded token : {decoded}")


def generate_text_from_prompt():
    prompt = "Hi, who are you ?"
    text = generated_text(prompt, length=30)
    print()
    print(text)


if __name__ == "__main__":
    explain_process()
    # generate_text_from_prompt()
