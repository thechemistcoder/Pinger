# import modules
from pythonping import ping
import tkinter as tk
import ttkbootstrap as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pinger')
        self.geometry('400x600')

        #Label
        self.label = ttk.Label(text='Enter URL or IP:')
        self.label.pack(pady=20)

        #Entry
        self.entry = ttk.Entry(width=50)
        self.entry.pack(pady=20)
        
        #Button
        self.button = ttk.Button(text='Ping',width=50,command=self.ping)
        self.button.pack(pady=20)

        #Label
        self.label_result = ttk.Label(text='')
        self.label_result.pack(pady=20)



    def ping(self):
        host = self.entry.get()
        result = ping(host, verbose=True)
        self.label_result.config(text=result)

    def run(self):
        self.mainloop()

app = App()
if __name__=='__main__':
    app.run()