// ===== BASE JAVASCRIPT =====

// Simple like button toggle
function toggleLike(button) {
    var icon = button.querySelector('i');
    var countSpan = button.querySelector('.like-count');

    if (icon.classList.contains('bi-heart')) {
        // Like the post
        icon.classList.remove('bi-heart');
        icon.classList.add('bi-heart-fill');
        icon.style.color = 'red';
        if (countSpan) {
            countSpan.textContent = parseInt(countSpan.textContent) + 1;
        }
    } else {
        // Unlike the post
        icon.classList.remove('bi-heart-fill');
        icon.classList.add('bi-heart');
        icon.style.color = '';
        if (countSpan) {
            countSpan.textContent = parseInt(countSpan.textContent) - 1;
        }
    }
}

// Simple alert for placeholder actions
function showAlert(message) {
    alert(message);
}

// Auto-hide Django messages after 3 seconds
document.addEventListener('DOMContentLoaded', function () {
    var alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.display = 'none';
        }, 3000);
    });
});
