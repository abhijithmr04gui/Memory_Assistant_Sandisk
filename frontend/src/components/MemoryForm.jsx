import { useState } from "react";
import { addMemory } from "../api";

export default function MemoryForm({ onStored }) {
  const [memory, setMemory] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const submitMemory = async () => {
    if (!memory.trim()) return;
    setLoading(true);
    setError(null);
    try {
      await addMemory(memory.trim());
      setMemory("");
      onStored?.();
    } catch (err) {
      setError(err.response?.data?.detail || err.message || "Failed to store memory");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="memory-form card">
      <textarea
        value={memory}
        onChange={(e) => setMemory(e.target.value)}
        placeholder="Write your memory..."
        rows={4}
        disabled={loading}
      />
      {error && <p className="error">{error}</p>}
      <button onClick={submitMemory} disabled={loading || !memory.trim()}>
        {loading ? "Storing..." : "Store Memory"}
      </button>
    </div>
  );
}
