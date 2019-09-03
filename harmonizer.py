import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


class Studio(object):

    def __init__(self, offer_input_pin, accept_input_pin):
        self._offer_ip = None
        self._accept_ip = None

        self.offer_input_pin = offer_input_pin
        self.accept_input_pin = accept_input_pin

    @property
    def offer_input_pin(self):
        return self._offer_ip

    @offer_input_pin.setter
    def offer_input_pin(self, val):
        try:
            new_pin = int(val)
        except ValueError:
            raise ValueError("Offer input pin value must be an integer! Got %s (type %s)" % (
                val, type(val)))
        else:
            # Clear the existing channel so that it can be used by something else
            if self.offer_input_pin:
                GPIO.remove_event_detect(self.offer_input_pin)
                GPIO.cleanup(self.offer_input_pin)

            # Setup the new channel
            self._offer_ip = new_pin
            GPIO.setup(new_pin, GPIO.INPUT, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(new_pin, GPIO.FALLING,
                                  callback=self.on_pin_fall)

    @property
    def accept_input_pin(self):
        return self._offer_ip

    @accept_input_pin.setter
    def accept_input_pin(self, val):
        try:
            new_pin = int(val)
        except ValueError:
            raise ValueError("Accept input pin value must be an integer! Got %s (type %s)" % (
                val, type(val)))
        else:

            # Clear the existing channel so that it can be used by something else
            if self.accept_input_pin:
                GPIO.remove_event_detect(self.accept_input_pin)
                GPIO.cleanup(self.accept_input_pin)

            # Setup the new channel
            self._accept_ip = new_pin
            GPIO.setup(new_pin, GPIO.INPUT, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(new_pin, GPIO.FALLING,
                                  callback=self.on_pin_fall)

    def on_pin_fall(self, channel):
        print "Pin %s is falling!" % channel

    def on_pin_rise(self, channel):
        print "Pin %s is rising!" % channel


s1 = Studio(21, 12)
s1.accept_input_pin = "cheese"
