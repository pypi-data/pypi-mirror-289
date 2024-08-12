from plexflow.core.torrents.providers.tpb.tpb import TPB
from plexflow.core.torrents.providers.yts.yts import YTS
from plexflow.core.torrents.providers.torrentquest.torrentquest import TorrentQuest
from typing import List
from plexflow.core.torrents.results.torrent import Torrent

class AutoTorrents:
    @staticmethod
    def movie(imdb_id: str = None, query: str = None, source: str = 'yts', **kwargs) -> List[Torrent]:
        if source == 'tpb':
            return TPB().search(query=imdb_id)
        elif source == 'yts':
            return YTS().search(query=imdb_id)
        elif source == 'torrentquest':
            return TorrentQuest(**kwargs).search(query=query)
        else:
            raise ValueError(f"Invalid source: {source}")
