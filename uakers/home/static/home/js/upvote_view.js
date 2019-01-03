let udbuttons = document.getElementsByClassName('co-upd');

// ------------- get cookie function --------------
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// --------------------- safe method function ------------------
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// ------ looping every upvote/downvote button -------
for(let u = 0; u<udbuttons.length; u++){

  udbuttons[u].addEventListener('click', function(e){

// ------- preventing subbmition --------
    e.preventDefault();
      // ------ upvote/downvote button target -----------
    let udhref = udbuttons[u].href;

  // ----------------- using the cookie function to get csrf token -------------
    let csrftoken = getCookie('csrftoken');

  // -------------- Setting up ajax so we insert the csrf token ---------------
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
      type: "POST",
      url: udhref,

      success: function(data){
        let ud_i_clicked = e.target;
        let ud_upvotes = udbuttons[u].parentNode.parentNode.getElementsByClassName('co-upd-info')[0].getElementsByClassName('co-upd-iu')[0].getElementsByClassName('ff-num')[0];

        let das = data.alert_state;
        let dau = data.alert_upvote_state;
        if(das == 'Upvoted'){
          ud_i_clicked.classList.add('co-upd-i-active');
          let ud_i_sibling = ud_i_clicked.parentNode.parentNode.getElementsByClassName('co-upd-downvote')[0].getElementsByClassName('co-upd-i')[0];
          if(ud_i_sibling.classList.contains('co-upd-i-active')){
            ud_i_sibling.classList.remove('co-upd-i-active');
          }

          ud_upvotes.innerHTML = dau;

        }
        else if(das == 'Unupvoted'){
          ud_i_clicked.classList.remove('co-upd-i-active');
          ud_upvotes.innerHTML = dau;
        }
        else if(das == 'Undownvoted'){
          ud_i_clicked.classList.remove('co-upd-i-active');
          ud_upvotes.innerHTML = dau;
        }
        else if(das == 'Downvoted'){
          ud_i_clicked.classList.add('co-upd-i-active');
          let ud_i_sibling = ud_i_clicked.parentNode.parentNode.getElementsByClassName('co-upd-upvote')[0].getElementsByClassName('co-upd-i')[0];
          if(ud_i_sibling.classList.contains('co-upd-i-active')){
            ud_i_sibling.classList.remove('co-upd-i-active');
          }

          ud_upvotes.innerHTML = dau;
        }
      }
    });

  })
}
