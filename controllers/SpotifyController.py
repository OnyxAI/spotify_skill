# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
"""

from spotify_skill.index import spotify
from flask_login import login_required
from flask import render_template

from spotify_skill.api import *


@spotify.route('/' , methods=['GET','POST'])
@login_required
def index():
    return render_template('spotify/index.html')

@spotify.route('/config' , methods=['GET','POST'])
@login_required
def config():
    return render_template('spotify/config.html')

@spotify.route('/widget')
@login_required
def widget():
    return render_template('spotify/widget.html')
