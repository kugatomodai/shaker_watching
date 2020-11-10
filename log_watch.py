# watchdogでファイルを監視する
# ファイルの最終行が変更されたら、load_data.pyを実行する
# 1分に1度ファイルの監視を走らせる... shakerのデータ取得最小単位が1 minなので

from watchdog.events import PatternMatchingEventHandler
from watchdog.ovservers import Observer
import time
import os

# 監視対象のディレクトリを指定
target_dir = 'C:\Users\forechem2\Desktop\ODVeiwer'
# 監視対象ファイルのパターンマッチを指定
target_file = '*.txt'

class ChangeHandler(PatternMatchingEventHandler):
    def __init__(self, command, patterns):
        super(ChangeHandler, self).__init__(patterns=patterns)
        self.command = command

    def _run_command(self):
        subprocess.call([self.command, ])

    def on_modified(self, event):
        print("data coming")
        #self._run_command()
        """
        ここをload_data.pyを実行するように変更する
        """

observer = Observer()

#監視するフォルダを第2引数に指定
observer.schedule(ChangeHandler([target_file]), target_dir, recursive=True) #どこでtarget_dir指定する？

#監視を開始
observer.start()

while True:
    time.sleep(60)
