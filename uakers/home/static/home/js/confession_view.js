document.addEventListener('DOMContentLoaded', function(){

  let textareas = document.getElementsByTagName('textarea');

  for (let txa=0; txa<textareas.length; txa++){

    textareas[txa].addEventListener('input', function(){
      if (textareas[txa].value == ''){
        textareas[txa].style.height = '35px';
      } else {
        let scrh = textareas[txa].scrollHeight + 4
        textareas[txa].style.height = scrh + 'px';
        console.log(textareas[txa].scrollHeight)
      }
    });
  }

});
