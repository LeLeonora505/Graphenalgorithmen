// access html elements from withing JS
let htmlElement = document.getElementById("idOfMyHtmlElement");
 
// function that interacts with flask server app
async function interactWithServer(word){
    // send post request to server
    let response = await fetch('/interactWithServer', {
        method: 'POST', // because want to send data to server s.t. it can process it
        headers: { // tells server that request body contains json data
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"name":"John", "age":41}) // data sent to server
    });
 
    // write response status (hopefully not 404!) into console
    console.log(response.status); 
 
    // wait for server's response, then access data sent back
    let json_data = await response.json();
 
    // now do something with data
    htmlElement.innerHTML = json_data.nameOfKey;
}
 
// function that is executed on even
function somethingHasHappened(event){
    // call function that interacts with server
    interactWithServer(inpPlainText.value);
}
 
// add event listeners (clicking button, typing something into input box, ...)
htmlElement.addEventListener('input',somethingHasHappened)