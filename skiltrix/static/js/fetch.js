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

// function sendCompany(event, url) {

//     event.preventDefault();
//     const company = document.getElementById("company").value;
//     const name = document.getElementById('name').value;

//     console.log(company);

//     fetch(url, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": document.querySelector(
//                 "[name=csrfmiddlewaretoken]"
//             ).value
//         },
//         body: JSON.stringify({
//             company: company,
//             name: name,
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch(error => {
//         console.error("Fetch error:", error);
//     });
// }


function sendCompany(event, url) {

    event.preventDefault();

    const form = event.target;

    // Validate required fields
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    const company = document.getElementById("company").value;
    const name = document.getElementById("name").value;
    const type = document.getElementById("type").value;
    const paid = document.getElementById("paid").value;
    const price = document.getElementById("price").value;
    const location = document.getElementById("location").value;
    const applyLink = document.getElementById("apply_link").value;
    const date = document.getElementById("date").value;

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
            type: type,
            paid: paid,
            price: paid === "1" ? price : 0,
            location: location,
            apply_link: applyLink,
            date: date
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


function toggleInternshipPrice() {

    const paid = document.getElementById("paid").value;

    const priceLabelRow =
        document.getElementById("priceLabelRow");

    const priceInputRow =
        document.getElementById("priceInputRow");

    const price =
        document.getElementById("price");

    if (paid === "1") {

        // Paid
        priceLabelRow.style.display = "table-row";
        priceInputRow.style.display = "table-row";

        price.required = true;

    } else {

        // Free
        priceLabelRow.style.display = "none";
        priceInputRow.style.display = "none";

        price.required = false;
        price.value = "";
    }
}


function uploadCompany(event, url) {
    event.preventDefault();

    const form = event.target;

    // Validate required fields
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    const form_ = document.getElementById("form");

    const formData = new FormData(form);

    const progressContainer = document.getElementById("progressContainer");
    const progressBar = document.getElementById("progressBar");
    const progressText = document.getElementById("progressText");
    const status = document.getElementById("status");

    // Show progress
    progressContainer.style.display = "block";
    progressBar.value = 0;
    progressText.textContent = "0%";
    status.textContent = "Uploading...";

    const xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    // Django CSRF
    xhr.setRequestHeader(
        "X-CSRFToken",
        document.querySelector("[name=csrfmiddlewaretoken]").value
    );

    // Upload progress
    xhr.upload.addEventListener("progress", function(event) {

        if (event.lengthComputable) {

            const percent = Math.round(
                (event.loaded / event.total) * 100
            );

            progressBar.value = percent;
            progressText.textContent = percent + "%";
        }
    });

    // Upload completed
    xhr.onload = function() {

        console.log("HTTP Status:", xhr.status);
        console.log("Response:", xhr.responseText);

        if (xhr.status >= 200 && xhr.status < 300) {

            try {

                const data = JSON.parse(xhr.responseText);

                console.log(data);

                if (data.status) {

                    progressBar.value = 100;
                    progressText.textContent = "100%";
                    status.textContent = "Company added successfully.";

                    // Optional: reset form
                    form.reset();

                    form_.setAttribute("class", "form");
                    // Hide image preview
                    const preview =
                        document.getElementById("imagePreview");

                    preview.src = "";
                    preview.style.display = "none";

                      

                } else {

                    status.textContent =
                        data.message || "Failed to add company.";
                }

            } catch (error) {

                console.error("JSON error:", error);

                status.textContent =
                    "Invalid server response.";
            }

        } else {

            status.textContent =
                "Upload failed.";

            console.error(
                "Server error:",
                xhr.status,
                xhr.responseText
            );
        }
    };

    // Network error
    xhr.onerror = function() {

        console.error("Upload error");

        status.textContent =
            "Network error while uploading.";
    };

    for (const [key, value] of formData.entries()) {
    console.log(key, value);
}
    // Start upload
    xhr.send(formData);
}

function uploadImage(event, url) {
    event.preventDefault();

    const form = event.target;

    // Check required fields
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    const form_ = document.getElementById("form");

    const formData = new FormData(form);

    const video = document.getElementById("video");
    const image = document.getElementById("image");

    if (!video.files.length) {
        alert("Please select a video");
        return;
    }

    if (!image.files.length) {
        alert("Please select an image");
        return;
    }

    const progressContainer =
        document.getElementById("progressContainer");

    const progressBar =
        document.getElementById("progressBar");

    const progressText =
        document.getElementById("progressText");

    const status =
        document.getElementById("status");

    // Show progress
    progressContainer.style.display = "block";
    progressBar.value = 0;
    progressText.textContent = "0%";
    status.textContent = "Uploading...";

    const xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    // Django CSRF
    xhr.setRequestHeader(
        "X-CSRFToken",
        document.querySelector(
            "[name=csrfmiddlewaretoken]"
        ).value
    );

    // Upload progress
    xhr.upload.addEventListener("progress", function (event) {

        if (event.lengthComputable) {

            const percent = Math.round(
                (event.loaded / event.total) * 100
            );

            progressBar.value = percent;
            progressText.textContent = percent + "%";

            console.log(
                "Uploaded:",
                event.loaded,
                "/",
                event.total,
                percent + "%"
            );


        }
    });

    // Request completed
    xhr.onload = function () {

        console.log("Status:", xhr.status);
        console.log("Response:", xhr.responseText);

        if (xhr.status >= 200 && xhr.status < 300) {

            try {

                const data = JSON.parse(xhr.responseText);

                console.log(data);

                if (data.status) {

                    progressBar.value = 100;
                    progressText.textContent = "100%";
                    status.textContent =
                        "Video uploaded successfully!";


                        
                    form_.setAttribute("class", "form");


                } else {

                    status.textContent =
                        data.message || "Upload failed.";
                }

            } catch (error) {

                console.error(
                    "Invalid JSON:",
                    xhr.responseText
                );

                status.textContent =
                    "Invalid server response.";
            }

        } else {

            console.error(
                "Upload failed:",
                xhr.status,
                xhr.responseText
            );

            status.textContent =
                "Upload failed.";
        }
    };

    // Network error
    xhr.onerror = function () {

        console.error("Upload error");

        status.textContent =
            "Network error while uploading.";
    };

    // Start upload
    xhr.send(formData);
}


// function coursesUrl(event, url) {
//     event.preventDefault();

//     const form = event.target;
//     const formData = new FormData(form);

//     const fileInput = document.getElementById("fileInput");
//     const file = fileInput.files[0];

//     if (!file) {
//         alert("Please select a file");
//         return;
//     }

//     fetch(url, {

//         method: "POST",
//         headers: {
//             "X-CSRFToken": document.querySelector(
//                     "[name=csrfmiddlewaretoken]"
//                 ).value
//         },

//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//     })
//     .catch(error => {
//         console.error("Fetch Error: ", error)
//     })
// }


function coursesUrl(event, url) {
    event.preventDefault();

    const form = event.target;

    // Validate required fields
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    const form_ = document.getElementById("form");
    const formData = new FormData(form);

    const fileInput = document.getElementById("image");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file");
        return;
    }

    const progressBar = document.getElementById("progressBar");
    const progressText = document.getElementById("progressText");

    // Reset progress
    progressBar.value = 0;
    progressText.textContent = "0%";

    const xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    // CSRF
    xhr.setRequestHeader(
        "X-CSRFToken",
        document.querySelector("[name=csrfmiddlewaretoken]").value
    );

    // Upload progress
    xhr.upload.addEventListener("progress", function (event) {

        if (event.lengthComputable) {

            const percent = Math.round(
                (event.loaded / event.total) * 100
            );

            progressBar.value = percent;
            progressText.textContent = percent + "%";
        }
    });

    // Request completed
    xhr.onload = function () {

        if (xhr.status >= 200 && xhr.status < 300) {

            try {
                const data = JSON.parse(xhr.responseText);

                console.log(data);

                progressBar.value = 100;
                progressText.textContent = "Upload complete";
                form_.setAttribute("class", "form");

            } catch (error) {
                console.error("Invalid JSON response:", error);
            }

        } else {
            console.error(
                "Upload failed:",
                xhr.status,
                xhr.responseText
            );

            progressText.textContent = "Upload failed";
        }
    };

    // Network error
    xhr.onerror = function () {
        console.error("Fetch Error");

        progressText.textContent = "Upload error";
    };

    // Start upload
    xhr.send(formData);

}


function previewImage(event) {

    const file = event.target.files[0];
    const preview = document.getElementById("imagePreview");

    if (!file) {
        preview.style.display = "none";
        preview.src = "";
        return;
    }

    // Make sure it is an image
    if (!file.type.startsWith("image/")) {
        alert("Please select an image file.");
        event.target.value = "";
        preview.style.display = "none";
        return;
    }

    const reader = new FileReader();

    reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = "block";
    };

    reader.readAsDataURL(file);
}


function togglePrice() {

    const paid = document.getElementById("paid").value;

    const priceRow = document.getElementById("priceRow");
    const priceInputRow = document.getElementById("priceInputRow");
    const price = document.getElementById("price");

    if (paid === "1") {

        // Paid
        priceRow.style.display = "table-row";
        priceInputRow.style.display = "table-row";

        price.required = true;

    } else {

        // Free
        priceRow.style.display = "none";
        priceInputRow.style.display = "none";

        price.required = false;
        price.value = "";
    }
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


