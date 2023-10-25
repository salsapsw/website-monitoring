const btn1 = document.getElementById('btnUtama1');
const btn2 = document.getElementById('btnUtama2');
const selectBox1 = document.getElementById('selectBox1');
const selectBox2 = document.getElementById('selectBox2');


btn1.addEventListener('click', function() {
  selectBox1.style.display = 'block';
    btn1.style.display = 'none';
    btn2.style.display = 'none';
    selectBox2.style.display = 'none';
});

btn2.addEventListener('click', function() {
    selectBox2.style.display = 'block';
    btn1.style.display = 'none';
    btn2.style.display = 'none';
    selectBox1.style.display = 'none';
  });