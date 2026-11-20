const toggle=document.querySelector('.menu-toggle');const nav=document.querySelector('nav');
toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus()}});
const dialog=document.querySelector('.lightbox');let opener;
document.querySelectorAll('[data-lightbox]').forEach(a=>a.addEventListener('click',e=>{if(!dialog.showModal)return;e.preventDefault();opener=a;dialog.querySelector('img').src=a.href;dialog.querySelector('img').alt=a.querySelector('img').alt;dialog.showModal()}));
dialog.querySelector('button').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close()});dialog.addEventListener('close',()=>opener?.focus());
const navDetails=document.querySelectorAll('.nav-group');
document.addEventListener('click',e=>{navDetails.forEach(d=>{if(!d.contains(e.target))d.open=false})});
document.addEventListener('keydown',e=>{if(e.key==='Escape')navDetails.forEach(d=>d.open=false)});
