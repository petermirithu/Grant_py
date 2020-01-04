$(document).ready(function(){  
  $('form').submit(function(event){
    event.preventDefault()
    form=$("form")
    
    $.ajax({
      url:'/ajax/review/<int:projo_id>',
      type:'POST',
      data:form.serialize(),
      dataType:'json',   
      success:function(data){
        alert('Successfully added you review...')
      },
    })        
  })
})
