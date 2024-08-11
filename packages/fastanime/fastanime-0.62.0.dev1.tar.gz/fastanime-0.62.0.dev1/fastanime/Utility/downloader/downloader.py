import logging
from queue import Queue
from threading import Thread

import yt_dlp
from yt_dlp.utils import sanitize_filename

logger = logging.getLogger(__name__)


class YtDLPDownloader:
    downloads_queue = Queue()

    def _worker(self):
        while True:
            task, args = self.downloads_queue.get()
            try:
                task(*args)
            except Exception as e:
                logger.error(f"Something went wrong {e}")
            self.downloads_queue.task_done()

    def __init__(self):
        self._thread = Thread(target=self._worker)
        self._thread.daemon = True
        self._thread.start()

    # Function to download the file
    # TODO: untpack the title to its actual values episode_title and anime_title
    def _download_file(self, url: str, download_dir, title, silent, vid_format="best"):
        anime_title = sanitize_filename(title[0])
        episode_title = sanitize_filename(title[1])
        ydl_opts = {
            # Specify the output path and template
            "outtmpl": f"{download_dir}/{anime_title}/{episode_title}.%(ext)s",
            "silent": silent,
            "verbose": False,
            "format": vid_format,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def download_file(self, url: str, title, silent=True):
        self.downloads_queue.put((self._download_file, (url, title, silent)))


downloader = YtDLPDownloader()
