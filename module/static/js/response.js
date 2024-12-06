document.addEventListener('DOMContentLoaded', () => {
    const goalsGroups = document.querySelectorAll('.goals-group');

    goalsGroups.forEach((group) => {
        group.addEventListener('click', () => {
            const goalsEl = group.querySelector('.goals');
            const goalsText = goalsEl.textContent;
            navigator.clipboard.writeText(goalsText).then(() => {
                showNotification('Text copied to clipboard!');
            });
        });
    });
});

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('fade-out');
        notification.addEventListener('transitionend', () => {
            notification.remove();
        });
    }, 2000);
}