$(function($) {
  $('#submit-contact').click(function() {
    var data = {
      email: $('#email').val(),
      website: $('#website').val(),
      description: $('#description').val()
    }

    $.post('/contact', data, function(d, s) {
      alert('Thanks. I will be in touch with your shortly.');

      $('#email').val('');
      $('#website').val('');
      $('#description').val('');
    });

    return false;
  })
});
