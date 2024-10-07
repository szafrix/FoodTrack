import { apiCall } from '../api.js';

export function setupAutocomplete(inputElement, resultsElement) {
    inputElement.addEventListener('input', async () => {
        const query = inputElement.value;
        if (query.length < 2) {
            resultsElement.innerHTML = '';
            return;
        }

        try {
            const response = await apiCall(`/autocomplete?user_input=${encodeURIComponent(query)}`, 'GET');
            displayAutocompleteResults(response.products, resultsElement, inputElement);
        } catch (error) {
            console.error('Error fetching autocomplete results:', error);
        }
    });
}

function displayAutocompleteResults(products, resultsElement, inputElement) {
    resultsElement.innerHTML = '';
    products.forEach(product => {
        const li = document.createElement('li');
        li.textContent = product.name;
        li.addEventListener('click', () => {
            inputElement.value = product.name;
            inputElement.dataset.product = JSON.stringify(product);
            resultsElement.innerHTML = '';
        });
        resultsElement.appendChild(li);
    });
}