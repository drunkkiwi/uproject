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

});
