# Auto Hastebin
Uploads your file to any hosted hastebin

For Ubuntu <br>
<strong> chmod +x haste.py </strong>this allows it to be executed by anyone.

Copy it to <strong>/usr/local/bin</strong> <br>Once done enter: <strong>alias haste /usr/local/bin/haste.py</strong>

Finally ready to go!

Syntax: <strong>haste filename </strong>

To keep it permanent you will need to add the alias to ~/.bashrc

Open the file with vim ~/.bashrc
Go to the bottom (Hint! Press G)
<strong>alias haste = /usr/local/bin/haste.py</strong>
<strong>:wq</strong> to leave vim
To make sure bash knows about it do <strong>source ~/.bashrc</strong>
