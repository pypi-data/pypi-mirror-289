from .collections import SMessage
from spotdl.types.song import Song
from spotdl.utils.spotify import SpotifyClient
from spotdl.download.downloader import Downloader
from spotdl.utils.formatter import create_file_name
#===============================================================================

class DownloadSR:

    def clinton() -> None:
        DATA01 = '4fe3fecfe5334023a1472516cc99d805'
        DATA02 = '0f02b7c483c04257984695007a4a8d5c'
        try: SpotifyClient.init(client_id=DATA01, client_secret=DATA02)
        except Exception: pass

#===============================================================================
            
    async def filename(songid, title="{title}", extension="mp3"):
        return create_file_name(songid, title, extension)

#===============================================================================

    async def started(songid, config):
        engine = Downloader(config)
        return engine.download_song(songid)

#===============================================================================

    async def download(songid, config):
        try:
            moonus = await DownloadSR.started(songid, config)
            return SMessage(status=True, result=moonus)
        except Exception as errors:
            return SMessage(errors=str(errors))

#===============================================================================

    async def getuid(incoming):
        try:
            moonus = Song.from_url(incoming)
            return SMessage(status=True, result=moonus)
        except Exception as errors:
            return SMessage(status=False, errors=errors)

#===============================================================================
