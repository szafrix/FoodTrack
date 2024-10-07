import { apiCall } from '../api.js';
import { setupAutocomplete } from '../utils/autocomplete.js';

export class RegisterProductManual {
    constructor() {
        this.form = document.getElementById('manualProductForm');
        this.productInput = document.getElementById('manualProductName');
        this.setupEventListeners();
        this.setupAutocomplete();
    }

    setupEventListeners() {
        this.form.addEventListener('submit', this.handleSubmit.bind(this));
    }

    setupAutocomplete() {
        const resultsElement = this.productInput.nextElementSibling;
        setupAutocomplete(this.productInput, resultsElement);
    }

    async handleSubmit(e) {
        e.preventDefault();
        const data = {
            name: this.productInput.value,
            kcal_100g: parseFloat(document.getElementById('kcal').value),
            proteins_100g: parseFloat(document.getElementById('proteins').value),
            carbs_100g: parseFloat(document.getElementById('carbs').value),
            fats_100g: parseFloat(document.getElementById('fats').value)
        };
        try {
            const response = await apiCall('/product/register-manual-input', 'POST', data);
            this.displayProductInfo(response.product);
            document.getElementById('manualProductResult').style.display = 'block';
        } catch (error) {
            console.error('Error registering product:', error);
        }
    }

    displayProductInfo(product) {
        const productInfoDiv = document.getElementById('manualProductInfo');
        productInfoDiv.innerHTML = `
            <p><strong>Name:</strong> ${product.name}</p>
            <p><strong>Calories (per 100g):</strong> ${product.kcal_100g}</p>
            <p><strong>Proteins (per 100g):</strong> ${product.proteins_100g}g</p>
            <p><strong>Carbohydrates (per 100g):</strong> ${product.carbs_100g}g</p>
            <p><strong>Fats (per 100g):</strong> ${product.fats_100g}g</p>
        `;
    }
}