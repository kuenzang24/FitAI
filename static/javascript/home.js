const multistepForm = document.querySelector("[data-multi-step]");
const fromSteps = [...multistepForm.querySelectorAll("[data-step]")];

// Getting the current page number
let currentStep = fromSteps.findIndex((step) => {
  return step.classList.contains("active");
});

if (currentStep < 0) {
  currentStep = 0;
  showCurrentStep();
}

multistepForm.addEventListener("click", (e) => {
    let incrementor;
  if (e.target.matches("[data-next]")) {
    incrementor = 1;
  } else if (e.target.matches("[data-previous]")) {
    incrementor = -1;
  } 

  if(incrementor == null)return 
  const inputs =[...fromSteps[currentStep].querySelectorAll("input")];

  const allValid = inputs.every(input => input.reportValidity());

  console.log(allValid)

  if(allValid){
    currentStep += incrementor
    showCurrentStep();
  }

});

function showCurrentStep() {
  fromSteps.forEach((step, index) => {
    step.classList.toggle("active", index === currentStep);
  });
}
