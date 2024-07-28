import weakref

"""
Consider an iPhone inventory application: each individual iPhone possesses a unique serial number,
yet most of the device's details remain identical.
In the absence of the Flyweight Pattern, 
every iPhone instance would necessitate storage of a
comprehensive list of features, leading to an unsustainable accumulation of wasted memory.
"""

class PhoneModel:
    _models = weakref.WeakKeyDictionary()
    
    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model
        
        return model

    def __init__(self, model_name, air=False, title=False,
                 touch_screen=False, face_locks=False,
                 camera=False, usb_charger=False):
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.title = title
            self.touch_screen = touch_screen
            self.face_locks = face_locks
            self.camera = camera
            self.usb_charger = usb_charger