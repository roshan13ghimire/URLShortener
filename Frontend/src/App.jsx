import { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const shortenUrl = async () => {
    setLoading(true);
    setShortUrl("");

    try {
      const res = await axios.post("http://127.0.0.1:5000/shorten", {
        long_url: url
      });

      setShortUrl(res.data.short_url);
    } catch (err) {
      console.log(err);
      alert("Error shortening URL");
    }

    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>🔗 URL Shortener</h1>

      <input
        placeholder="Enter URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ padding: "10px", width: "300px" }}
      />

      <br /><br />

      <button onClick={shortenUrl} disabled={loading}>
        {loading ? "Shortening..." : "Shorten"}
      </button>

      {shortUrl && (
        <div style={{ marginTop: "20px" }}>
          <a href={shortUrl} target="_blank" rel="noreferrer">
            {shortUrl}
          </a>
        </div>
      )}
    </div>
  );
}

export default App;