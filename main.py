import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Hello World Notebook", application=app)
        self.set_default_size(600, 500)

        tabed = Gtk.Notebook.new()
        homeGrid = Gtk.Grid.new()
        labelTest = Gtk.Label.new("Testing")
        labelHome = Gtk.Label.new("Home")
        button1 = Gtk.Button.new()
        button2 = Gtk.Button.new()
        button3 = Gtk.Button.new()

        iconSize = 32
        image1 = Gtk.Image.new()
        image2 = Gtk.Image.new()
        image3 = Gtk.Image.new()
        image4 = Gtk.Image.new()
        image1.set_from_file("Craft.png")
        image2.set_from_file("tux.png")
        image3.set_from_file("gchrom1.png")
        image4.set_from_file("gchrom2.png")
        homeGrid.set_column_homogeneous(True)
        # homeGrid.set_column_spacing(2)
        homeGrid.set_row_homogeneous(True)
        # homeGrid.set_row_spacing(3)
        button1.set_image(image1)
        button1.set_always_show_image(True)
        button2.set_image(image3)
        button2.set_always_show_image(True)
        button3.set_image(image4)
        button3.set_always_show_image(True)

        # homeGrid.insert_column(1)
        # homeGrid.insert_column(2)
        # homeGrid.insert_column(3)
        # homeGrid.insert_row(1)
        homeGrid.attach(button1, 0, 0, 2, 1)
        # homeGrid.attach_next_to(image2, image1, Gtk.PositionType.RIGHT, 3, 1)
        homeGrid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 2, 1)
        homeGrid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 2, 1)

        # tabed.insert_page_menu()
        tabed.insert_page(homeGrid, labelHome, 0)
        tabed.insert_page(image2, labelTest, -1)
        tabed.set_show_tabs(True)

        # print(row-homogeneous)

        self.add(tabed)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)