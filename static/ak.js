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
var z=d.getElementById('chz');if(z){var M=JSON.parse(z.dataset.map);z.addEventListener('submit',function(e){e.preventDefault();var w=z.what.value,b=z.budget.value,g=z.where.value,o=M[w]||{},p=o[g]||o.other&&g!='US'&&o.other||o.any||o.US,r=d.getElementById('chr');r.innerHTML='';if(!p)return;var h=d.createElement('p'),a=d.createElement('a');a.href=p[1];a.textContent=p[0];h.appendChild(d.createTextNode('Our pick: '));h.appendChild(a);var n=d.createElement('p');n.textContent=p[2];r.appendChild(h);r.appendChild(n)})}

/* P8: compare tray */
var tr=d.getElementById('tray');if(tr){var bx=q('input[name=t]');bx.forEach(function(b){b.addEventListener('change',function(){var s=bx.filter(function(x){return x.checked}),c=s.length?s[0].dataset.cat:0;bx.forEach(function(x){x.disabled=c&&x.dataset.cat!=c||!x.checked&&s.length>2});tr.hidden=s.length<2;tr.href='/compare/?t='+s.map(function(x){return x.value}).join(',');tr.textContent='Compare '+s.length+' tools'})})}
var cd=d.getElementById('cmpdyn'),ts=(location.search.match(/[?&]t=([\w,-]+)/)||[])[1];if(cd&&ts)fetch('/tools.json').then(function(r){return r.json()}).then(function(J){var s=ts.split(',').filter(function(k){return J.t[k]}).slice(0,3),T=s.map(function(k){return J.t[k]});if(s.length<2||T.some(function(t){return t.c!=T[0].c}))return cd.textContent='Pick 2-3 tools from one category.';
function el(t,x,p){var e=d.createElement(t);if(x)e.textContent=x;p&&p.appendChild(e);return e}el('h2',T.map(function(t){return t.n}).join(' vs '),cd);var tb=el('table',0,el('div',0,cd)),hr=el('tr',0,el('thead',0,tb));tb.className='ct';tb.parentNode.className='ctw';el('th','Feature',hr);T.forEach(function(t,i){var h=el('th',0,hr),a=el('a',t.n,h);a.href='/tools/'+s[i]+'/'});var bd=el('tbody',0,tb);['Our verdict'].concat(J.rows[T[0].c]).forEach(function(r){var w=el('tr',0,bd);el('th',r,w);T.forEach(function(t){el('td',r=='Our verdict'?t.l:t.f[r]||'Not stated',w)})});var k=J.cmp[s.slice().sort().join('-')];if(k){var p=el('p','',cd),a=el('a','Read our full comparison',p);a.href='/compare/'+k+'/'}})

/* GA outbound clicks */
d.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[rel*=noopener]');if(!a||!/Official/.test(a.textContent))return;try{var c=a.closest('[data-name]'),n=a.nextElementSibling;gtag('event','outbound_click',{link_url:a.href,tool_name:c?c.dataset.name:d.title.split(' |')[0],affiliate:!!(n&&n.className=='affl')})}catch(x){}})
})();