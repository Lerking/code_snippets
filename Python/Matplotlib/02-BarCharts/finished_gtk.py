import csv
import numpy as np
import pandas as pd
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
from collections import Counter

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
ax.barh(languages, popularity)

ax.set_title("Most Popular Languages")
ax.set_xlabel("Number of People Who Use")

fig.tight_layout()

sw = Gtk.ScrolledWindow()
win.add(sw)
# A scrolled window border goes outside the scrollbars and viewport
sw.set_border_width(10)

canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
canvas.set_size_request(800, 600)
sw.add(canvas)

win.show_all()
Gtk.main()