from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib


def save_artifact(artifact: Any, path: str | Path) -> None:
    """Persist a model or metadata artifact."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, output_path)


def load_artifact(path: str | Path) -> Any:
    """Load a persisted artifact."""
    return joblib.load(Path(path))
