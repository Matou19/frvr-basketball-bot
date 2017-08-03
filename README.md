# FRVR Basketball Bot

It plays FRVR basketball automated

Notes:
 * You need to install <b>GTK, OpenCV, numpy, pymouse</b> modules
 * It was tested under <b>Linux, 1920x1080</b>. There must be a Windows module to take screenshots, use it instead, and it should work fine
 * If it's so slow, know that its because of image matching with OpenCV

Bugs / to-dos:
* Need to detect if <b>hoop moves</b>, if so, get <b>speed</b> (pixels per second), <b>calculate new destination</b> with time offset (so complicated maybe do when i'm so bored)