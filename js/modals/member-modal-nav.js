/*
 * Bootstrap v3.0.0
 * 
 * Modal nav using arrow keys
 */
 
var modal = 0;
var total = 17;

var alive = 0;

$(document.documentElement).keyup(function (event) {
  if (alive == 1) {
  
    // handle cursor keys
    if (event.keyCode == 37) {
      //left arrow
      $('#modal' + modal).modal('hide');
      $('#modal' + mod(modal - 1,total)).modal('show');
    } else if (event.keyCode == 39) {
      // right arrow
      $('#modal' + modal).modal('hide');
      $('#modal' + mod(modal + 1,total)).modal('show');
    }
    
  }
});

for (var i = 0; i < total; i++) {
  show_event_i_fixed(i);
  hide_event_i_fixed(i);
}

function show_event_i_fixed(i) {
  $('#modal' + i).on('show.bs.modal', function () {
    modal = i;
    alive = 1;
  });
}

function hide_event_i_fixed(i) {
  $('#modal' + i).on('hide.bs.modal', function () {
    alive = 0;
  });
}

/*
 * Positive modulo function (user defined)
 */

function mod(n, m) {
        return ((n % m) + m) % m;
}