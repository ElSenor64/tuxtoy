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
        button4 = Gtk.Button.new()
        button5 = Gtk.Button.new()
        button6 = Gtk.Button.new()
        button7 = Gtk.Button.new()
        button8 = Gtk.Button.new()
        button9 = Gtk.Button.new()

        iconSize = 128
        # iconSizes = Gtk.IconSet
        favicon = Gtk.Image.new()
        image2 = Gtk.Image.new()
        nope = Gtk.Image.new()
        icon1 = Gtk.Image.new()
        icon2 = Gtk.Image.new()
        icon3 = Gtk.Image.new()
        icon4 = Gtk.Image.new()
        icon5 = Gtk.Image.new()
        icon6 = Gtk.Image.new()
        icon7 = Gtk.Image.new()
        icon8 = Gtk.Image.new()
        icon9 = Gtk.Image.new()

        favicon.set_from_file("gchrom1.png")
        image2.set_from_file("tux.png")
        # nope.set_from_icon_name("action-unavailable-symbolic", 48)
        icon1.set_from_file("icons/cmatrix.png")
        icon2.set_from_file("icons/oneko.png")
        icon3.set_from_file("icons/pi.png")
        icon4.set_from_file("icons/xeyes.png")
        icon5.set_from_file("icons/starwars.png")
        icon6.set_from_file("icons/rev.svg")
        icon7.set_from_file("icons/figlet.png")
        icon8.set_from_file("icons/nope.png")
        icon9.set_from_file("icons/nope.png")
        homeGrid.set_column_homogeneous(True)
        # homeGrid.set_column_spacing(2)
        homeGrid.set_row_homogeneous(True)
        # homeGrid.set_row_spacing(3)
        button1.set_image(icon1)
        button1.set_always_show_image(True)
        button2.set_image(icon2)
        button2.set_always_show_image(True)
        button3.set_image(icon3)
        button3.set_always_show_image(True)
        button4.set_image(icon4)
        button4.set_always_show_image(True)
        button5.set_image(icon5)
        button5.set_always_show_image(True)
        button6.set_image(icon6)
        button6.set_always_show_image(True)
        button7.set_image(icon7)
        button7.set_always_show_image(True)
        button8.set_image(icon8)
        button8.set_always_show_image(True)
        button9.set_image(icon9)
        button9.set_always_show_image(True)

        homeGrid.attach(button1, 0, 0, 2, 1)
        homeGrid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 2, 1)
        homeGrid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 2, 1)
        homeGrid.attach_next_to(button4, button1, Gtk.PositionType.BOTTOM,2, 1)
        homeGrid.attach_next_to(button5, button4, Gtk.PositionType.RIGHT, 2, 1)
        homeGrid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 2, 1)
        homeGrid.attach_next_to(button7, button4, Gtk.PositionType.BOTTOM,2, 1)
        homeGrid.attach_next_to(button8, button7, Gtk.PositionType.RIGHT, 2, 1)
        homeGrid.attach_next_to(button9, button8, Gtk.PositionType.RIGHT, 2, 1)
        # homeGrid.insert_column(1)
        # homeGrid.insert_column(2)
        # homeGrid.insert_column(3)
        # homeGrid.insert_row(1)

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