(function(){var d=document,q=function(s,r){return Array.prototype.slice.call((r||d).querySelectorAll(s))};
/* P3: show only differences */
q('[data-ct]').forEach(function(w,i){var t=w.querySelector('table'),c=t.querySelector('.cnt'),rows=q('tbody tr',t);
var l=d.createElement('label');l.className='difft';l.innerHTML='<input type="checkbox"> Show only differences';w.parentNode.insertBefore(l,w);
function upd(on){var n=0;rows.forEach(function(r){var v=q('td',r).map(function(x){return x.textContent.replace(/src$/,'').trim()});var same=v.length>1&&v.every(function(x){return x===v[0]});r.hidden=on&&same;if(!r.hidden)n++});c.textContent='Showing '+n+' of '+rows.length+' features'}
l.firstChild.addEventListener('change',function(e){upd(e.target.checked)});upd(false)});
})();
