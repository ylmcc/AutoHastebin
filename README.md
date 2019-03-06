# Auto Hastebin
Uploads your file to any hosted hastebin. In this example https://paste.redbrick.dcu.ie is used.

For Ubuntu <br>
<strong> chmod +x haste.py </strong>this allows it to be executed by anyone.

Copy it to <strong>/usr/local/bin</strong> <br>Once done enter: <strong>alias haste /usr/local/bin/haste.py</strong>

Finally ready to go!

Syntax: <strong>haste filename </strong>

To keep it permanent you will need to add the alias to <strong>~/.bashrc</strong><br>

Open the file with vim ~/.bashrc<br><br>Go to the bottom (Hint! Press G)<br><br>
Add the following:<strong> alias haste=/usr/local/bin/haste.py</strong><br><br>
<strong>:wq</strong> to leave vim<br><br>
To make sure bash saves it <strong>source ~/.bashrc</strong>
