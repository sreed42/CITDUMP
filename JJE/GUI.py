import main
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


builder = Gtk.Builder()
builder.add_from_file("MansionGUI.glade")
#builder.connect_signals(Handler())

window = builder.get_object("applicationwindow1")
window.show_all()

Gtk.main()