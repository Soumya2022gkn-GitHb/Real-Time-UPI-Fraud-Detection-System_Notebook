from pathlib import Path


def test_expected_project_directories_exist() -> None:
    project_root = Path(__file__).resolve().parents[1]
    expected_directories = [
        "app",
        "config",
        "data/raw",
        "data/interim",
        "data/processed",
        "data/synthetic",
        "models",
        "notebooks",
        "reports/figures",
        "src/rtufd",
        "tests",
    ]

    missing = [path for path in expected_directories if not (project_root / path).exists()]

    assert not missing, f"Missing directories: {missing}"
