function log_error(log_id, url) {

    const view = document.getElementById('view');
    fetch(url, {

        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({ log_id: log_id })
    }).catch(error => {
        console.error('Error:', error);
    });

}