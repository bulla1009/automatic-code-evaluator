import streamlit as st
import anthropic

# In-memory storage for the submitted code
stored_code = None

# Function to handle code submission
def submit_code(code):
    global stored_code
    stored_code = code

# Streamlit app layout
st.title("Python IDE")
st.subheader("Write your Python code below:")

code = st.text_area("Code Editor", height=300)
prompt = f"""
\n\nHuman: Please act as a code evaluator. Evaluate the following code snippet based on four criteria: Correctness, Style, Efficiency, and Error Handling. 

For each criterion, provide a detailed analysis and a score from 1 to 10, where 1 is the lowest and 10 is the highest. 

The criteria are defined as follows:
1. Correctness: Does the code achieve its intended purpose correctly?
2. Style: Does the code follow good programming practices and conventions, including naming conventions, indentation, and comments?
3. Efficiency: Is the code optimized for performance, considering time and space complexity?
4. Error Handling: Does the code handle potential errors and edge cases appropriately?

Here is the code snippet:
\n\n{code}\n\nAssistant:
"""
if st.button("Submit Code"):
    if code.strip():
        submit_code(code)
        st.success("Code submitted successfully.")
    else:
        st.warning("Please enter some code before submitting.")

api_key_ant = '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'
def evaluate_code(code):
    client = anthropic.Client(api_key=api_key_ant)
    response = client.completions.create(
        model='claude-v1',  # Use a valid model name
        max_tokens_to_sample=1024,
        prompt=prompt
    )
    return response.completion
feedback = evaluate_code(code)
# Extracting and printing the feedback
st.markdown(f"**{feedback}**")