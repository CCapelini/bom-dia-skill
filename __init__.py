from mycroft import MycroftSkill, intent_file_handler


class BomDia(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dia.bom.intent')
    def handle_dia_bom(self, message):
        self.speak_dialog('dia.bom')


def create_skill():
    return BomDia()

