from src.main import Kinkajou
import kivy.app as kivy_app


def test_kivy_app_exists():
    assert isinstance(Kinkajou(), kivy_app.App)
