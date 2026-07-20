from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = ('Собирает пожертвования на всевозможные задачи, '
                            'связанные с помощью кошачьей популяции:'
                            ' на корм, на медицинское обслуживание, '
                            'организацию приютов и на другую помощь котам, '
                            'кошкам и котятам.')
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()