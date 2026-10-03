
async function loadDashboard(){
  const stats = await (await fetch("/api/dashboard/stats")).json();
  document.getElementById("statsCards").innerHTML = `
    <div class="card"><div class="small">Assessments</div><div class="stat">${stats.total}</div></div>
    <div class="card"><div class="small">Average Risk</div><div class="stat">${stats.avg_score}/100</div></div>
    <div class="card"><div class="small">High/Critical</div><div class="stat">${(stats.distribution.HIGH||0)+(stats.distribution.CRITICAL||0)}</div></div>
    <div class="card"><div class="small">Privacy Model</div><div class="stat">10 cats</div></div>`;
  const levels = ["LOW","MODERATE","HIGH","CRITICAL"];
  document.getElementById("distribution").innerHTML = levels.map(l => {
    const n=stats.distribution[l]||0, max=Math.max(1,...levels.map(x=>stats.distribution[x]||0));
    return `<div class="bar"><div class="bar-label"><span>${l}</span><b>${n}</b></div>
    <div class="bar-track"><div class="bar-fill" style="width:${n/max*100}%"></div></div></div>`;
  }).join("");
  document.getElementById("recent").innerHTML = stats.recent.length ?
    stats.recent.map(r=>`<p><b>${r.assessment_id}</b> — ${Math.round(r.overall_score)}/100 — ${r.risk_level} — ${new Date(r.created_at).toLocaleString()}</p>`).join("")
    : "<p>No assessments yet.</p>";
  const checklist = await (await fetch("/api/privacy-checklist")).json();
  document.getElementById("checklist").innerHTML = checklist.checklist.map(x=>`<div class="check">☐ ${x}</div>`).join("");
}
loadDashboard();
