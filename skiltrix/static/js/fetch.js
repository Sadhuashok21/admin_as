function fetchUrl(event, url){
    event.preventDefault();
    const language = document.getElementById('language').value
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector(
                "[name=csrfmiddlewaretoken]"
            ).value
        },

        body: JSON.stringify({
            language: language
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error("Fetch error: ", error);
    });
}

function sendCompany(event, url) {

    event.preventDefault();
    const company = document.getElementById("company").value;
    const name = document.getElementById('name').value;

    console.log(company);

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector(
                "[name=csrfmiddlewaretoken]"
            ).value
        },
        body: JSON.stringify({
            company: company,
            name: name,
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error("Fetch error:", error);
    });
}

function uploadImage(event, url) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch(url, {

        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector(
                    "[name=csrfmiddlewaretoken]"
                ).value
        },

        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error("Fetch Error: ", error)
    })
}


function coursesUrl(event, url) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch(url, {

        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector(
                    "[name=csrfmiddlewaretoken]"
                ).value
        },

        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error("Fetch Error: ", error)
    })
}


function deleteUrl(url, language_id, type) {
    fetch(url, {
        method: 'DELETE',
        headers: {
            "Content-Type": "application/json",
             "X-CSRFToken": document.querySelector(
                "[name=csrfmiddlewaretoken]"
            ).value
        },

        body: JSON.stringify({
            [type]: language_id
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error("Fetch error: ", error);
    })
}



function x_into(){
    const con = document.querySelector('.container');
    const form = document.getElementById("form")

    form.classList.toggle('active')
    con.classList.toggle('active')
}


