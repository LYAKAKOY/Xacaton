const input = document.getElementById('id_username');
const image = document.getElementById('griffon');

input.addEventListener('focus', onFocus);
input.addEventListener('blur', noFocus);
input.addEventListener('input', updateValue);


function changeImg(num) {
  image.src=`../../static/users/pictures/griffon/${num}.png`;
}

function onFocus(e) {

  let l1 = input.value.length;
  let n = 60;
  if (l1 == 0) {
    setTimeout("changeImg(15)", n);
    setTimeout("changeImg(13)", n*2);
    setTimeout("changeImg(11)", n*3);
    setTimeout("changeImg(9)", n*4);
    setTimeout("changeImg(7)", n*5);
    setTimeout("changeImg(5)", n*6);
    setTimeout("changeImg(3)", n*7);
    setTimeout("changeImg(1)", n*8);
  }

  if (l1 < 16) {
    if (l1 % 2 == 0) {
      l1--;
    }
    for (let i = 15, j = 30; i >= l1; j+=45, i-=2) {
      console.log(i);
      setTimeout(`changeImg(${i})`, j);
    }
  }
  if (l1 > 16) {
    if (l1 % 2 == 0) {
      l1++;
    }
    if (l1 > 31) {
        l1 = 31;
      }
    for (let i = 17, j = 30; i <= l1; j+=45, i+=2) {
      console.log(i);
      setTimeout(`changeImg(${i})`, j);
    }
  }
}

function noFocus() {
  let l1 = input.value.length;
  console.log(l1);
  if (l1 < 16) {
    if (l1 % 2 == 0) {
      l1++;
    }
    for (let i = l1, j = 30; i <= 16; j+=45, i+=2) {
      setTimeout(`changeImg(${i})`, j);
    }
  }
  if (l1 > 16) {
    if (l1 % 2 == 0) {
      l1++;
    }

        if (l1 > 31) {
      l1 = 31;
    }
    for (let i = l1, j = 30; i >= 16; j+=45, i-=2) {
      setTimeout(`changeImg(${i})`, j);
    }
  }
  setTimeout(`changeImg(16)`, 500);
}

function updateValue(e) {
  let len = e.target.value.length;

  if (len < 32 && len % 2 == 1) {
    changeImg(len);
  }
}
