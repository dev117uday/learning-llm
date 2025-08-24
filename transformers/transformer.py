from sympy.stats.sampling.sample_numpy import do_sample_numpy
from transformers import pipeline


def create_simple_llm(model_name, task_type):
    return pipeline(task=task_type, model=model_name, pad_token_id=50256)

def generate_text(generator, prompt, max_length=100):
    generated_text = generator(text_inputs=prompt, max_length=max_length, do_sample=True, temperature=0.7)
    return generated_text[0]["generated_text"]


model_name = "distilgpt2"
task_type = "text-generation"
prompt = "Hello World, I am ..."

generator = create_simple_llm(model_name, task_type)
print(generate_text(generator, prompt))




