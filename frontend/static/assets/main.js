const runBtn = document.getElementById("run");
const queryEl = document.getElementById("query");
const resultsEl = document.getElementById("results");

const uploadBtn = document.getElementById("upload_btn");
const fileInput = document.getElementById("file_input");
const docIdInput = document.getElementById("doc_id");
const uploadStatus = document.getElementById("upload_status");

// POST query to backend
runBtn.addEventListener("click", async () => {
  const q = queryEl.value.trim();
  if (!q) return alert("Type a query");
  resultsEl.innerHTML = "Loading...";
  try {
    const res = await fetch("/api/query/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: q, top_k: 5 }),
    });
    const data = await res.json();
    resultsEl.innerHTML = "";
    if (data.results && data.results.length) {
      data.results.forEach(r => {
        const el = document.createElement("div");
        el.className = "p-2 border-b";
        el.innerHTML = `<strong>${r.id}</strong> &middot; score: ${r.score || r.distance || ""} <div>${r.metadata?.text ? r.metadata.text.substring(0, 300) : ""}</div>`;
        resultsEl.appendChild(el);
      });
    } else {
      resultsEl.innerHTML = "No results";
    }
  } catch (err) {
    resultsEl.innerHTML = "Error: " + err.toString();
  }
});

// Upload file and send to backend for ingestion/indexing
uploadBtn.addEventListener("click", async () => {
  const file = fileInput.files && fileInput.files[0];
  const docId = (docIdInput.value || "").trim();
  if (!file) return alert("Choose a PDF or TXT file to upload");
  if (!docId) return alert("Provide a document ID");

  uploadStatus.innerText = "Uploading and indexing... (runs in background)";
  uploadBtn.disabled = true;

  const form = new FormData();
  form.append("doc_id", docId);
  form.append("file", file);

  try {
    const res = await fetch("/api/insert/", {
      method: "POST",
      body: form,
    });
    const data = await res.json();
    if (res.ok) {
      uploadStatus.innerText = `Accepted: ${data.inserted_chunks || 0} chunks (background).`;
    } else {
      uploadStatus.innerText = `Upload failed: ${data.detail || JSON.stringify(data)}`;
    }
  } catch (err) {
    uploadStatus.innerText = "Error: " + err.toString();
  } finally {
    uploadBtn.disabled = false;
    // optional: clear file input
    // fileInput.value = "";
  }
});
