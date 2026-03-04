import { useState, useCallback } from "react";
import MemoryForm from "../components/MemoryForm";
import ChatUI from "../components/ChatUI";
import MemoryTimeline from "../components/MemoryTimeline";

export default function Dashboard() {
  const [refreshKey, setRefreshKey] = useState(0);

  const onMemoryStored = useCallback(() => {
    setRefreshKey((k) => k + 1);
  }, []);

  return (
    <div className="dashboard">
      <div className="left-panel">
        <section className="panel-section">
          <h2>Add Memory</h2>
          <MemoryForm onStored={onMemoryStored} />
        </section>
        <section className="panel-section">
          <MemoryTimeline key={refreshKey} />
        </section>
      </div>
      <div className="right-panel">
        <h2>Ask Memory</h2>
        <ChatUI />
      </div>
    </div>
  );
}
