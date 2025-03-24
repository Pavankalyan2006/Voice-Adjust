document.getElementById("start").addEventListener("click", () => {
    const gender = document.querySelector('input[name="gender"]:checked').value;

    fetch('/process_voice', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ gender: gender })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("inputHz").textContent = data.input_pitch;
        document.getElementById("adjustedHz").textContent = data.adjusted_pitch;
        document.getElementById("selectedGender").textContent = data.gender.charAt(0).toUpperCase() + data.gender.slice(1);
    })
    .catch(error => console.error("Error:", error));
});
