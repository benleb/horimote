[![Build
Status](https://travis-ci.org/benleb/horimote.svg?branch=master)](https://travis-ci.org/benleb/horimote)
[![PyPI](https://img.shields.io/pypi/v/horimote.svg)](https://pypi.python.org/pypi/horimote/)

# Horimote
Horimote is a simple Python library for the Horizon HD-Recorder sold by Unitymedia Germany.

Thanks to [OrangeTux](https://github.com/OrangeTux) & [kuijp](https://github.com/kuijp) for their work on [einder](https://github.com/OrangeTux/einder) & [horizoncontrol](https://github.com/kuijp/horizoncontrol). This is just another Python fork focussing on the Horzion HD-Recorder from Unitymedia Germany.

## Installation
```bash
$ pip install horimote
```

## Usage
`horimote.Client` controls the set-top box by sending bytes. These bytes
represent the buttons of a remote control. You can find all supported
keys in [horimote.keys](horimote/keys.py). The example shows how to send
keys.

```python
import time

import logging
from horimote import Client
from horimote import keys

# Enable logging.
logging.basicConfig(level=logging.DEBUG)

# Replace IP with the IP of your set-top box. The port parameter is optional,
# by default its 5900.
c = Client("192.168.1.245", port=5900)

c.power_on()

# Wait a few seconds to let the set-top box have some time to start.
time.sleep(5)

# Select channel 501.
c.send_key(keys.NUM_5)
c.send_key(keys.NUM_0)
c.send_key(keys.NUM_1)

# For selecting a channel horimote.Client offers a small helper function.
c.select_channel(501)

# No watch some TV...

c.power_off()
c.disconnect()
```

The `horimote.Client` can also be used as a context manager:

``` {.sourceCode .python}
from horimote import Client

with Client("192.168.1.245") as c:
    c.select_channel(501)
```

License
=======

This software is licensed under the [MIT license](LICENSE).
