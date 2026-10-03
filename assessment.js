
let questions = [];
let lastAnswers = null;

const form = document.getElementById("assessmentForm");
const result = document.getElementById("result");
const errorBox = document.getElementById("error");

async function loadQuestions(){
  const res = await fetch("/api/questions");
  const data = await res.json();
  questions = data.questions;
  let current = "";
  questions.forEach((q, i) => {
    if(q.category !== current){
      current = q.category;
      const heading = document.createElement("div");
      heading.className = "card";
      heading.innerHTML = `<h2>${current}</h2>`;
      form.appendChild(heading);
    }
    const box = document.createElement("div");
    box.className = "question";
    box.innerHTML = `<h3>${i+1}. ${q.text}</h3>
      <div class="options">${q.options.map(v => `<label class="option">
      <input required type="radio" name="${q.id}" value="${v}"> ${v.replaceAll("_"," ")}</label>`).join("")}</div>`;
    form.appendChild(box);
  });
}

function riskClass(level){ return "risk-" + level.toLowerCase(); }

function renderResult(data){
  result.classList.remove("hidden");
  const cats = Object.entries(data.category_scores).map(([k,v]) =>
    `<div class="bar"><div class="bar-label"><span>${k}</span><b>${Math.round(v)}</b></div>
     <div class="bar-track"><div class="bar-fill" style="width:${Math.min(100,v)}%"></div></div></div>`).join("");
  const findings = data.findings.slice(0,10).map(f =>
    `<div class="finding"><b>${f.severity} — ${f.category}</b><br>${f.description}<br><span class="small">Fix: ${f.fix}</span></div>`).join("") || "<p>No major findings.</p>";
  const recs = data.recommendations.slice(0,10).map(r =>
    `<div class="rec"><b>${r.priority} — ${r.category}</b><br>${r.recommendation}</div>`).join("");
  result.innerHTML = `<div class="card"><span class="badge">ASSESSMENT ${data.assessment_id}</span>
    <div class="score ${riskClass(data.risk_level)}">${Math.round(data.overall_score)}/100</div>
    <h2 class="${riskClass(data.risk_level)}">${data.risk_level}</h2>
    <div class="meter"><div style="width:${data.overall_score}%"></div></div>
    <p>Higher score means higher assessed exposure/risk. This is an educational framework simulation.</p>
    <div class="actions"><a class="btn primary" target="_blank" href="/api/report/${data.assessment_id}/html">Open HTML Report</a>
    <a class="btn" href="/api/report/${data.assessment_id}/pdf">Download PDF Report</a>
    <a class="btn" href="/dashboard">Dashboard</a></div></div>
    <div class="result-grid"><div class="card"><h2>Category Scores</h2>${cats}</div>
    <div><div class="card"><h2>Top Findings</h2>${findings}</div><div class="card"><h2>Recommendations</h2>${recs}</div></div></div>
    <div class="card"><h2>Improvement Simulator</h2><p>Simulate safe improvements without changing your stored assessment.</p>
    <button class="btn primary" onclick="runSimulation()">Simulate Recommended Improvements</button><div id="simulation"></div></div>`;
  window.scrollTo({top: result.offsetTop - 20, behavior:"smooth"});
}

document.getElementById("submitBtn").addEventListener("click", async (e)=>{
  e.preventDefault();
  errorBox.textContent = "";
  if(!form.reportValidity()){ errorBox.textContent = "Please answer every question."; return; }
  const answers = {};
  questions.forEach(q => answers[q.id] = document.querySelector(`input[name="${q.id}"]:checked`).value);
  lastAnswers = answers;
  const res = await fetch("/api/assessment",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({answers})});
  const data = await res.json();
  if(!res.ok){ errorBox.textContent = data.details?.join(", ") || data.error || "Assessment failed."; return; }
  renderResult(data);
});

async function runSimulation(){
  const changes = {
    phone_public:"NO", email_public:"NO", birthday_public:"NO", location_public:"NO",
    realtime_location:"NO", travel_posts:"NO", geotagging:"NO", tag_review:"NO",
    unknown_mentions:"NO", mfa_enabled:"YES", unique_password:"YES",
    login_alerts:"YES", sessions_reviewed:"YES", third_party_reviewed:"YES",
    unused_apps:"NO", broad_app_permissions:"NO", privacy_reviewed:"YES",
    old_public_posts:"NO", old_comments:"YES", photo_metadata:"NO",
    unknown_connections:"RARELY"
  };
  const res = await fetch("/api/assessment/simulate-improvement",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({answers:lastAnswers,changes})});
  const data = await res.json();
  document.getElementById("simulation").innerHTML =
    `<div class="card"><h3>Before: ${Math.round(data.original.overall_score)}/100 — ${data.original.risk_level}</h3>
     <h3>After simulation: ${Math.round(data.simulated.overall_score)}/100 — ${data.simulated.risk_level}</h3>
     <p><b>Simulated risk reduction: ${Math.round(data.risk_reduction)} points</b></p>
     <p class="small">Simulation only. It is not a guarantee of real-world safety.</p></div>`;
}
loadQuestions();
