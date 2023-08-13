import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Streamlit app
def main():
    st.title("Question Rephrasing App")

    # User input
    user_input = st.text_input("Enter your question:")
    if user_input:
        st.write(f"Original question: {user_input}")

        # Rephrase the question
        rephrased_question = rephrase_question(user_input)

        # Display rephrased question and radio buttons in a single line
        feedback = st.radio("Did you like the rephrased question?", ["Like", "Dislike"])
        st.write(f"{rephrased_question}   {feedback}")

        # Process user feedback
        if feedback == "Like":
            st.success("Thank you for your feedback!")

def rephrase_question(question):
    input_text = f"rephrase: {question}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_beams=5, early_stopping=True)
    rephrased_question = tokenizer.decode(output[0], skip_special_tokens=True)
    return rephrased_question

if __name__ == "__main__":
    main()
