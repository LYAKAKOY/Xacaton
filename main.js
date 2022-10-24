let closeBtn = document.querySelector('.notification__close');
let notificationBlock = document.querySelector('.notification');

setTimeout(function() {
    document.querySelector('.notification').classList.toggle('closed');
    if (document.querySelector('.closed')) {
        setTimeout(function() {
            document.querySelector('.notification').remove();
        }, 400);
    }
}, 10000);

closeBtn.onclick = function () {
    notificationBlock.classList.toggle('closed')
    setTimeout(function() {
        document.querySelector('.notification').remove();
    }, 400);
}

