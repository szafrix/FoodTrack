import { RegisterIntake } from './components/RegisterIntake.js';
import { RegisterProductManual } from './components/RegisterProductManual.js';
import { RegisterProductImage } from './components/RegisterProductImage.js';
import { handleApiError, hideErrorPopup } from './errorHandler.js';
import { openTab } from './utils/tabHandler.js';

document.addEventListener('DOMContentLoaded', () => {
    new RegisterIntake();
    new RegisterProductManual();
    new RegisterProductImage();

    // Set up global error handling
    window.addEventListener('error', (event) => {
        handleApiError({
            error: event.message,
            error_type: 'ClientError',
            stack_trace: event.error?.stack
        });
    });

    // Close error popup when clicking outside or on close button
    document.querySelector('.close-btn').addEventListener('click', hideErrorPopup);
    window.addEventListener('click', function (event) {
        const popup = document.getElementById('errorPopup');
        if (event.target == popup) {
            hideErrorPopup();
        }
    });

    // Make openTab function globally available
    window.openTab = openTab;

    // Open the default tab
    document.getElementById("defaultOpen").click();
});