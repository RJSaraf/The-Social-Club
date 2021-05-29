var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("nav").style.top = "0";
    } else {
        document.getElementById("nav").style.top = "-115px";
    }
    prevScrollpos = currentScrollPos;
}


function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }

  function hide(){
    var element = document.getElementById("pmsgfile");
    element.classList.toggle("d-block");

  }


  ///////////////////////////////////////////////////

/*

function hallo() { alert("Hello! YE SEVA ABHI UPLABDH NAHI HAI"); }

(document).ready(function(){
  var $myForm = $('')
  $myForm.submit(function(event){
    event.preventDefault()
  var $formdata = $(this).serialize()
  var $thisurl = $myForm.attr('action')
  
  $.ajax({
      method:'POST',
      url: $thisurl,
      data: $formdata,
      success: function() {
          $($myForm).fadeOut(800, function(){
              $myForm.html().fadeIn().delay(2000);

          });
      }

      
  })
  console.log($formdata)
  console.log($thisurl)  
  })
  });

  
  $(document).ready(function(){
    setInterval(function(){
          $("#chatbox").load(window.location.href + " #chatbox" );
    }, 3000);
    });
  
*/