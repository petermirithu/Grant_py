$(document).ready(function(){  
  $('form').submit(function(event){
    event.preventDefault()
    form=$('form')
    
    $.ajax({
      post_id:function(data){
        var x= data['post_id']
      },
      url:'/ajax/review/'+x+'/',
      type:'POST',
      data:form.serialize(),
      dataType:'json',   
      success:function(data){
        alert(data['success'])
      },
    })      
    $('#id_body').val('')
  })
})
