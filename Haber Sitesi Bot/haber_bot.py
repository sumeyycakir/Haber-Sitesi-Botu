import feedparser
from tkinter import *
import webview
from datetime import datetime

def default_color_button():
    btn_son_dakika.configure(bg="lightgrey")
    btn_dunya.configure(bg="lightgrey")
    btn_ekonomi.configure(bg="lightgrey")
    btn_saglik.configure(bg="lightgrey")

def clear_frame():
    for widget in fr_haberler.winfo_children():
        widget.destroy()

def open_url(event):
   webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
   webview.start()

def add_haberler(haberler):
   haber_count = 0
   for haber in haberler.entries:
      haber_count = haber_count + 1
      if haber_count > 2:
         break
      
      Label(fr_haberler, text=haber.title, anchor='w', font=('Cambria', 14)).pack(side=TOP, fill="x")
      lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Cambria', 14), fg="blue", cursor="hand2")
      lbl_link.pack(side=TOP, fill="x")
      lbl_link.bind("<Button-1>", open_url)
      Label(fr_haberler, text="-", anchor='c', bg="lightgrey").pack(side=TOP, fill="x")

def son_dakika_command():
    clear_frame()
    default_color_button()
    btn_son_dakika.configure(bg="gold")
    for url in son_dakika_url:
        haberler = feedparser.parse(url)
      # print(url, datetime.now().time())
        add_haberler(haberler)
   
def dunya_command():
     clear_frame()
     default_color_button()
     btn_dunya.configure(bg="gold")
     for url in dunya_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def ekonomi_command():
     clear_frame()
     default_color_button()
     btn_ekonomi.configure(bg="gold")
     for url in ekonomi_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def saglik_command():
     clear_frame()
     default_color_button()
     btn_saglik.configure(bg="gold")
     for url in saglik_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

son_dakika_url = ["https://www.sozcu.com.tr/feeds-son-dakika",
                  "https://www.haberturk.com/rss/kategori/gundem.xml",
                  "https://www.cnnturk.com/feed/rss/all/news",
                  "https://www.ntv.com.tr/gundem.rss"]

ekonomi_url = ["https://www.sozcu.com.tr/feeds-rss-category-ekonomi",
               "https://www.haberturk.com/rss/ekonomi.xml",
               "https://www.cnnturk.com/feed/rss/ekonomi/news",
               "https://www.ntv.com.tr/ekonomi.rss"]

saglik_url = ["https://www.sozcu.com.tr/feeds-rss-category-saglik",
              "https://www.haberturk.com/rss/kategori/saglik.xml",
              "https://www.cnnturk.com/feed/rss/saglik/news",
              "https://www.ntv.com.tr/saglik.rss"]

dunya_url = ["https://www.sozcu.com.tr/feeds-rss-category-dunya",
             "https://www.haberturk.com/rss/kategori/dunya.xml",
             "https://www.cnnturk.com/feed/rss/dunya/news",
             "https://www.ntv.com.tr/dunya.rss"]

window = Tk()
window.title("Haber Bot Programı")
window.geometry("1000x600")


fr_haberler = Frame(window, height=600)
fr_buttons = Frame(window, relief=RAISED, bg="darkgrey", bd=2)


btn_son_dakika = Button(fr_buttons, text="Son Dakika", font=('Times New Roman', 14), bg="lightgrey", command=son_dakika_command)
btn_dunya = Button(fr_buttons, text="Dünya", font=('Times New Roman', 14), bg="lightgrey", command=dunya_command)
btn_ekonomi = Button(fr_buttons, text="Ekonomi", font=('Times New Roman', 14), bg="lightgrey", command= ekonomi_command)
btn_saglik = Button(fr_buttons, text="Sağlık", font=('Times New Roman', 14), bg="lightgrey", command=saglik_command)

btn_son_dakika.grid(row=0,column=0, sticky="ew", padx=5, pady=5)
btn_dunya.grid(row=1,column=0, sticky="ew", padx=5, pady=5)
btn_ekonomi.grid(row=2,column=0, sticky="ew", padx=5, pady=5)
btn_saglik.grid(row=3,column=0, sticky="ew", padx=5, pady=5)


fr_buttons.grid(row=0,column=0, sticky="ns")
fr_haberler.grid(row=0,column=1, sticky="nsew")


window.mainloop()
