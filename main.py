from controllers.buku_controller import BukuController
from views.buku_view import BukuView

if __name__ == "__main__":
    view = BukuView()
    app = BukuController(view)
    app.run()