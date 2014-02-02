/*
 * Bootstrap v3.0.0
 * 
 * Modal nav using arrow keys
 */
 
var officer_modal = 0;
var officer_total = 3;

var officer_alive = 0;

$(document.documentElement).keyup(function (event) {
  if (officer_alive == 1) {
  
    // handle cursor keys
    if (event.keyCode == 37) {
      //left arrow
      $('#officer-modal' + officer_modal).modal('hide');
      $('#officer-modal' + mod(officer_modal - 1,officer_total)).modal('show');
    } else if (event.keyCode == 39) {
      // right arrow
      $('#officer-modal' + officer_modal).modal('hide');
      $('#officer-modal' + mod(officer_modal + 1,officer_total)).modal('show');
    }
    
  }
});

for (var i = 0; i < officer_total; i++) {
  show_event_i_fixed(i);
  hide_event_i_fixed(i);
}

function show_event_i_fixed(i) {
  $('#officer-modal' + i).on('show.bs.modal', function () {
    officer_modal = i;
    officer_alive = 1;
  });
}

function hide_event_i_fixed(i) {
  $('#officer-modal' + i).on('hide.bs.modal', function () {
    officer_alive = 0;
  });
}

/*
 * Positive modulo function (user defined)
 */

function mod(n, m) {
        return ((n % m) + m) % m;
}