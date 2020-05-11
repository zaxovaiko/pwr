import sys
import os
import paho.mqtt.client as mqtt
import tkinter as tk
from dotenv import load_dotenv


def run_client():
    has_access = False
    login_window = None
    placeholder = None

    def show_login_window():
        nonlocal login_window, placeholder
        login_window = tk.Tk()
        login_window.title('Log in')
        login_window.resizable(False, False)

        placeholder = tk.Label(login_window, text='Use your credentials to log in.')
        placeholder.grid(column=0, row=0, columnspan=6, pady=(15, 5), padx=15)

        tk.Label(login_window, text='Login').grid(column=1, row=1, columnspan=1, padx=(15, 5), pady=(20, 5))
        tk.Label(login_window, text='Password').grid(column=1, row=2, columnspan=1, padx=(15, 5), pady=(15, 10))
        tk.Button(login_window,
                  text='Log in',
                  command=lambda: client.publish(os.getenv('TOPIC_AUTH'), f'{name_in.get()},{pass_in.get()}'))\
            .grid(column=4, row=3,  sticky='nsew', padx=(15, 0), pady=(0, 15))

        name_in = tk.Entry(login_window)
        pass_in = tk.Entry(login_window)
        name_in.grid(column=3, row=1, columnspan=3, pady=(15, 5), padx=(0, 15), sticky='news')
        pass_in.grid(column=3, row=2, columnspan=3, pady=(10, 10), padx=(0, 15), sticky='news')

        login_window.mainloop()

    def show_client_window():
        window = tk.Tk()
        window.title('Client')
        window.resizable(False, False)

        terminal_label = tk.Label(window, text=f'{os.getenv("TERMINAL")} is connected.')
        terminal_label.grid(column=0, row=0, columnspan=6, pady=(15, 5), padx=15)

        card_id_textfield = tk.Entry(window)
        card_id_textfield.grid(column=1, row=1, columnspan=5, pady=(5, 10), padx=(0, 15))

        def publish():
            if card_id_textfield.get().isdigit():
                client.publish(os.getenv('TOPIC_CARD'), int(card_id_textfield.get()))
                terminal_label.config(text='Card ID was sent.')
            else:
                terminal_label.config(text='Card ID must be a number.')

        def stop():
            client.loop_stop()
            client.disconnect()
            sys.exit(0)

        tk.Label(window, text='Card ID').grid(column=0, row=1, columnspan=1, padx=(15, 5))
        ct = tk.Button(window, text="Check card", command=publish)
        ct.grid(column=1, row=2, columnspan=3, pady=(5, 15))
        tk.Button(window, text="Stop", command=stop).grid(column=4, row=2, columnspan=2, pady=(5, 15))

        window.mainloop()

    def on_connect(client, userdata, flags, rc):
        print(mqtt.connack_string(rc))
        if rc != 0:
            print('Error has occurred. Reload script.')
            sys.exit(0)

    def on_message(client, userdata, message):
        msg = message.payload.decode("utf-8")
        if msg == 'Success':
            nonlocal has_access
            has_access = True
            login_window.destroy()
        else:
            nonlocal placeholder
            placeholder.config(text='Invalid data.')

    client = mqtt.Client(os.getenv('TERMINAL'))
    client.tls_set(os.getenv('CERTIFICATE'))
    client.username_pw_set(username=os.getenv('CLIENT_USER'), password=os.getenv('CLIENT_PASS'))
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(os.getenv('BROKER'), int(os.getenv('PORT')))
    client.loop_start()
    client.subscribe(os.getenv('TOPIC_RES'))

    show_login_window()
    if has_access:
        show_client_window()


if __name__ == '__main__':
    load_dotenv()
    run_client()
