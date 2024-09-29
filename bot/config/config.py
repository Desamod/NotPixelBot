from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [3000, 8000]
    START_DELAY: list[int] = [5, 60]
    AUTO_PAINT: bool = True
    AUTO_MINING: bool = True
    AUTO_TASK: bool = True
    AUTO_UPGRADE: bool = True
    AUTO_UPGRADE_PAINT: bool = True
    MAX_PAINT_LEVEL: int = 7
    AUTO_UPGRADE_RECHARGE_SPEED: bool = True
    MAX_RECHARGE_LEVEL: int = 4
    AUTO_UPGRADE_ENERGY: bool = True
    MAX_ENERGY_LEVEL: int = 3
    USE_RANDOM_COLOR: bool = True
    OWN_COLOR: str = "#FFFFFF"
    NIGHT_SLEEP: bool = True
    NIGHT_SLEEP_START_TIME: list[int] = [0, 2]
    NIGHT_SLEEP_END_TIME: list[int] = [5, 7]
    REF_ID: str = 'f342952117'


settings = Settings()
