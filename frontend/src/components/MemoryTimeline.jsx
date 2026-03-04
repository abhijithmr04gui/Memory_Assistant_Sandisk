import { useEffect, useState } from "react";
import { getMemories } from "../api";

export default function MemoryTimeline() {
  const [memories, setMemories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchMemories = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getMemories();
      setMemories(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || "Failed to load memories");
      setMemories([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMemories();
  }, []);

  if (loading) return <p className="timeline-loading">Loading memories...</p>;
  if (error) return <p className="error">{error}</p>;

  return (
    <div className="memory-timeline">
      <h3>Memory Timeline</h3>
      {memories.length === 0 ? (
        <p className="empty">No memories yet. Add one above!</p>
      ) : (
        <div className="timeline-list">
          {memories.map((m, i) => (
            <div key={i} className="memory-card">
              <p>{m.text}</p>
              {m.timestamp && <small>{m.timestamp}</small>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
