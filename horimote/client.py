# coding=utf-8
import socket
import struct
from logging import getLogger
from http.client import HTTPConnection

from horimote import keys
from horimote.exceptions import AuthenticationError

log = getLogger(__name__)


class Client:
    """ The set-top box Client. """
    def __init__(self, ip, port=5900):
        self.ip = ip
        self.port = port

        self.con = None

        self.connect()
        self.authorize()

    def connect(self):
        """ Connect sets up the connection with the Horizon box. """
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.con.connect((self.ip, self.port))

        log.debug('Connected with set-top box at %s:%s.',
                  self.ip, self.port)

    def disconnect(self):
        """ Disconnect closes the connection to the Horizon box. """
        if self.con is not None:
            self.con.close()
            log.debug('Closed connection with with set-top box at %s:%s.',
                      self.ip, self.port)

    def authorize(self):
        """ Use the magic of a unicorn and summon the set-top box to listen
        to us.

                            /
                       ,.. /
                     ,'   ';
          ,,.__    _,' /';  .
         :','  ~~~~    '. '~
        :' (   )         )::,
        '. '. .=----=..-~  .;'
         '  ;'  ::   ':.  '"
           (:   ':    ;)
            \\   '"  ./
             '"      '"

        Seriously, I've no idea what I'm doing here.
        """
        # Read the version of the set-top box and write it back. Why? I've no
        # idea.
        version = self.con.makefile().readline()
        self.con.send(version.encode())

        # The set-top box returns with 2 bytes. I've no idea what they mean.
        self.con.recv(2)

        # The following reads and writes are used to authenticate. But I don't
        # fully understand what is going on.
        self.con.send(struct.pack('>B', 1))
        msg = self.con.recv(4)
        response = struct.unpack(">I", msg)

        if response[0] != 0:
            log.debug("Failed to authorize with set-top at %s:%s.",
                      self.ip, self.port)
            raise AuthenticationError()

        # Dunno where this is good for. But otherwise the client doesn't work.
        self.con.send(b'0')
        log.debug('Authorized succesfully with set-top box at %s:%s.',
                  self.ip, self.port)

    def send_key(self, key):
        """ Send a key to the Horizon box. """
        cmd = struct.pack(">BBBBBBH", 4, 1, 0, 0, 0, 0, key)
        self.con.send(cmd)

        cmd = struct.pack(">BBBBBBH", 4, 0, 0, 0, 0, 0, key)
        self.con.send(cmd)

    def is_powered_on(self):
        """ Get power status of device.

        The set-top box can't explicitly powered on or powered off the device.
        The power can only be toggled.

        To find out the power status of the device a little trick is used.
        When the set-top box is powered a web server is running on port 62137
        of the device server a file at /DeviceDescription.xml. By checking if
        this file is available the power status can be determined.

        :return: Boolean indicitation if device is powered on.
        """
        host = '{0}:29153'.format(self.ip)
        try:
            HTTPConnection(host, timeout=2).\
                request('GET', '/description1.xml')
        except (ConnectionRefusedError, socket.timeout):
            log.debug('Set-top box at %s:%s is powered off.',
                      self.ip, self.port)

            return False

        log.debug('Set-top box at %s:%s is powered on.', self.ip, self.port)
        return True

    def power_on(self):
        """ Power on the set-top box. """
        if not self.is_powered_on():
            log.debug('Powering on set-top box at %s:%s.', self.ip, self.port)
            self.send_key(keys.POWER)

    def power_off(self):
        """ Power on the set-top box. """
        if self.is_powered_on():
            log.debug('Powering off set-top box at %s:%s.', self.ip, self.port)
            self.send_key(keys.POWER)

    def select_channel(self, channel):
        """ Select a channel.

        :param channel: Number of channel.
        """
        for i in str(channel):
            key = int(i) + 0xe300
            self.send_key(key)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.disconnect()
