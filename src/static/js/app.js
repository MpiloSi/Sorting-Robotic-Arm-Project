document.addEventListener("DOMContentLoaded", function() {
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");
    const modeSelect = document.getElementById("sorting-mode");

    // Start Sorting
    startButton.addEventListener("click", () => {
        fetch('/api/start-sorting', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => alert(data.status))
        .catch(error => console.error('Error:', error));
    });

    // Stop Sorting
    stopButton.addEventListener("click", () => {
        fetch('/api/stop-sorting', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => alert(data.status))
        .catch(error => console.error('Error:', error));
    });

    // Mode selection
    modeSelect.addEventListener("change", () => {
        alert(`Mode changed to ${modeSelect.value}`);
    });
});
