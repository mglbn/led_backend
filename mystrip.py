from rpi_ws281x import PixelStrip, Color

class MyStrip():

    def __init__(self):
        LED_COUNT = 150        # Number of LED pixels.
        LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
        # LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
        LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA = 10          # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

        self.strip.begin


    def blau(self):
        
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(Color(0,0,255))

        self.strip.show

    def rot(self):

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(Color(255,0,0))

        self.strip.show()


    def aus(self):

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(Color(0,0,0))

        self.strip.show()