import { apiCall } from '../api.js';
import { setupAutocomplete } from '../utils/autocomplete.js';

export class RegisterIntake {
    constructor() {
        this.form = document.getElementById('intakeForm');
        this.productInput = document.getElementById('productName');
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
        const product = this.productInput.dataset.product ? JSON.parse(this.productInput.dataset.product) : {
            name: this.productInput.value,
            kcal_100g: 0,
            proteins_100g: 0,
            carbs_100g: 0,
            fats_100g: 0
        };
        const data = {
            product: product,
            quantity: parseInt(document.getElementById('quantity').value),
            date: new Date(document.getElementById('intakeDate').value).toISOString()
        };
        try {
            const response = await apiCall('/intake/register', 'POST', data);
            alert(response.message);
        } catch (error) {
            console.error('Error registering intake:', error);
        }
    }
}