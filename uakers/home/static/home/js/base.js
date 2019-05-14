document.addEventListener('DOMContentLoaded', function(){

  let mn_wrapper = document.getElementsByClassName('mn-wrapper')[0];

  if (mn_wrapper){
    mn_wrapper.addEventListener('click', function(){

      let lnn = document.getElementsByClassName('live_notification_number')[0];
      let live_href_read = lnn.getAttribute('data-href-read');

      let mn_drop_list = document.getElementsByClassName('mn-drop-list')[0];

      if(mn_drop_list.classList.contains('mn-drop-list-active')){
        mn_drop_list.classList.remove('mn-drop-list-active');
      } else {
        mn_drop_list.classList.add('mn-drop-list-active');

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        function read_notification(){
          $.ajax({
            type: "POST",
            url: live_href_read,

            success: function(data){
            }
          });

        }

        read_notification();
      }

    });
  }


  let co_upd_iu = document.getElementsByClassName('co-upd-iu');


  for (let cui=0; cui<co_upd_iu.length; cui++){
    co_upd_iu[cui].addEventListener('click', function(){

      let co_voters = co_upd_iu[cui].parentNode.parentNode.parentNode.getElementsByClassName('co_voters')[0];

      co_voters.style.display = "block";

    });
  }


  let co_remove_layer = document.getElementsByClassName('co_remove_layer');

  for(crl=0; crl<co_remove_layer.length; crl++){

    co_remove_layer[crl].addEventListener('click', function(){

      let co_voters_close = this.parentNode;
      co_voters_close.style.display = 'none';

    });
  }

  //for(crl=0; crl<co_remove_layer; crl++){
    //console.log(co_remove_layer[crl]);
  //}

});
