$("#slideshow > div:gt(0)").hide();

setInterval(function() {
  $('#slideshow > div:first')
    .fadeOut(1000)
    .next()
    .fadeIn(1000)
    .end()
    .appendTo('#slideshow');
}, 3000);


$('tr').hide().filter(function () {
    return $(this).find('td[colspan]').length;
}).addClass('header2').css('display', 'table-row').click(function () {
    $(this).nextUntil('tr.header2').css('display', function (i, v) {
        return this.style.display === 'table-row' ? 'none' : 'table-row';
    });
});

function addToMovieChoices(choice) {
  if(document.getElementById('choice1') === 'choose a movie') {
    document.getElementById('choice1') = choice;
  } elseif(document.getElementById('choice2') === 'choose a movie') {
    document.getElementById('choice2') = choice;
  } else {
    console.log("You've already made your two choices. Move on or deselect one.");
  }
}


document.getElementById("slide1").addEventListener("click", addToMovieChoices(document.getElementById('slide1')));
document.getElementById("slide2").addEventListener("click", addToMovieChoices(document.getElementById('slide2'));
document.getElementById("slide3").addEventListener("click", addToMovieChoices(document.getElementById('slide3'));
document.getElementById("slide4").addEventListener("click", addToMovieChoices(document.getElementById('slide4'));
document.getElementById("slide5").addEventListener("click", addToMovieChoices(document.getElementById('slide5'));
