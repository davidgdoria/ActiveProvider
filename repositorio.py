from datetime import datetime, timezone


class RepositorioInstancias:
    def __init__(self) -> None:
        self._instancias: dict[str, dict] = {}

    def criar_instancia(self, activity_id: str) -> dict:
        """Register an instance; a repeated deploy keeps the existing data."""
        return self._instancias.setdefault(
            activity_id,
            {"activityID": activity_id, "criada_em": datetime.now(timezone.utc).isoformat()},
        )

    def existe_instancia(self, activity_id: str) -> bool:
        """Check whether an instance has been deployed."""
        return activity_id in self._instancias
