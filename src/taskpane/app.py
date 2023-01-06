from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import openai
import uvicorn

openai.api_key = "PUT YOUR API KEY"

app = FastAPI()

# Configure CORS to allow requests from the origin of the taskpane HTML file
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_formula(input_string: str) -> str:
    # Use the OpenAI API to generate a formula based on the input string
    prompt = f"Generate an Excel formula based on the following input:\n{input_string}"
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
    formula = completions.choices[0].text

    # Check for common mistakes or misunderstandings in the input string
    if "?" in formula:
        return "Error: Could not understand input. Please check your syntax and try again."
    elif "N/A" in formula:
        return "Error: Could not generate formula. Please check your input and try again."

    return formula

@app.get("/generate_formula/{input_string}")
def get_generate_formula(input_string: str):
    return {"formula": generate_formula(input_string)}

if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)
