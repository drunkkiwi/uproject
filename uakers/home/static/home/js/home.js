document.addEventListener('DOMContentLoaded', function(){

  let ns_text = document.getElementsByClassName('ns-text')[0];

  if (ns_text){
    ns_text.addEventListener('click', function(){
      let post_conf = document.getElementsByClassName('post-conf')[0];
      if (post_conf.classList.contains('post-conf-zero')){
        post_conf.classList.remove('post-conf-zero');
        ns_text.innerHTML = 'Click this bar to remove confession box';
      } else {
        post_conf.classList.add('post-conf-zero');
        ns_text.innerHTML = 'Click this bar to confess';
      }
    });
  }

});
