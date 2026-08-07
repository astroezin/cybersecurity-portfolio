/*
    SIEM Alert Dashboard
    dashboard.js
*/

document.addEventListener("DOMContentLoaded", function () {

    console.log("SIEM Alert Dashboard Loaded");

    const table = document.querySelector("table");

    if (!table) {
        return;
    }

    const container = table.parentElement;

    const search = document.createElement("input");

    search.type = "text";
    search.className = "form-control mb-3";
    search.placeholder = "Search alerts...";

    container.insertBefore(search, table);

    search.addEventListener("keyup", function () {

        const value = search.value.toLowerCase();

        const rows = table.querySelectorAll("tbody tr");

        rows.forEach(function (row) {

            const text = row.textContent.toLowerCase();

            if (text.includes(value)) {

                row.style.display = "";

            } else {

                row.style.display = "none";

            }

        });

    });

    const badges = document.querySelectorAll(".badge");

    badges.forEach(function (badge) {

        badge.style.cursor = "default";

    });

    const cards = document.querySelectorAll(".card");

    cards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {

            card.style.transform = "translateY(-2px)";
            card.style.transition = "0.2s";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform = "translateY(0px)";

        });

    });

});
