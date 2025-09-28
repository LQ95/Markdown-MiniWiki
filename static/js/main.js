const md = window.markdownit();

markdownContent = document.getElementById("content");

markdownEditWindowContent = document.getElementById("edit-content");
if (markdownContent) {
  markdownContent.innerHTML = md.render(markdownContent.textContent);
}

/**
 * to be reviewed for future usage
 function renderMarkdown(markdown, target, options = {}) {
  const el =
    typeof target === "string" ? document.querySelector(target) : target;
  if (!el) {
    console.error("renderMarkdown: target non trovato");
    return;
  }

  // Inizializza markdown-it una sola volta
  const md =
    window._md ||
    (window._md = window.markdownit({
      html: false, // più sicuro
      linkify: true, // auto-link di URL
      breaks: true, // \n -> <br>
      typographer: true,
      ...(options.markdownIt || {}),
    }));

  const dirtyHtml = md.render(markdown || "");
  const cleanHtml = DOMPurify.sanitize(
    dirtyHtml,
    options.sanitize || { USE_PROFILES: { html: true } }
  );

  el.innerHTML = cleanHtml;

  // (Opzionale) Apri i link esterni in nuova scheda
  el.querySelectorAll("a[href]").forEach((a) => {
    const href = a.getAttribute("href") || "";
    if (
      !href.startsWith("#") &&
      !href.startsWith("mailto:") &&
      !href.startsWith("tel:")
    ) {
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
    }
  });
}
**/
