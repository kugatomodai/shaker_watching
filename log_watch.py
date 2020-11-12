# watchdogでファイルを監視する
# ファイルの最終行が変更されたら、load_data.pyを実行する
# 1分に1度ファイルの監視を走らせる... shakerのデータ取得最小単位が1 minなので


from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os

target_dir = 'C:\\Users\\xxx\\Desktop\\ODVeiwer'
target_file = '*.txt'

class ChangeHandler(FileSystemEventHandler):
   # def __init__(self, command, patterns):
       # super(ChangeHandler, self).__init__(patterns=patterns)
       # self.command = command

  #  def _run_command(self):
       # subprocess.call([self.command, ])

    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print("data coming")
        

if __name__ == "__main__":
     event_handler = ChangeHandler()
     observer = Observer()
     observer.schedule(event_handler, target_dir, recursive=True)
     observer.start()
     try:
         while True:
             time.sleep(1)
     except KeyboardInterrupt:
         observer.stop()
     observer.join()

