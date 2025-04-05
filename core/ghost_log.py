from datetime import datetime
from core.interfaces.ghost_log_interface import GhostLogInterface

class GhostLog(GhostLogInterface):
    def __init__(self):
        self._log = []

    def write(self, event: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] {event}"
        self._log.append(entry)
        print(f"👻 Log: {entry}")

    def read_all(self) -> list[str]:
        return self._log.copy()

    def snapshot(self) -> str:
        snapshot_data = "\n".join(self._log)
        return f"📸 Snapshot ({len(self._log)} entries):\n{snapshot_data}"
