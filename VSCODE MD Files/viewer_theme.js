(function(){
  function safeJsonParse(s, fallback){ try{ return JSON.parse(s); }catch(e){ return fallback; } }
  const body = document.body;

  const toggleBtn = document.querySelector('[data-action="toggle-sidebar"]');
  if(toggleBtn){
    toggleBtn.addEventListener('click', function(){ body.classList.toggle('sidebar-open'); });
  }

  document.addEventListener('click', function(e){
    if(!body.classList.contains('sidebar-open')) return;
    const sidebar = document.getElementById('sidebar');
    if(!sidebar) return;
    const inside = sidebar.contains(e.target);
    const isToggle = e.target && e.target.closest && e.target.closest('[data-action="toggle-sidebar"]');
    if(!inside && !isToggle){ body.classList.remove('sidebar-open'); }
  });

  const STORAGE_KEY = 'rv_nav_open';
  const nav = document.getElementById('nav');
  if(nav){
    const details = Array.from(nav.querySelectorAll('details.nav-dir[data-path]'));
    const openSet = new Set(safeJsonParse(localStorage.getItem(STORAGE_KEY), []));
    details.forEach(d => {
      const p = d.getAttribute('data-path') || '';
      if(p && openSet.has(p)) d.open = true;
      d.addEventListener('toggle', () => {
        const path = d.getAttribute('data-path') || '';
        if(!path) return;
        if(d.open) openSet.add(path); else openSet.delete(path);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(openSet)));
      });
    });

    const collapseAll = document.querySelector('[data-action="collapse-all"]');
    if(collapseAll){
      collapseAll.addEventListener('click', () => {
        details.forEach(d => d.open = false);
        localStorage.setItem(STORAGE_KEY, '[]');
      });
    }
  }

  document.addEventListener('keydown', function(e){
    const tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : '';
    const inInput = tag === 'input' || tag === 'textarea' || (e.target && e.target.isContentEditable);

    if((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')){
      e.preventDefault();
      const s = document.querySelector('input[type="search"]');
      if(s) s.focus();
      return;
    }
    if(inInput) return;

    if(e.key === '['){
      const prev = document.querySelector('.footer-nav a:first-child');
      if(prev && prev.getAttribute('href')) window.location.href = prev.getAttribute('href');
    }
    if(e.key === ']'){
      const links = document.querySelectorAll('.footer-nav a');
      const next = links.length > 1 ? links[1] : null;
      if(next && next.getAttribute('href')) window.location.href = next.getAttribute('href');
    }
    if(e.key === 'Escape'){ body.classList.remove('sidebar-open'); }
  });
})();
