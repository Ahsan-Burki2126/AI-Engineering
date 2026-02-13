from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model ONCE (global)
MODEL_NAME = "facebook/blenderbot-400M-distill"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def generate_reply(conversation_history, user_message):
    """
    conversation_history: list of strings
    user_message: string
    returns: bot reply (string)
    """

    # 1. Combine conversation history into one string
    history_text = " ".join(conversation_history)

    # 2. Add the new user message
    full_input = history_text + " " + user_message if history_text else user_message

    # 3. Tokenize
    inputs = tokenizer(full_input, return_tensors="pt")

    # 4. Generate reply
    output_ids = model.generate(**inputs)

    # 5. Decode reply
    reply = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return reply.strip()
