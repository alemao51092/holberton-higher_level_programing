function handleResponse(response) {
    if (!response.ok) {
      console.log("network response was not ok");
    } else {
      return response.json();
    }
  }
  
  function appendTitle(response_data) {
    const listMovies = document.querySelector("#list_movies");
    let movies = response_data.results;
  
    movies.forEach((movie) => {
      let item = document.createElement("li");
      item.textContent = movie.title;
  
      listMovies.appendChild(item);
    });
  }
  function handleError(error) {
    console.log(error);
  }
  
  const promise = fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  promise.then(handleResponse).then(appendTitle).catch(handleError);