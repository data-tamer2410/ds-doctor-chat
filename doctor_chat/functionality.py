# This file contains the functionality of the chatbot.

import streamlit as st
import time
from transformers import TFAutoModelForCausalLM, AutoTokenizer


class LongMessageError(Exception):
    # Custom exception for long messages
    def __init__(self):
        super().__init__("The input message is too long.")


@st.cache_resource()
def load_model_and_tokenizer() -> tuple:
    # Load model and tokenizer
    model_path = "doctor_chat/gpt2-doctor-chat"
    model = TFAutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer


def processing_user_input(user_input: str, context: list, tokenizer) -> dict:
    # Process user input
    input_text = '\n'.join(f"{message['token']} {message['content']}" for message in context)
    input_text += f"\n[|Human|] {user_input}\n[|AI|]"
    input_ids = tokenizer(input_text, return_tensors="tf")
    while input_ids["input_ids"].shape[1] > tokenizer.vocab_size:
        if not context:
            raise LongMessageError
        second_token = '[|AI|]' if context[0]["token"] == '[|Human|]' else '[|Human|]'
        start_i = input_text.find(second_token)
        input_text = input_text[start_i:]
        input_ids = tokenizer(input_text, return_tensors="tf")
        context.pop(0)
    return input_ids


def generate_response(input_ids: dict, model, tokenizer) -> str:
    # Generate response
    response = model.generate(
        **input_ids,
        max_length=1500,
        eos_token_id=[
            tokenizer.eos_token_id,
            tokenizer.additional_special_tokens_id[1],
        ],
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.2,
    )
    response = tokenizer.decode(response[0, :-1]).split("[|AI|]")[-1].strip()
    return response


def ai_message_generator(response: str) -> str:
    # Function for st.write_stream to display AI messages
    for word in response.split():
        yield word + ' '
        time.sleep(0.08)
