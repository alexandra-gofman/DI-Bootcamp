
class Phone:

    def __init__(self, phone_number:int):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
        self.received_messages_history = []
        self.sent_messages_history = []

    def call(self, other_phone):
        calling = f'{self.phone_number} called to {other_phone.phone_number}'
        self.call_history.append(calling)
        return

    def show_call_history(self):
        print(self.call_history)
        return

    def send_message(self, other_phone, message):
        message_dict = {
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'content': message
        }
        self.sent_messages_history.append(message_dict)
        other_phone.received_messages_history.append(message_dict)

        return

    def show_outgoing_messages(self):
        print(self.sent_messages_history)
        return

    def show_incoming_messages(self):
        print(self.received_messages_history)
        return

    def show_messages_from(self, other_phone):
        i = 0
        for message in self.received_messages_history:
            if other_phone.phone_number in message.values():
                print(message['content'])
                i = 1
        if i == 0:
            print(f'There are no messages from {other_phone.phone_number}')
        return


p1 = Phone(111)
p2 = Phone(222)

p1.call(p2)
p1.send_message(p2, "Hi!")
p2.send_message(p1, "Hello!")

p1.show_call_history()
p1.show_incoming_messages()
p2.show_outgoing_messages()
p1.show_messages_from(p2)
