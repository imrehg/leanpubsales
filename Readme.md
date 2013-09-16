Leanpub Sales
-------------

This scripts uses the Leanpub API to query sales number for your book,
and display info if a new sales has been made.

Have to copy `secrets.py.example` to  `secrets.py` and update the API key
and book slug in there.

You can automate things by adding a similar line in crontab:

    */15 * * * * cd /leanpubsales/; ./sales.py | ifne /usr/bin/mail -s "New Book Sales" "my@email.com"

This will run the script every 15 minutes, and whenever there are new sales, will
send an email to the given address.

For this to work correctly, the `counts.txt` file has to be preserved in the
script's directory, otherwise you'll receive emails every 15 minutes, which
is not fun

License
=======

Copyright (C) 2013 by Gergely Imreh <imrehg@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
