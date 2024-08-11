import os, configparser

current_file_directory = os.path.dirname(os.path.abspath(__file__))


class Config:
    @property
    def hostname(self) -> str:
        return (
            self.config.get("DEVELOPMENT", "HOSTNAME")
            if os.environ.get("DEBUG") == "1"
            else self.config.get("PRODUCTION", "HOSTNAME")
        )

    @property
    def version(self) -> str:
        return self.config.get("DEFAULT", "VERSION")

    def set_base_url(self) -> str:
        self.base_url = f"https://{self.hostname}/{self.version}/"

    def set_api_key(self, api_key) -> str:
        self.api_key = (
            api_key or os.environ.get("API_KEY") or self._raise_value_error("API_KEY")
        )

    def set_user_email(self, user_email) -> str:
        self.user_email: str = (
            user_email
            or self.config.get("DEFAULT", "USER_EMAIL")
            or self._raise_value_error("USER_EMAIL")
        )

    def _raise_value_error(self, env_var_name):
        raise ValueError(
            f"A value must be provided or set in the environment variable '{env_var_name}'."
        )

    def __init__(self, api_key, user_email) -> None:
        config_filepath = os.path.join(current_file_directory, "api.ini")
        self.config = configparser.ConfigParser()
        self.config.read(config_filepath)
        self.set_base_url()
        self.set_api_key(api_key)
        self.set_user_email(user_email)
