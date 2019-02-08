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

let csrftoken = getCookie('csrftoken');

let lnn = document.getElementsByClassName('live_notification_number')[0];
let livehref = lnn.getAttribute('data-href');

// --------------------- safe method function ------------------
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}



$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function fetch_live_list(){
  $.ajax({
    type: "POST",
    url: livehref,

    success: function(data){
      let drplist = document.getElementsByClassName('mn-drop-list')[0];
      for (let z=0; z<data.live_notification_list.length; z++){
        console.log(data.live_notification_list[z]);
        console.log(drplist);
        let lnn = document.getElementsByClassName('live_notification_number')[0];
        lnn.innerHTML = data.live_notification_count;
        let newdata = data.live_notification_list[z];
        let extraS = '';

        if (newdata.notification_type == 'follow'){
          extraS = 'followed you';
        } else if (newdata.notification_type == 'likeConf'){
          extraS = 'liked your confession';
        } else if (newdata.notification_type == 'likeCom'){
          extraS = 'liked your comment';
        }

        let htmlel = document.createElement('a');
        htmlel.setAttribute('href', newdata.notification_url);
        htmlel.innerHTML = '<div class="mn-drop-item mn-drop-item-new"><div class="mn-usr-photo" style="background-image: url(' + newdata.notification_image + ')"></div>' + newdata.notification_init + ' ' + extraS + '</div>';
        drplist.insertBefore(htmlel, drplist.firstChild);
      }
    }
  });

}


setInterval(fetch_live_list, 5000)
