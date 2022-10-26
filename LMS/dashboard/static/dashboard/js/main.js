let closeBtn = document.querySelector('.notification__close');
let notificationBlock = document.querySelector('.notification');
let dropdownLink = document.getElementById('dropdownlink');
let dropdownItem = document.querySelector('.item-dropdown');


document.getElementById('dropdownlink').onclick = function(e) {
    dropdownItem.classList.toggle('active');
    e.preventDefault();
}

