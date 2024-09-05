describe('UI Tests', () => {
    it('Should start the sorting process when Start button is clicked', () => {
        const startButton = document.getElementById('start-button');
        startButton.click();
        // Assertions for start logic
    });

    it('Should stop the sorting process when Stop button is clicked', () => {
        const stopButton = document.getElementById('stop-button');
        stopButton.click();
        // Assertions for stop logic
    });

    it('Should change the mode when the dropdown is selected', () => {
        const modeSelect = document.getElementById('sorting-mode');
        modeSelect.value = 'manual';
        modeSelect.dispatchEvent(new Event('change'));
        // Assertions for mode change logic
    });
});
