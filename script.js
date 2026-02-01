document.getElementById("surveyForm").onsubmit = async (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target));

  await fetch("/submit", {
    method:"POST",
    headers:{ "Content-Type":"application/json" },
    body: JSON.stringify(data)
  });

  alert("Thank you 💚 Survey submitted!");
  e.target.reset();
};
