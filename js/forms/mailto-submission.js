/*!
 * Attempt to fix annoying lack of server side PHP with a mailto hack using javascript instead.
 */
 
$('#mailto-submission').click( function () {

  var string = "mailto:citations@yale.edu"
             + "?subject="
             + encodeURIComponent($('#contact-subject').val())
             + "&body="
             + encodeURIComponent($('#contact-message').val())
  
  console.log(string)
  
  window.location.href = string
  
});