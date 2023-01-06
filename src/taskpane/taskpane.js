// script.js

const inputField = document.getElementById("inputField");
const submitButton = document.getElementById("submitButton");
const outputField = document.getElementById("outputField");

submitButton.addEventListener("click", () => {
  const input = inputField.value;

  // Make a GET request to the FastAPI endpoint to generate the formula
  fetch("http://127.0.0.1:8000/generate_formula/" + input, {
    method: "GET"
  })
    .then(response => response.json())
    .then(data => {
      // Access the generated formula in the JSON object returned by the FastAPI endpoint
      const formula = data.formula;
      // Set the text content of the output field to the generated formula
      outputField.textContent = formula;
    });
});
