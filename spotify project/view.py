import main
from tkinter import *

# Run view.py!!!!!!!!!!!!!


class MyWindow:
    def __init__(self, win):

        self.lbl1 = Label(win, text='Artist name?')
        self.lbl1.pack(side=LEFT)
        self.lbl1.place(x=window.winfo_width()/2, y=window.winfo_width()/2)
        self.artist = Entry(win, bd=1.5)
        self.artist.pack(side=RIGHT)
        self.artist.place(x=window.winfo_width()/2+100)
# Entry(win, text='Song')
        self.results = Listbox(win)
        self.results.place(width=350, x=window.winfo_width()/2,
                           y=window.winfo_width()/2 + 100)
        # Button
        self.btn_search = Button(win, text='Search', command=self.search)
        self.btn_search.place(width=80, x=window.winfo_width()/2 +
                              250, y=window.winfo_width()/2 + 300)

    # event for when search button is pressed

    def search(self):
        self.results.delete(0, 'end')
        artist = self.artist.get()
        name = main.search_for_artist(main.get_token(), artist)
        artist_id = name["id"]
        self.song = main.get_songs_by_artist(main.get_token(), artist_id)
        # array of songs
        Song_list = []
        for S in self.song:
            self.results.insert('end', S['name'])


window = Tk()
mywin = MyWindow(window)
# adding widgets here
window.title('Spotify Song Print')
window.geometry("500x500+10+20")


window.mainloop()
