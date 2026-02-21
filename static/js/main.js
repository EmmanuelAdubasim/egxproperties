document.addEventListener("DOMContentLoaded", () => {
  // ===== Gallery click (thumbnails switch main image) =====
  const mainImg = document.querySelector(".gallery-main img");
  const thumbs = document.querySelectorAll(".gallery-thumbs img");

  if (mainImg && thumbs.length > 0) {
    thumbs.forEach((thumb) => {
      thumb.style.cursor = "pointer";

      thumb.addEventListener("click", () => {
        const src = thumb.getAttribute("src");
        if (!src) return;

        mainImg.setAttribute("src", src);

        thumbs.forEach(t => t.classList.remove("active-thumb"));
        thumb.classList.add("active-thumb");
      });
    });

    thumbs[0].classList.add("active-thumb");
  }

  // ===== Share listing (copy link) =====
  const shareBtn = document.getElementById("shareBtn");
  const shareHint = document.getElementById("shareHint");

  if (shareBtn) {
    shareBtn.addEventListener("click", async () => {
      try {
        const url = window.location.href;

        // If browser supports native share (mobile), use it
        if (navigator.share) {
          await navigator.share({ title: document.title, url });
        } else {
          await navigator.clipboard.writeText(url);
          if (shareHint) {
            shareHint.style.display = "block";
            setTimeout(() => (shareHint.style.display = "none"), 1800);
          }
        }
      } catch (err) {
        // fallback copy if clipboard/share fails
        try {
          const url = window.location.href;
          const temp = document.createElement("input");
          temp.value = url;
          document.body.appendChild(temp);
          temp.select();
          document.execCommand("copy");
          document.body.removeChild(temp);
          if (shareHint) {
            shareHint.style.display = "block";
            setTimeout(() => (shareHint.style.display = "none"), 1800);
          }
        } catch (e) {
          alert("Unable to share/copy link on this browser.");
        }
      }
    });
  }
});
