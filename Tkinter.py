#from __future__ import unicode_literals
import tkinter as tk
from tkinter import simpledialog
from prompt_toolkit import prompt
from gmail_login import *
import re

## function used to take login details
def show_login_fields(window,email_address,password):
    #login(email_address,password)
    regex = '[^@]+@[^@]+\.[^@]+'
    if(re.search(regex,email_address)):  
        window.destroy()
        if login(email_address,password):
            email_content(email_address,password)
        else:
            login_failed(email_address)
        return
    else:
        window.destroy()
        email_validation(email_address)
        return

## function used to call send email function
def send_email_details(window,email_address,password,from_email,Subject,Message):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,from_email)):  
        window.destroy()
        if sendmail(email_address,password,from_email,Subject,Message):
            email_sent()
        return
    else:
        window.destroy()
        email_validation(from_email)
        return

## function used to set the popup window size
def set_window_size(title):
    window = tk.Tk()
    window.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return(window)

## function displays the login popup
def login_popup():
    
    window = set_window_size("Login Screen")
    
    tk.Label(window, text="Email Address").grid(row=0)
    tk.Label(window, text="Password").grid(row=1)

    from_email = tk.Entry(window)
    password = tk.Entry(window,show="*")
    
    from_email.grid(row=0, column=1)
    password.grid(row=1, column=1)

    btn = tk.Button(window, text='Login', command=lambda: show_login_fields(window,from_email.get(),password.get())).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
    window.mainloop()

## function displays the Email Details popup
def email_content(email_address,password):

    window = set_window_size("Email Details")
    
    tk.Label(window, text="To Email Address").grid(row=0)
    tk.Label(window, text="Subject").grid(row=1)
    tk.Label(window, text="Message").grid(row=2)

    to_email = tk.Entry(window)
    subject = tk.Entry(window)
    message = tk.Entry(window)

    to_email.grid(row=0, column=1)
    subject.grid(row=1, column=1)
    message.grid(row=2, column=1)

    btn=tk.Button(window, text='Send Email', command=lambda: send_email_details(window,email_address,password,to_email.get(),subject.get(),message.get())).grid(row=4, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
    window.mainloop()


## Pop for Login Fail
def login_failed(username):
    window = set_window_size("Login Failed")
    tk.Label(window, text="Login Failed").grid(row=0)
    btn=tk.Button(window, text='Close',command = window.quit).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
    btn1=tk.Button(window, text='Retry',command = lambda: login_popup()).grid(row=4, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
    window.mainloop()

## Popup for Fail email validation 
def email_validation(username):
    window = set_window_size("Fail Email Validation")
    tk.Label(window, text="Login Failed").grid(row=0)
    btn=tk.Button(window, text='Close',command = window.quit).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
    
    btn1=tk.Button(window, text='Retry',command = lambda: login_popup()).grid(row=4, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
    window.mainloop()

## Popup for Successful Mail Transfer
def email_sent():
    window = set_window_size("Email Sent")
    tk.Label(window, text="Email Sent").grid(row=0)
    btn=tk.Button(window, text='Close',command = window.quit).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)


