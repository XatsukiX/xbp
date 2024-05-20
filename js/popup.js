document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.item');
    const popup = document.getElementById('popup');
    const description = document.getElementById('description');
    const close = document.getElementById('close');

    items.forEach(item => {
        item.addEventListener('click', function() {
            description.textContent = item.getAttribute('data-description');
            popup.style.display = 'block';
        });
    });

    close.addEventListener('click', function() {
        popup.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
});
