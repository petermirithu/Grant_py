$(document).ready(function(){  
  $('#form2').submit(function(event){
    event.preventDefault()
    form=$('#form2')
        
    $.ajax({      
      url:'/ajax/review/',
      type:'POST',
      data:form.serialize(),
      dataType:'json',   
      success:function(data){        
        alert(data['success']);
        $('.json_stuf').prepend('<div class="card" style="width:650px">' +
          '<p><img class="rounded-circle" src="https://cdn4.iconfinder.com/data/icons/human-user-business-person-avatars/100/23A-1User-512.png" width="40px" heigth="40px"><b>' + '  ' + data['posted_by'] + '</b>' + '  ' + data['body'] + '</p>' +
          '<p>' + data['posted_on'] + '</p>' +
        '</div>'
        );
      },
    })      
    $('#id_body').val('')
  })

  $('#rate').submit(function(event){
    event.preventDefault()
    form=$('#rate')
        
    $.ajax({      
      url:'/rate/',
      type:'POST',
      data:form.serialize(),
      dataType:'json',   
      success:function(data){        
        alert(data['success']);                
      },
    })      
    document.getElementById("rate").reset();
  })
})
