from src.main import KinkajouApp
import kivy.app as kivy_app


def test_kivy_app_exists():
    assert isinstance(KinkajouApp(), kivy_app.App)
