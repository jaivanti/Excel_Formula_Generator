const inputString = document.getElementById("input-string");
const outputString = document.getElementById("output-string");
const generateButton = document.getElementById("generate-button");

generateButton.addEventListener("click", function() {
  const input = inputString.value;
  fetch(`http://localhost:8000/generate_formula/${input}`)
    .then(response => response.json())
    .then(data => {
      outputString.value = data.formula;
    });
});
