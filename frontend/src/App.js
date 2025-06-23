import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [skills, setSkills] = useState([]);
  const [jobs, setJobs] = useState([]);

  const handleUpload = async () => {
    if (!file) return alert("Please upload a resume");

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:8000/parse-resume", formData);
    setSkills(res.data.skills);

    const jobRes = await axios.get(`http://localhost:8001/search?skills=${res.data.skills.join(",")}`);
    setJobs(jobRes.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Upload Your Resume</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Search Jobs</button>

      {skills.length > 0 && (
        <>
          <h3>Extracted Skills:</h3>
          <ul>{skills.map((skill) => <li key={skill}>{skill}</li>)}</ul>
        </>
      )}

      {jobs.length > 0 && (
        <>
          <h3>Matching Jobs:</h3>
          <ul>
            {jobs.map((job, index) => (
              <li key={index}>
                <a href={job.url} target="_blank" rel="noreferrer">{job.title} at {job.company_name}</a>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default App;
