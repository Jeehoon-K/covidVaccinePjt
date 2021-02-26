"use strict"

const pfizerButton = document.getElementById("button1")
const modernaButton = document.getElementById("button2")


function pfizerOn(){
    pfizerButton.style.fontSize = "xx-large" ;
}

function pfizerOut(){
    pfizerButton.style.fontSize = "x-large" ;
}

function modernaOn(){
    modernaButton.style.fontSize = "xx-large" ;
}

function modernaOut(){
    modernaButton.style.fontSize = "x-large" ;
}


pfizerButton.addEventListener("mouseenter",pfizerOn)
pfizerButton.addEventListener("mouseleave",pfizerOut)

modernaButton.addEventListener("mouseenter",modernaOn)
modernaButton.addEventListener("mouseleave",modernaOut)