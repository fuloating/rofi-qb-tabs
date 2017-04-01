rofi-qb-tabs
============

Qutebrowser's session handling in a rofi's dmenu-like list. This script is meant to replace the browser's own session handling allowing returning user to launch clean qutebrowser without reloading the websites from the last session, yet access them on demand.

Installation
------------

Place qbuserscript.py to qutebrowser's userscript dir. Place tabs.sh to a dir defined in the outFilename variable in qbuserscript.py. Place empty file named tabs to a dir defined in the TABFILE variable in tabs.sh.

Usage
-----

The qbuserscript.py userscript saves the current qutebrowser session for rofi to use and quits qutebrowser. Invoke it in qutebrowser with `:spawn --userscript qbuserscript.py`.

Run the rofi menu with `rofi -show tabs -modi tabs:<path-to-tabs.sh>` to open up the list of websites from the previous sessions. Executing one of the websites from the rofi list will launch that URL in the qutebrowser and remove it from the list.

If qutebrowser is run in "tabs-are-windows" mode, you could run a rofi list with currently open windows plus the saved websites from previous sessions for example with: `rofi -combi-modi "window,tabs:$HOME/scripts/rofi/tabs.sh" -show combi -modi combi,tabs:$HOME/scripts/rofi/tabs.sh`
