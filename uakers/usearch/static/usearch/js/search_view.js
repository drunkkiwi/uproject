document.addEventListener('DOMContentLoaded', function(){

  let search_types = document.getElementsByClassName('s_type');

  for (let i=0; i<search_types.length; i++) {
    search_types[i].addEventListener('click', function(){
      this.submit();
    });
  }


});
