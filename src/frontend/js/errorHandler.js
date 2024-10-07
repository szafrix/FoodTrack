function handleApiError(error) {
    console.error('API Error:', error);
    showErrorPopup(error.error, error.error_type, error.stack_trace);
}

function showErrorPopup(message, errorType, stackTrace) {
    const popup = document.getElementById('errorPopup');
    const errorMessage = document.getElementById('errorMessage');
    errorMessage.innerHTML = `
        <p><strong>Error:</strong> ${message || 'Unknown error'}</p>
        <p><strong>Type:</strong> ${errorType || 'Unknown'}</p>
        ${stackTrace ? `<details><summary>Technical Details</summary><pre>${stackTrace}</pre></details>` : ''}
    `;
    popup.style.display = 'block';
}

function hideErrorPopup() {
    document.getElementById('errorPopup').style.display = 'none';
}

// Client-side error logging
window.onerror = function (message, source, lineno, colno, error) {
    console.error('Unhandled error:', { message, source, lineno, colno, error });
    showErrorPopup('An unexpected error occurred', 'ClientError', error?.stack);
};

export { handleApiError, showErrorPopup, hideErrorPopup };