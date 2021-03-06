.. program:: qu2f-register

:program:`qu2f-register` -- U2F_REGISTER qrexec call
====================================================

Synopsis
--------

:command:`qu2f-register`

Description
-----------

This program handles ``u2f.Register`` qrexec call.

Options
-------

None.

Qrexec calls
------------

``u2f.Register``
    On standard input a complete command APDU is expected. On standard output,
    response APDU is returned.


Bugs
----

To enable debug log, touch either of those files:

- ``/etc/qubes/u2f-debug-enable``

- ``/usr/local/etc/qubes/u2f-debug-enable``

The log will be sent to syslog AUTH facility.

Author
------

| Wojtek Porczyk <woju@invisiblethingslab.com>

.. vim: tw=80
