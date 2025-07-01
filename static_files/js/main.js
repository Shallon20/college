const topBar = document.getElementById("top-bar");
let lastScroll = 0;

window.addEventListener("scroll", () => {
    const currentScroll = window.scrollY;

    if (currentScroll > lastScroll && currentScroll > 50) {
        topBar.classList.add("hidden");
    } else {
        topBar.classList.remove("hidden");
    }

    lastScroll = currentScroll;
});
