function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	break;
      }
    }
  }
  return cookieValue;
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});

function get_classes(module, class_name_part)
{
  $.ajax({
    type:"POST",
    url: 'ajax/get_classes',
    data: {
      "module":module,
      "name_part":class_name_part 
    },
    dataType: 'json',
    success: function (data) {
	    $("#class_list").empty();
	    for (var option_index = 0; option_index < data.classes.length; option_index++) {
		    var option = document.createElement("option");
		    option.text = data.classes[option_index].name;
		    $("#class_list").append(option);
	    }
    },
    error: function (data) {
      alert('error');

    }
  }); 

}

window.onload =  function() {
  var module = $("#modules").val()
  var module = class_name_part = "";
  $("#modules").change(function() 
		  {
  	  module = $("#modules").val()
  	  class_name_part = $("#class_name").val();
	  get_classes(module, class_name_part)
  });
};
