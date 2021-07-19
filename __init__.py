from mycroft import MycroftSkill, intent_file_handler


class ThunderRatControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.rat.thunder.intent')
    def handle_control_rat_thunder(self, message):
        self.speak_dialog('control.rat.thunder')


def create_skill():
    return ThunderRatControl()

