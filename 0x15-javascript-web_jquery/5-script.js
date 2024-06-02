$(function addItem () {
  $('button').click(function () {
    // $('.my_list').html('<li><i>Item</i></li>')
    // if item exist it doesn't add anther one
    $('.my_list').append('<li><i>Item</i></li>');
  });
});
