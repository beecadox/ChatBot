from tkinter import *
from chat import chatbot_response
from check_functions import check_if_name, check_if_food_item


def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    global name_flag, addr, tel, name
    global price
    start_chat = 0
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        if name_flag == 2:
            addr = msg.replace("addr ", "")
        if name_flag == 1:
            tokens = msg.split()
            if len(tokens) == 1:
                tel = tokens[0]
            else:
                for t in tokens:
                    if t.isnumeric():
                        tel = t
            name_flag += 1
        ChatLog.config(foreground="#3d7043", font=("Arial", 12))
        res = chatbot_response(msg)
        flag, tmp_price = check_if_food_item(msg)
        tmp_flag = check_if_name(msg)
        if tmp_flag == 1:
            name = msg.replace("name ", "")
            name_flag = 1
        price = price + tmp_price

        if flag == 1:
            ChatLog.insert(END, "KabooliBot: \nTotal: " + str(price) + ' €\n' + res + '\n')
            flag = 0
        else:
            ChatLog.insert(END, "KabooliBot: " + res + '\n\n')
            if res == "Thank you for choosing Kabooli World. Estimated delivery time 30 minutes":
                ChatLog.insert(END, "\n\tName: " + name + '\n\tTelephone Number: ' + tel +
                               '\n\tAddress: ' + addr + '\n\tTotal:' + str(price) + ' €\n\nTo quit close window\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("KABOOLI WORLD!")
base.geometry("600x700")
base.resizable(width=FALSE, height=FALSE)
# Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", )

ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("Arial", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#c4868c", activebackground="#9d3e3c", fg='#000000',
                    command=send)

# Create the box to enter message
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

# Place all components on the screen
scrollbar.place(x=576, y=6, height=586)
ChatLog.place(x=6, y=6, height=586, width=570)
EntryBox.place(x=148, y=601, height=90, width=430)
SendButton.place(x=6, y=601, height=90)
base.mainloop()
