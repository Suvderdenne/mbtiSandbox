fetch("http://whoism.mandakh.org/whois/",{
  method:"POST",
  headers:{
    "Content-Type":"application/json"
  },
  body: JSON.stringify({
    action:"example", pid:1
  })
})
  .then((response) => response.json())
  .then((data) => {
    document.getElementById("firstname").innerText = data.data[0]['personal_details']['firstname'];
    document.getElementById("lastname").innerText = data.data[0].personal_details.lastname;
    document.getElementById("mergjil").innerText = data.data[0].personal_details.headline;
    document.getElementById("hayg").innerText = data.data[0].personal_details.address;
    document.getElementById("dugar").innerText = data.data[0].personal_details.phone;
    document.getElementById("name").innerText = `2024 ${data.data[0].personal_details.name}`
    
    const experienceList = document.getElementById("experienceList");
      if ("experience" in data) {
        data.data[0].experience.forEach((exp) => {
          const li = document.createElement("li");
          li.innerHTML = `<strong>${exp.job_title}</strong> at ${exp.company}, ${exp.start_date} - ${exp.end_date}<ul>${exp.responsibilities.map(res => `<li>${res}</li>`).join('')}</ul>`;
          experienceList.appendChild(li);
        });
      } 
      else {
        document.getElementById("experience").style.display = 'none';
      }

    const educationList = document.getElementById("educationList");
    if ("education" in data){
        data.data[0].education.forEach((edu) => {
          const li = document.createElement("li");
          li.innerHTML = `<strong>${edu.degree}</strong> at ${edu.institution}, ${edu.graduation_year}. I started studying in ${edu.institution} located ${edu.location} in ${edu.start_year}`;
          educationList.appendChild(li);
        });
    }
    else{
      document.getElementById("education").style.display = "none"
    }

    const skillsList = document.getElementById("skillsList");
    if("skills" in data){
    data.data[0].skills.forEach((skills) => {
      const li = document.createElement("li");
      li.innerText = `${skills.skill} : ${skills.proficiency};`
      skillsList.appendChild(li);
    });
  } 
  else{
    document.getElementById("skills").style.display = "none"
  }
    const cerList = document.getElementById("cerList")
    if("certifications" in data){
    data.data[0].certifications.forEach((cers) =>{
      const li = document.createElement("li");
      li.innerHTML = `I received <strong>${cers.name}</strong> from <strong>${cers.institution}</strong> in ${cers.year}`
      cerList.appendChild(li);
    });
  } 
  else{
    document.getElementById("certification").style.display = "none"
  }

    const porList = document.getElementById("Porlist");
    if("projects" in data){
    data.data[0].projects.forEach((pors) => {
      const li = document.createElement("li");
      li.innerHTML = `I worked on <strong>${pors.name}</strong>. ${pors.description} You can see it at <a href="${pors.url}" target="_blank"><strong>${pors.url}</strong></a>`;
      porList.appendChild(li);
    });
  } 
  else{
    document.getElementById("projects").style.display = "none"
  }

    const lanList = document.getElementById("lanList");
    if("languages" in data){
    data.data[0].languages.forEach((lans)=>{
      const li = document.createElement("li")
      li.innerHTML = `${lans.language} : ${lans.proficiency}`
      lanList.appendChild(li);
    });
  } else{
    document.getElementById("languages").style.display = "none"
  }

    const hobList = document.getElementById("hobList");
    if("hobbies" in data){

    data.data[0].hobbies.forEach((hobs) =>{
      const li = document.createElement("li")
      li.innerText = `${hobs}`
      hobList.appendChild(li)
    });
  } else {
    document.getElementById("hobbies").style.display = "none"
  }
  })
  .catch((error) => console.error("Error fetching data:", error));
  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("downloadButton").addEventListener("click", function () {
        var element = document.body;

        html2pdf().from(element).set({
            margin: 1,
            filename: 'resume.pdf',
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
        }).save();
    });
});
