# This runs the application
from phone_data import phones
from tmo_api import TmoData
from phone import Phone
from view import View
from controller import Controller
from router import Router
from repo import Repo

phone_repo = Repo(phones())
app_view = View()
app_controller = Controller(app_view, phone_repo)
router = Router(app_controller)

router.run()
