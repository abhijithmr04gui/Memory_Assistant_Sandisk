import { useState } from "react";
import { chat } from "../api";

export default function ChatUI() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendQuery = async () => {
    if (!query.trim()) return;
    const userQuery = query.trim();
    setQuery("");
    setLoading(true);
    setError(null);
    setMessages((prev) => [...prev, { role: "user", text: userQuery }]);
    try {
      const data = await chat(userQuery);
      setMessages((prev) => [...prev, { role: "ai", text: data.answer }]);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || "Failed to get answer");
      setQuery(userQuery);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-ui card">
      <div className="messages">
        {messages.length === 0 && (
          <p className="placeholder">Ask anything about your stored memories...</p>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`message message-${msg.role}`}>
            <strong>{msg.role === "user" ? "You" : "Memory OS"}:</strong> {msg.text}
          </div>
        ))}
        {loading && <div className="message message-ai typing">Thinking...</div>}
      </div>
      {error && <p className="error">{error}</p>}
      <div className="chat-input">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendQuery()}
          placeholder="Ask your memories..."
          disabled={loading}
        />
        <button onClick={sendQuery} disabled={loading || !query.trim()}>
          Ask
        </button>
      </div>
    </div>
  );
}
