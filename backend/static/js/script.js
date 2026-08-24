// ============================================================
// AuthFlow — Google Sign-In
// ------------------------------------------------------------
// Redirects the browser to Django's OAuth entry point, which
// starts the real Google login flow. Django owns all OAuth
// logic, tokens, and secrets — this file only triggers the
// navigation.
// ============================================================

function continueWithGoogle() {
  window.location.href = "/auth/google/login/";
}

/**
 * Displays a temporary status message below the Google button.
 * Not used by continueWithGoogle() anymore, but kept here in
 * case you want to show status messages elsewhere later.
 */
function showStatusMessage(text) {
  let statusEl = document.getElementById("statusMessage");

  if (!statusEl) {
    statusEl = document.createElement("p");
    statusEl.id = "statusMessage";
    statusEl.className = "status-message";

    const card = document.querySelector(".auth-card");
    const footnote = document.querySelector(".footnote");
    card.insertBefore(statusEl, footnote);
  }

  statusEl.textContent = text;
  statusEl.classList.add("visible");

  // Auto-hide after a few seconds
  clearTimeout(showStatusMessage._timer);
  showStatusMessage._timer = setTimeout(() => {
    statusEl.classList.remove("visible");
  }, 4000);
}

// ============================================================
// Event Bindings
// ============================================================
document.addEventListener("DOMContentLoaded", () => {
  const googleBtn = document.getElementById("googleBtn");

  if (googleBtn) {
    googleBtn.addEventListener("click", continueWithGoogle);
  }
});