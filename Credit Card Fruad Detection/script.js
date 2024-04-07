// script.js
document.getElementById('fraudDetectionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data
    const cardNumber = document.getElementById('cardNumber').value;
    const expirationDate = document.getElementById('expirationDate').value;
    const cvv = document.getElementById('cvv').value;
    const transactionAmount = document.getElementById('transactionAmount').value;

    // Perform fraud detection (dummy example)
    const isFraudulent = Math.random() < 0.1; // 10% chance of being fraudulent

    // Display result
    const resultDiv = document.getElementById('result');
    if (isFraudulent) {
        resultDiv.innerText = 'Transaction flagged as potentially fraudulent. Please contact customer support.';
        resultDiv.style.color = 'red';
    } else {
        resultDiv.innerText = 'Transaction approved.';
        resultDiv.style.color = 'green';
    }
});