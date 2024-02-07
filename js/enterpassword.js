function checkPassword(){
    var Password = document.getElementById("passwordInput").value;
    if (Password === "digifab"){
        window.location.href = "./digi_fab/index.html"
    } else if (Password === "de12"){
        window.location.href = "./de12/index.html"
    } else if (Password === "diary"){
        window.location.href = "./diary/index.html"
    } else if (Passwprd = "pokedex"){
        window.location.href = "https://xatsukix.github.io/Pokedex/suito/index-list.html"
    } else{
        alert("No exist password")
    }
}