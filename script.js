// Skills Section Animation
document.getElementById("skills").addEventListener("click", function () {
    let skillsList = document.querySelector(".skill-list");
    if (skillsList.style.display === "none" || skillsList.style.display === "") {
        skillsList.style.display = "block";
    } else {
        skillsList.style.display = "none";
    }
});

// Contact Section Animation
document.getElementById("contact").addEventListener("mouseover", function () {
    document.querySelector(".contact-info").style.display = "block";
});

document.getElementById("contact").addEventListener("mouseleave", function () {
    document.querySelector(".contact-info").style.display = "none";
});

// Smooth Scrolling Effect Like Gaming UI
document.addEventListener("scroll", function () {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    document.body.style.backgroundPositionY = -scrollTop * 0.3 + "px";
});
