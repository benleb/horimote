|Build Status| |PyPI|

Horimote
======

Horimote is an API wrapper for the set-top boxes SMT C7400 and SMT C7401.
In the Netherlands these boxes are sold by a big Dutch cable operator
under the name Horizon Box. The name Einder is a Dutch synonym for
horizon.

I'd like to thank `kuijp <https://github.com/kuijp>`__ for his
work on `horizoncontrol <https://github.com/kuijp/horizoncontrol>`__.
This is just a shameless Python rip off.

Installation
------------

.. code:: shell

    $ pip install horimote

Usage
-----

``horimote.Client`` controls the set-top box by sending bytes. These bytes
represent the buttons of a remote control. You can find all supported
keys in `horimote.keys <horimote/keys.py>`__. The example shows how to
send keys.

.. code:: python

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

The ``horimote.Client`` can also be used as a context manager:

.. code:: python

    from horimote import Client

    with Client("192.168.1.245") as c:
        c.select_channel(501)

License
-------

This software is licensed under the `MIT license <LICENSE>`__.

.. |Build Status| image:: https://travis-ci.org/OrangeTux/horimote.svg?branch=master
   :target: https://travis-ci.org/OrangeTux/horimote
.. |PyPI| image:: https://img.shields.io/pypi/v/horimote.svg
   :target: https://pypi.python.org/pypi/horimote/
