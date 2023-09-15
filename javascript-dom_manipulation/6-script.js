function handleResponse(response) {
    if (!response.ok) {
      console.log("network response was not ok");
    } else {
      return response.json();
    }
  }
  
  function updateCharacterName(respose_data) {
    document.querySelector("#character").textContent = respose_data.name;
  }
  
  function handleError(error) {
    console.log(error);
  }
  
  const promise = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
  promise.then(handleResponse).then(updateCharacterName).catch(handleError);