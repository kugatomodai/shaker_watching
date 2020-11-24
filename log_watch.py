# watchdogでファイルを監視する
# ファイルの最終行が変更されたら、load_data.pyを実行する
# 1秒に1度ファイルの監視を走らせる... shakerのデータ取得最小単位が1 minなので


from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os
import sys
import subprocess

target_dir = 'C:\\Users\\xxx\\Desktop\\ODVeiwer'

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        filepath = event.src_path # modified file path here
        filename = os.path.basename(filepath) # modified file name here 
        print("%s data coming" % filename)
        subprocess.call('python load_data.py %s' % filename, shell=True)
        subprocess.call('python machinist.py %s' % filename, shell=True)

# execute every one second       
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
