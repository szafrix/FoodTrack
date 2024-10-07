import { handleApiError } from './errorHandler.js';

const API_BASE_URL = window.location.origin;

export async function apiCall(endpoint, method, data) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        const result = await response.json();
        if (!response.ok) {
            throw result;
        }
        return result;
    } catch (error) {
        handleApiError(error);
        throw error;
    }
}