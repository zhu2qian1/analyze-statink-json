class Constants:
    json_path: str = "./resource/statink.json"
    dist_path: str = "./dist/statink.yaml"
    indent_size: int = 2
    default_sr_keys: tuple[str] = (
        "id",
        "url",
        "user",
        "stage",
        "danger_rate",
        "golden_eggs",
        "power_eggs",
        "waves",
        "start_at",
        "shift",
    )
