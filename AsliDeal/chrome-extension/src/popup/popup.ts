// This file contains the logic for the popup, including fetching data from the backend and rendering the results.

import { fetchVerificationResult } from '../lib/api';

document.addEventListener('DOMContentLoaded', () => {
    const verifyButton = document.getElementById('verify-button');
    const resultContainer = document.getElementById('result-container');

    verifyButton.addEventListener('click', async () => {
        const url = document.getElementById('url-input').value;
        if (!url) {
            resultContainer.textContent = 'Please enter a valid URL.';
            return;
        }

        resultContainer.textContent = 'Verifying...';
        try {
            const result = await fetchVerificationResult(url);
            resultContainer.textContent = result.isValid 
                ? `The discount is valid: ${result.discountPercentage}% off!` 
                : 'The discount is not valid.';
        } catch (error) {
            resultContainer.textContent = 'Error verifying the discount. Please try again.';
            console.error('Verification error:', error);
        }
    });
});