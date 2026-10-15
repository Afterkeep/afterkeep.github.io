(function(){var d=document,q=function(s,r){return Array.prototype.slice.call((r||d).querySelectorAll(s))};
/* P3: show only differences */
q('[data-ct]').forEach(function(w,i){var t=w.querySelector('table'),c=t.querySelector('.cnt'),rows=q('tbody tr',t);
var l=d.createElement('label');l.className='difft';l.innerHTML='<input type="checkbox"> Show only differences';w.parentNode.insertBefore(l,w);
function upd(on){var n=0;rows.forEach(function(r){var v=q('td',r).map(function(x){return x.textContent.replace(/src$/,'').trim()});var same=v.length>1&&v.every(function(x){return x===v[0]});r.hidden=on&&same;if(!r.hidden)n++});c.textContent='Showing '+n+' of '+rows.length+' features'}
l.firstChild.addEventListener('change',function(e){upd(e.target.checked)});upd(false)});

/* P4: filters with URL hash */
var f=d.getElementById('fbar');if(f){f.hidden=false;var cards=q('#tlist .card'),R={"Top pick":0,"Good":1,"Use with caution":2,"Not recommended":3};cards.forEach(function(c,i){c.dataset.i=i});
function vals(n){return q('[name='+n+']:checked',f).map(function(x){return x.value})}
function run(){var c=vals('cat'),r=vals('region'),fr=vals('price').length,rec=vals('rec').length,so=f.sort.value,n=0;
cards.forEach(function(e){var ok=(!c.length||c.indexOf(e.dataset.cat)>=0)&&(!r.length||r.indexOf(e.dataset.region)>=0)&&(!fr||/Free/.test(e.dataset.price||''))&&(!rec||/Top pick|Good/.test(e.dataset.verdict||''));if((c.length||r.length||fr||rec)&&!e.classList.contains('tc'))ok=c.length&&!r.length&&!fr&&!rec&&false;e.hidden=!ok;if(ok)n++});
q('#tlist .grid').forEach(function(g){var k=q('.card',g).sort(function(a,b){return so=='name'?a.dataset.name.localeCompare(b.dataset.name):so=='verdict'?((R[a.dataset.verdict]+1)||9)-((R[b.dataset.verdict]+1)||9):a.dataset.i-b.dataset.i});k.forEach(function(x){g.appendChild(x)});var v=k.some(function(x){return!x.hidden});g.hidden=!v;var h=g.previousElementSibling;if(h){h.hidden=!v;if(h.previousElementSibling&&h.previousElementSibling.tagName=='H2')h.previousElementSibling.hidden=!v}});
d.getElementById('fcount').textContent='Showing '+n+' of '+cards.length+' listings';
var h=[];['cat','region','price','rec'].forEach(function(k){var v=vals(k);if(v.length)h.push(k+'='+v.join(','))});if(so)h.push('sort='+so);history.replaceState(null,'',h.length?'#'+h.join('&'):location.pathname)}
function load(){var m={};location.hash.slice(1).split('&').forEach(function(p){var a=p.split('=');if(a[1])m[a[0]]=a[1].split(',')});if(!m.cat&&/^#(vaults|platforms|crypto|estate)$/.test(location.hash))m.cat=[location.hash.slice(1)];q('input',f).forEach(function(i){i.checked=!!(m[i.name]&&m[i.name].indexOf(i.value)>=0)});f.sort.value=(m.sort||[''])[0]}
f.addEventListener('change',run);f.addEventListener('reset',function(){setTimeout(run,0)});load();run()}

/* home search */
var Q=d.getElementById('q');if(Q){var I;fetch('/search.json').then(function(r){return r.json()}).then(function(x){I=x});Q.addEventListener('input',function(){var v=Q.value.toLowerCase().trim(),R=d.getElementById('results');R.textContent='';if(!v||!I)return;var m=I.filter(function(x){return(x.t+' '+x.d).toLowerCase().indexOf(v)>=0}).slice(0,8);if(!m.length){R.innerHTML='<p class=meta>No matches</p>';return}m.forEach(function(x){var a=d.createElement('a');a.href=x.u;a.textContent=x.t;R.appendChild(a)})})}
/* P7: start-here chooser */
var z=d.getElementById('chz');if(z){var M=JSON.parse(z.dataset.map);z.addEventListener('submit',function(e){e.preventDefault();var w=z.what.value,b=z.budget.value,g=z.where.value,o=M[w]||{},p=o[g]||o.other&&g!='US'&&o.other||o.any||o.US,r=d.getElementById('chr');r.innerHTML='';if(!p)return;var h=d.createElement('p'),a=d.createElement('a');a.href=p[1];a.textContent=p[0];h.appendChild(d.createTextNode('Our pick: '));h.appendChild(a);var n=d.createElement('p');n.textContent=p[2]+(b=='free'&&/Paid only|pricing/.test(p[2])?' Tip: see free tools at /tools/free/.':'');r.appendChild(h);r.appendChild(n)})}
})();