/*
PRAVIDLA HRY:

- Hra má dva hráče, kteří se střídají každé kolo
- V každé kole hází hráč kostkou kolikrát chce. Hodnota každého hodu se přičítá k jeho bodů v daném kole.
- Pokud na kostce padne 1, ztrácí všechny body v daném kole a na řadu se dostává hráč dvě.
- Hráč může zvolit "dost", což znamená, že všechny body nahrané v jeho kole se přičtou k jeho celkovým bodům. Poté je na řadě hráč dvě.
- Hra končí jakmile jeden z hráčů dosáhne dopředu určeného počtu bodů (typicky 100 bodů).

*/


// deklarace konstant a proměnných
const bodyKVyhre = 100;
let body;
let bodyVKole;
let aktivniHrac;
let hraProbiha;
let kostka = {
    hodnota: 0,
    hod: function() {
        this.hodnota = Math.floor(Math.random() * 6) + 1;
    }
}

// přístup k prvkům DOM
const kostkaDOM = document.querySelector('.kostka');

function bodyDOM(hrac) {
    return document.getElementById("body-" + hrac);
}

function bodyVKoleDOM(hrac) {
    return document.getElementById("soucasne-" + hrac);
}

function toggleHracPanelDOM_aktivni() {
    for (let hrac = 0; hrac <= 1; hrac++) {
        document.querySelector(`.hrac-${hrac}-panel`).classList.toggle("aktivni");
    }
}

function hracPanelDOM_reset() {
    document.querySelector(".hrac-0-panel").classList.add("aktivni");
    document.querySelector(".hrac-1-panel").classList.remove("aktivni");
    for (let i = 0; i <= 1; i++) {
        document.querySelector(`.hrac-${i}-panel`).classList.remove("vitez");
        document.getElementById(`jmeno-${i}`).textContent = `Hráč ${i+1}`;
    }
}


// funkce
function novaHra() {
    body = [0, 0];
    bodyVKole = 0;
    aktivniHrac = 0;
    kostka.hodnota = 0;

    bodyDOM(0).textContent = "0";
    bodyDOM(1).textContent = "0";
    bodyVKoleDOM(0).textContent = "0";
    bodyVKoleDOM(1).textContent = "0";

    hracPanelDOM_reset();
    kostkaDOM.style.display = "none";
 
    hraProbiha = true;
}


function prepniHrace() {
    body[aktivniHrac] += bodyVKole;
    bodyDOM(aktivniHrac).textContent = body[aktivniHrac];
    bodyVKole = 0;

    if (body[aktivniHrac] < bodyKVyhre) {
        kostkaDOM.textContent = "0";
        if (aktivniHrac == 0) { aktivniHrac = 1 }
        else { aktivniHrac = 0 }
        bodyVKoleDOM(aktivniHrac).textContent = "0";
        toggleHracPanelDOM_aktivni();
    } else {
        hraProbiha = false;
        document.getElementById("jmeno-" + aktivniHrac).textContent = "Vítěz!";
        document.querySelector(`.hrac-${aktivniHrac}-panel`).classList.remove("aktivni");
        document.querySelector(`.hrac-${aktivniHrac}-panel`).classList.add("vitez");
    }
}


// události
document.querySelector(".tlacitko-novy").addEventListener("click", novaHra);


document.querySelector(".tlacitko-hod").addEventListener("click", function() {    
    if (hraProbiha) {
        // 1. Náhodné číslo
        kostka.hod();
        
        // 2. Zobrazit výsledek
        kostkaDOM.textContent = kostka.hodnota;
        kostkaDOM.style.display = "block";
        
        // 3. Aktualizovat body kola, pokud (ne-)/padla 1
        if (kostka.hodnota != 1) {
            bodyVKole += kostka.hodnota;
            bodyVKoleDOM(aktivniHrac).textContent = bodyVKole;
        }
        else {
            bodyVKoleDOM(aktivniHrac).textContent = "0";
            bodyVKole = 0;
            prepniHrace();
        }
    }
});


document.querySelector(".tlacitko-dost").addEventListener("click", function() {
    if (hraProbiha) prepniHrace();
});


novaHra();
