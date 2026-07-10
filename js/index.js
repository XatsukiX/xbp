 function routeToLog(){
    var hash = window.location.hash; // 例: #/log/xbp-1
    var match = hash.match(/^#\/log\/([a-zA-Z0-9-]+)$/);
    var home = document.getElementById('home');
    var pages = document.querySelectorAll('.detail-page');

    if(match){
      var targetId = 'page-' + match[1];
      var found = false;
      pages.forEach(function(page){
        if(page.id === targetId){
          page.classList.add('active');
          found = true;
        } else {
          page.classList.remove('active');
        }
      });
      if(found){
        home.style.display = 'none';
        window.scrollTo(0,0);
        return;
      }
    }

    // 該当するログが無い場合、またはトップ表示の場合
    pages.forEach(function(page){ page.classList.remove('active'); });
    home.style.display = 'block';
  }

  window.addEventListener('hashchange', routeToLog);
  window.addEventListener('DOMContentLoaded', routeToLog);