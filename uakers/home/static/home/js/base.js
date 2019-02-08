document.addEventListener('DOMContentLoaded', function(){

  let mn_wrapper = document.getElementsByClassName('mn-wrapper')[0];

  mn_wrapper.addEventListener('click', function(){

    let mn_drop_list = document.getElementsByClassName('mn-drop-list')[0];

    if(mn_drop_list.classList.contains('mn-drop-list-active')){
      mn_drop_list.classList.remove('mn-drop-list-active');
    } else {
      mn_drop_list.classList.add('mn-drop-list-active');
    }

  });

});
