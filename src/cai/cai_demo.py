# Conda env: cai

# Install dependencies (run in Colab or locally if needed)
# !pip install transformers gradio torch

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Load model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define simple constitution rules
constitution = [
    "No toxic or offensive language",
    "Be concise",
    "Stay factual"
]

# Helper function to generate text
def ask_model(prompt, max_tokens=150):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=max_tokens)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# CAI pipeline function
def cai_demo(user_question):
    # Step 1: Original answer
    answer_prompt = f"Answer this question: {user_question}"
    original_answer = ask_model(answer_prompt)

    # Step 2: Critique against constitution
    critique_prompt = f"Check the following answer against these rules: {constitution}\nAnswer: {original_answer}\nCritique:"
    critique = ask_model(critique_prompt, max_tokens=100)

    # Step 3: Revise based on critique
    revision_prompt = f"Revise the following answer according to this critique: {critique}\nOriginal answer: {original_answer}\nRevised answer:"
    revised_answer = ask_model(revision_prompt, max_tokens=150)

    return original_answer, critique, revised_answer

# Gradio interface
interface = gr.Interface(
    fn=cai_demo,
    inputs=gr.Textbox(label="Ask a question"),
    outputs=[
        gr.Textbox(label="Original Answer"),
        gr.Textbox(label="Critique"),
        gr.Textbox(label="Revised Answer")
    ],
    title="Mini Constitutional AI Demo",
    description="This demo shows a simple self-critique & revision loop based on a constitution."
)

interface.launch()
