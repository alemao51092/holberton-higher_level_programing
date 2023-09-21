const $ = window.$;
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const results = data.results;

    $.each(results, function (index, result) {
      $('#list_movies').append('<li>' + result.title + '</li>');
    });
  });
});