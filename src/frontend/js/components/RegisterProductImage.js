import { apiCall } from '../api.js';
import { setupAutocomplete } from '../utils/autocomplete.js';
import { showErrorPopup } from '../errorHandler.js';

export class RegisterProductImage {
    constructor() {
        this.form = document.getElementById('imageProductForm');
        this.productInput = document.getElementById('imageProductName');
        this.spinner = document.getElementById('spinner');
        this.resultDiv = document.getElementById('imageProductResult');
        this.confirmButton = document.getElementById('confirmImageProduct');
        this.setupEventListeners();
        this.setupAutocomplete();
    }

    setupEventListeners() {
        this.form.addEventListener('submit', this.handleSubmit.bind(this));
        this.confirmButton.addEventListener('click', this.handleConfirm.bind(this));
    }

    setupAutocomplete() {
        const resultsElement = this.productInput.nextElementSibling;
        setupAutocomplete(this.productInput, resultsElement);
    }

    async handleSubmit(e) {
        e.preventDefault();
        this.spinner.style.display = 'block';
        this.resultDiv.style.display = 'none';

        const formData = new FormData(this.form);

        try {
            const response = await fetch(`${API_BASE_URL}/product/register-image-input`, {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const error = await response.json();
                throw error;
            }

            const result = await response.json();
            this.displayProductInfo(result.product);
        } catch (error) {
            console.error('Error reading product from image:', error);
            showErrorPopup(error.error || 'Failed to read product from image', error.error_type, error.stack_trace);
        } finally {
            this.spinner.style.display = 'none';
        }
    }

    async handleConfirm() {
        const productInfoDiv = document.getElementById('imageProductInfo');
        const product = JSON.parse(productInfoDiv.dataset.product);

        try {
            const response = await apiCall('/product/register-confirm-image-input', 'POST', product);
            alert('Product registered successfully!');
            this.form.reset();
            this.resultDiv.style.display = 'none';
        } catch (error) {
            console.error('Error confirming product:', error);
            showErrorPopup(error.error || 'Failed to confirm product', error.error_type, error.stack_trace);
        }
    }

    displayProductInfo(product) {
        const productInfoDiv = document.getElementById('imageProductInfo');
        productInfoDiv.innerHTML = `
            <p><strong>Name:</strong> ${product.name}</p>
            <p><strong>Calories (per 100g):</strong> ${product.kcal_100g}</p>
            <p><strong>Proteins (per 100g):</strong> ${product.proteins_100g}g</p>
            <p><strong>Carbohydrates (per 100g):</strong> ${product.carbs_100g}g</p>
            <p><strong>Fats (per 100g):</strong> ${product.fats_100g}g</p>
        `;
        productInfoDiv.dataset.product = JSON.stringify(product);
        this.resultDiv.style.display = 'block';
    }
}