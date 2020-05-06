import time
import os
import logging
import sys
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers import Observer
import os.path
import time

class FileOrganizerEventHandler(FileSystemEventHandler):
    
    # folders and their extensions
    _folderAndExt = {
        "Coding" : ['.vi','.py','.c','.cpp','.java'],
        "Images" : ['.jpg','.jpeg','.bmp','.gif','.png'],
        "Documents" : ['.doc','.docx','.txt','.ppt','.xlsx','.pdf'],
        "Installers" : ['.exe','.msi'],
        "Audio" : ['.mp3','.flac','.wav'],
        "Video" : ['.mp4'],
        "Torrents" : ['.torrent'],
        "Compressed" : ['.zip', '.rar']
    }

    # def on_created(self, event):
    def on_moved(self, event):
        # ignore new folders
        if event.is_directory:
            return

        if not event.src_path.endswith('.crdownload'):
            return
        else:
            time.sleep(1)
        
        # recognize the file
        breakLoop = False
        file_name = os.path.basename(event._dest_path)
        folder_path = os.path.dirname(event._dest_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        file_ext = os.path.splitext(file_name)[1]
        for key in self._folderAndExt:
            for x in self._folderAndExt[key]:
                if x == file_ext:
                    # create a new folder if it doesn't exist
                    if not os.path.exists(os.path.join(folder_path, key)):
                        os.makedirs(os.path.join(folder_path, key))
                    # move the file to correct folder
                    timeout = time.time() + 10 # wait 10s max for access to file 
                    target_path = os.path.join(folder_path, key, file_name)
                    while True:
                        try:
                            # if file with that name exists add ' - x' at the end
                            for x in range(10):
                                if os.path.exists(target_path):
                                    target_path = os.path.join(folder_path, key, (file_name_no_ext + '(' + str(x+2) + ')' + file_ext))
                                    continue
                                os.rename(event._dest_path, target_path)
                                break
                            break
                        except Exception as ex:
                            print(ex)
                            time.sleep(1)
                        if time.time() > timeout:
                            break
                    # set breakLoop variable to break the outer for loop
                    breakLoop = True
                    break
            if breakLoop: break

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # get Downloads folder path
    downloadFolder = os.path.expanduser(r'~\Downloads')

    # listen for new file events
    event_handler = FileOrganizerEventHandler()
    # event_handler = LoggingEventHandler()
    
    # start Observer
    observer = Observer()
    observer.schedule(event_handler, downloadFolder)
    observer.start()
    

    # start endless loop (interuppted by ctrl-C)
    try:
        while True:
            time.sleep(1)
    except(KeyboardInterrupt):
        observer.stop()
    observer.join()