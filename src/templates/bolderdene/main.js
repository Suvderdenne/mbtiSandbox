fetch("example.json")
  .then((response) => response.json())
  .then((data) => {
    document.getElementById("lastname").innerText =
      data.data[0].personal_details.lastname;
    document.getElementById("address").innerText +=
      data.data[0].personal_details.address;

    if ("experience" in data.data[0]) {
      const experienceList = document.getElementById("experience");
      experienceList.innerHTML = "Experience";
      data.data[0].experience.forEach((exp) => {
        const li = document.createElement("li");

        li.innerHTML = ` ${exp.company} <ul>${exp.responsibilities
          .map((res) => `<li>${res}</li>`)
          .join("")}</ul>`;
        experienceList.appendChild(li);
      });
    } else {
      document.getElementById("experience").style.display = "none";
    }

    if ("education" in data.data[0]) {
      const educationList = document.getElementById("education");
      educationList.innerHTML = "Education";
      data.data[0].education.forEach((exp) => {
        const li = document.createElement("li");

        li.innerHTML = ` ${exp.institution}, ${exp.start_year} `;
        educationList.appendChild(li);
      });
    } else {
      document.getElementById("education").style.display = "none";
    }
  })
  .catch((error) => console.error("Error fetching data:", error));
