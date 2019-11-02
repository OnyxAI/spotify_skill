from os.path import dirname, join

from spotify_skill.index import spotify
from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

__author__ = ''

LOGGER = getLogger(__name__)

class SpotifySkill(OnyxSkill):
    def __init__(self):
        super(SpotifySkill, self).__init__(name="SpotifySkill")

    def get_blueprint(self):
        return spotify

    def initialize(self):
        LOGGER.info("Spotify Skill initialize")

    def stop(self):
        pass

def create_skill():
    return SpotifySkill()
