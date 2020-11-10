# watchdogでファイルを監視する
# ファイルの最終行が変更されたら、load_data.pyを実行する
# 1分に1度ファイルの監視を走らせる... shakerのデータ取得最小単位が1 minなので

from watchdog.events import PatternMatchingEventHandler
from watchdog.ovservers import Observer
import time
import os

class ChangeHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        """
        ここをload_data.pyを実行するように変更する
        """

observer = Observer()

#監視するフォルダを第2引数に指定
observer.schedule(ChangeHandler(), './work', recursive=True)

#監視を開始
observer.start()

while True:
    time.sleep(60)
