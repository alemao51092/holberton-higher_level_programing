function handleResponse(response) {
    if (!response.ok) {
      console.log("network response was not ok");
    } else {
      return response.json();
    }
  }
  
  function translation(response_data) {
    const hello_div = document.querySelector("#hello");
    const para = document.createElement("p");
    para.textContent = response_data.hello;
  
    hello_div.appendChild(para);
  }
  
  function handleError(error) {
    console.log(error);
  }
  
  const promise = fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
  promise.then(handleResponse).then(translation).catch(handleError);