from PyQt5.QtCore import pyqtSignal, QObject


class FileLoadedWrapper(QObject):
    signal = pyqtSignal(str)

class Foo(QObject):

    # Define a new signal called 'trigger' that has no arguments.
    trigger = pyqtSignal()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.

        print("trigger signal received")
