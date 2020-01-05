$(document).ready(function(){  
  $('#review_form').on('submit',function(event){
    event.preventDefault()
    form= $('#review_form')
    
    $.ajax({
      url:'/ajax/review/<int:projo_id>',
      type:'POST',
      data:form.serialize(),
      dataType:'json',   
      success:function(data){
        alert(data['success'])
        $('#id_body').val('')
      },
    })      
  })
})
