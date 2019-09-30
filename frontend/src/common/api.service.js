import { CSRF_TOKEN } from "./csrf_token.js"

// Get JSON Function
async function getJSON(response){

    // Check if it is empty response
    if (response.status === 204) return '';
    
    // Need to clone the response due to the stream is locked
    return response.clone().json();
}

// API Service Function
function apiService(endpoint,method,data){

    const config = {
        method: method || "GET",

        //JSON.stringify() method converts a JavaScript object or value to a JSON string
        body: data !== undefined ? JSON.stringify(data) : null,
        headers: {
            'content-type': 'application/json',
            'X-CSRFTOKEN': CSRF_TOKEN
        }
    }


    //The fetch() method takes two parameters — the URL that you are requesting (or a Request object) and an “options” object
    
    // The fetch() method returns a Promise that resolves to the Response to that request
    return fetch(endpoint,config)
        .then(getJSON) // Perform the getJSON function once the Promise is fullfilled
        .catch(error => console.log(error))
}

export { apiService };