document.addEventListener("DOMContentLoaded", () => {
  const loginModal = document.getElementById("loginModal");
  const registerModal = document.getElementById("registerModal");

  const loginOverlay = document.getElementById("loginOverlay");
  const registerOverlay = document.getElementById("registerOverlay");

  const openLoginBtn = document.getElementById("openLogin");
  const closeLoginBtn = document.getElementById("closeLogin");

  const openRegisterFromLogin = document.getElementById("openRegisterFromLogin");
  const openLoginFromRegister = document.getElementById("openLoginFromRegister");
  const closeRegisterBtn = document.getElementById("closeRegister");

  /* ================= HELPERS ================= */

  function openModal(modal, overlay) {
    modal.classList.add("active");
    overlay.classList.add("active");
  }

  function closeModal(modal, overlay) {
    modal.classList.remove("active");
    overlay.classList.remove("active");
  }

  function closeAll() {
    [loginModal, registerModal].forEach(m => m.classList.remove("active"));
    [loginOverlay, registerOverlay].forEach(o => o.classList.remove("active"));
  }

  /* ================= LOGIN ================= */

  if (openLoginBtn) {
    openLoginBtn.addEventListener("click", () => {
      closeAll();
      openModal(loginModal, loginOverlay);
    });
  }

  if (closeLoginBtn) {
    closeLoginBtn.addEventListener("click", () => {
      closeModal(loginModal, loginOverlay);
    });
  }

  loginOverlay.addEventListener("click", () => {
    closeModal(loginModal, loginOverlay);
  });

  /* ================= REGISTRO ================= */

  if (openRegisterFromLogin) {
    openRegisterFromLogin.addEventListener("click", () => {
      closeAll();
      openModal(registerModal, registerOverlay);
    });
  }

  if (openLoginFromRegister) {
    openLoginFromRegister.addEventListener("click", () => {
      closeAll();
      openModal(loginModal, loginOverlay);
    });
  }

  if (closeRegisterBtn) {
    closeRegisterBtn.addEventListener("click", () => {
      closeModal(registerModal, registerOverlay);
    });
  }

  registerOverlay.addEventListener("click", () => {
    closeModal(registerModal, registerOverlay);
  });

  /* ================= OLVIDÉ CONTRASEÑA ================= */

  const forgotPasswordLink = document.querySelector(".modal-footer .link");

  if (forgotPasswordLink) {
    forgotPasswordLink.addEventListener("click", (e) => {
      e.preventDefault();
      alert("Funcionalidad de recuperación de contraseña pendiente");
      // aquí luego conectamos con Django PasswordResetView
    });
  }
});
