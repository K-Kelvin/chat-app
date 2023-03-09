let badWords = [];

async function populateBadWords() {
    try {
        const response = await fetch(
            "https://docs.google.com/spreadsheets/d/1hIEi2YG3ydav1E06Bzf2mQbGZ12kh2fe4ISgLg_UBuM/export?format=csv"
        );
        // const data = await response.json()
        console.log(response)
        // const lines = data.split("\n");
        // badWords = lines.map((line) => line.split(",")[0]);
        // console.log(badWords)
        // return badWords;
    } catch (error) {
        console.error(error);
    }
}
populateBadWords();

function cussWordFound(input) {
    if (!input) {
        return false;
    }

    let input = input
        .replace(/1/g, "i")
        .replace(/!/g, "i")
        .replace(/3/g, "e")
        .replace(/4/g, "a")
        .replace(/@/g, "a")
        .replace(/5/g, "s")
        .replace(/7/g, "t")
        .replace(/0/g, "o")
        .replace(/9/g, "g");

    const inputWords = input.toLowerCase().split(/[^a-zA-Z]/g);
    for (const inputWord of inputWords) {
        if (badWords.includes(inputWord)) {
            foundProfanity = true;
            console.log(`${inputWord} is a bad word`);
            alert(`Use of words like ${input} is not allowed on this platform!`)
            return true;
        }
    }
    foundProfanity = false;
    console.log("Clean message.........")
    return false;
}