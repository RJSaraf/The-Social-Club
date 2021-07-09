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


  ///////////////////////////////////////////////////

/*

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


<script>

                    console.log(window.location)
                    var loc = window.location
                    var myForm = $('.msgform')
                    var msgInput = $('#msg-text')

                    var wsStart = 'ws://'
                    if(loc.protocol == 'https:'){
                        wsStart = 'wss://'
                    }

                    var endpoint = wsStart + loc.host + loc.pathname
                    var socket = new ReconnectingWebSocket(endpoint)

                    socket.onmessage = function(e){
                        console.log(e.data)
                        chatbox.append()
                    }
                    socket.onopen = function(e){
                        console.log('open', e)

                          myForm.submit(function(event){
                            event.preventDefault();
                            var msgtext = msgInput.val()
                            var data_dict = {'message':msgtext}
                            socket.send(JSON.stringify(data_dict))
                            myForm[0].reset()
                        })
                    }
                    socket.onerror = function(e){
                        console.log('error', e)
                    }
                    socket.onclose = function(e){
                        console.log('close', e)
                    }
                         
            </script>
  
*/