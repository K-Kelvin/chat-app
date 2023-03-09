function checkProfanity(text) {
    const encodedParams = new URLSearchParams();
    encodedParams.append("content", text);
    encodedParams.append("censor-character", "*");

    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/x-www-form-urlencoded',
            'X-RapidAPI-Key': '50165337b5msh2a6235f7d2415d8p1604d2jsn59a69a110664',
            'X-RapidAPI-Host': 'neutrinoapi-bad-word-filter.p.rapidapi.com'
        },
        body: encodedParams
    };

    return new Promise((resolve, reject) => {
        fetch('https://neutrinoapi-bad-word-filter.p.rapidapi.com/bad-word-filter', options)
        .then(response => response.json())
        .then(response => resolve(response))
        .catch(err => reject(err));
    })
}