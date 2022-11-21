const http = new EasyHTTP;

function getHighscore(){
    http.get("http://127.0.0.1:5000/highscoreList")
    .then(data => document.getElementById("first").innerHTML = `<div>${data[0]} <br> ${data[1]} <br> ${data[2]}</div>`)                
    .catch(err => console.log(err));

    //document.getElementById("highscoreBoard").innerHTML = "hello";
}

function insertHighscore(name, score){
    const data = {
        username : name,
        highscore : score
    }
    http.post("http://127.0.0.1:5000/highscoreList", data)
    .then(data => console.log(data))
    .catch(err => console.log(err));
}