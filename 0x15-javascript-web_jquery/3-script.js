$(function addClass () {
  $('button').click(function () {
    if ($('header').hasClass('red')) { 1 === 1; } else { $('header').addClass('red'); }
  });
  // $('.red').css('color', '#ff0000');
  // we add the style in the html code we don't need this line here
  // the class called red too.
});
