"""
Mental Health Support Chatbot - Streamlit Interface
Uses a fine-tuned DistilGPT2 model from the notebook training step.
"""

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import warnings
warnings.filterwarnings("ignore")

MODEL_PATH = "./mental-health-chatbot-final"

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "self-harm", "self harm", "end my life",
    "want to die", "better off dead", "suicidal", "cut myself", "overdose"
]

HELPLINE_TEXT = """
⚠️ **CRISIS DETECTED — Please Read** ⚠️

If you're in crisis or thinking about suicide, **please reach out now**:

| Country | Helpline | Number |
|---------|----------|--------|
| 🇺🇸 US | 988 Suicide & Crisis Lifeline | **988** |
| 🇬🇧 UK | Samaritans | **116 123** |
| 🇪🇺 EU | Emergency Services | **112** |
| 🌍 Global | Befrienders | [befrienders.org](https://www.befrienders.org) |

**You are not alone. Help is available 24/7.** 💙
"""

st.set_page_config(
    page_title="Mental Health Support Bot",
    page_icon="💙",
    layout="centered"
)

st.title("💙 Mental Health Support Chatbot")
st.caption("Fine-tuned on EmpatheticDialogues — here to listen, not to diagnose.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Hi there 👋 I'm here to listen and support you. "
            "You can talk to me about stress, anxiety, or anything on your mind. "
            "Remember — I'm not a therapist, just a supportive listener. "
            "How are you feeling today?"
        )
    })


@st.cache_resource
def load_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
        device = 0 if torch.cuda.is_available() else -1
        chatbot = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=device
        )
        return tokenizer, chatbot, device
    except Exception:
        return None, None, None


tokenizer, chatbot, device = load_model()

if chatbot is None:
    st.error(
        "⚠️ Fine-tuned model not found at `./mental-health-chatbot-final`. "
        "Run the notebook first to train and save the model, or place the model files in that directory."
    )
    st.stop()


def check_crisis(text):
    return any(kw in text.lower() for kw in CRISIS_KEYWORDS)


def generate_response(user_input):
    prompt = f"Context: {user_input}\nResponse:"
    result = chatbot(
        prompt,
        max_length=len(prompt) + 120,
        temperature=0.75,
        top_k=50,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        num_return_sequences=1,
    )
    response = result[0]["generated_text"]
    if "Response:" in response:
        response = response.split("Response:")[-1].strip()
    response = response.split(user_input)[-1].strip() if user_input in response else response
    return response


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Share what's on your mind..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if check_crisis(prompt):
        st.session_state.messages.append({"role": "assistant", "content": HELPLINE_TEXT})
        with st.chat_message("assistant"):
            st.markdown(HELPLINE_TEXT)
    else:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.markdown("### About")
    st.markdown(
        "This chatbot is fine-tuned on the **EmpatheticDialogues** dataset "
        "to provide supportive, empathetic responses."
    )
    st.markdown("### ⚠️ Important")
    st.markdown(
        "This is **NOT** a substitute for professional mental health care. "
        "If you're experiencing a crisis, please use the helplines listed above."
    )
    st.markdown("### Model Info")
    st.markdown(f"- **Base:** DistilGPT2 (82M params)")
    st.markdown(f"- **Device:** {'GPU' if device == 0 else 'CPU'}")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
