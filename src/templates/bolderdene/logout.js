function logout() {
  fetch("http://whoism.mandakh.org/api/addCv/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // 'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({
      action: "logout_cv",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.resultCode === 200) {
        // Clear local storage if you stored pid or other user info
        console.log(data.data[0].success);
        localStorage.removeItem("pid");
        window.location.href = "../bolderdene/logout.html"; // Redirect to the login page or home page
      } else {
        alert("Амжилтгүй");
      }
    })
    .catch((error) => console.error("Сэрвисийн алдаа:", error));
}
