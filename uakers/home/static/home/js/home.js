document.addEventListener('DOMContentLoaded', function(){

  let ns_text = document.getElementsByClassName('ns-text')[0];

  //let rin = 'zoomInUp';
  //let rout = 'zoomOutUp';

  let rin = 'fadeInDown';
  let rout = 'fadeOutUp';

  if (ns_text){
    ns_text.addEventListener('click', function(){
      let post_conf = document.getElementsByClassName('post-conf')[0];
      if (post_conf.classList.contains('post-conf-zero')){
        post_conf.classList.remove('post-conf-zero');
        post_conf.classList.remove(rout);
        post_conf.classList.add(rin);
        ns_text.innerHTML = 'Click this bar to remove confession box';
      } else {
        post_conf.classList.remove(rin);
        post_conf.classList.add(rout);

        setTimeout(function(){
          post_conf.classList.add('post-conf-zero');
        }, 400);
        ns_text.innerHTML = 'Click this bar to confess';
      }
    });
  }

});
