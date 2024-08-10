# smi_leds

This project allows you to drive 8 or 16 WS2812 LED strips with one single Raspberry Pi!

The basis for this project is Jeremy P Bentham's [rpi_smi_leds](https://github.com/jbentham/rpi/tree/master)
project that uses the RPi's SMI memory interface to accurately drive 8 or 16 LED strips -- flicker free and without
a lot of CPU overhead -- simply amazing. For all the gory details on how this works,
read Jeremy's excellent blog post about his code:

    https://iosoft.blog/category/neopixel/

However, Jeremy's code was just that -- some code, but with zero documentaion on how to
build it (several fixes were needed) or how to install it on a RPi. This project 
addresses those shortcomings and packages that code into a deployable project.

You can choose to link to a static C library build with CMake and include it in your
C/C++ project, or you can choose the python module, which can be installed from pip.

## Design philosophy

This module is for advanced users of LED strips and thus it may be missing some of the 
features you'd expect in other modules (e.g. setting indiviual LED values). For the
moment, this module assumes that you are an advanced user of LEDs and thus likely
already have some tools around creating LED sequences in your toolkit. 

The only way to update the leds is via the led_set() function which takes a buffer
of bytes exactly NUM_STRIPS * NUM_LEDS * 3 in size with LED data and sends it to the 
driver. The led_send() function actually shifts the LEDs out to the LED strips.

There is some code in the driver for setting indiviual pixels, but it wasn't working,
so I've not exposed that function. But if people want that, someone should be able to
make it work.

# Installation

## C/C++ static library

To install smi_leds for 8 LED strands:

```
mkdir build
cd build
cmake ..
make
sudo make install
```

To install for 16 channels, pass an option to cmake:

```
mkdir build
cd build
cmake .. -DENABLE_16_CHANNELS:BOOL=ON
make
sudo make install
```

### Building your own code

To build your own code, run:

```
gcc -I /usr/local/include -L /usr/local/lib my_test.c -lsmi_leds
```

## Python 

To install via pip for 8 LED strands:

```
pip install smi_leds
```

To install via pip for 16 LED strands:

```
export LED_NCHANS=16
pip install smi_leds
```

# Hardware Setup

The image below shows the GPIO pins that will drive the LED strips:

![alt text](https://github.com/mayhem/smi_leds/blob/main/docs/rpi_smi_pinout.png?raw=true)

Remember that each one of these outputs will likely need to be level-shifted to 5V
(unless your LED strips are 3.3V tolerant) and have a 300 Ohm resisor in-line if you'd like
to follow best practices.

Here is the same information in a more convenient table:

![alt text](https://github.com/mayhem/smi_leds/blob/main/docs/rpi_smi_pins-2.png?raw=true)

SD0 through SD17 are the GPIOs that will drive your LED strips.

# Software Setup

## C

The full example in examples/example.c. This simple function sets all the LEDs to
red at 25% brightness and exits:

```
int main(int argc, char *argv[])
{
    bool    ret;
    uint8_t buffer[NUM_LEDS * NUM_STRIPS * 3];
    uint8_t *ptr = buffer;
    
    // TODO: Check the num leds setting
    // initialize the smi_leds module, starting with a 25% brightness
    leds_init(NUM_LEDS, 25);                   
    
    // Manually and slowly build the color buffer. 3 bytes per pixel (RGB) 
    // for NUM_LEDS pixels and NUM_STRIPS strips
    for(int led = 0; led < NUM_LEDS; led++)
    {                                                      
        for(int strip = 0; strip < NUM_STRIPS; strip++)
        {                       
            *(ptr++) = 0x00;    
            *(ptr++) = 0x00;    
            *(ptr++) = 0xFF;
        }             
    }
    
    // Send the buffer to the SMI buffer
    leds_set(buffer);    
    
    // Actually send them to the LEDs:
    leds_send();    
}
```

## Python 3

TODO: Improve the python version and have it match the C version. Explain below:

```
import smi_leds

num_leds = 144 
num_strips = 8
total_leds = num_leds * num_strips
total_bytes = total_leds * 4

def set_led(leds, strip, index, color):
    offset = (strip * num_leds + index) * 4;
    leds[offset] = color[2]
    leds[offset + 1] = color[1]
    leds[offset + 2] = color[0]

smi_leds.leds_init(num_leds, 25)

leds = bytearray((0,) * num_leds * num_strips * 4)
row = 0
while True:
    for strip in range(num_strips):
        for led in range(num_leds):
            if led // 4 % 2 == row % 2:
                color = ( 16, 0, 0 )
            else:
                color = ( 0, 0, 16 )
            set_led(leds, strip, led, color)

    smi_leds.leds_set(leds)
    smi_leds.leds_send()
    row += 1

sleep(1)
```
