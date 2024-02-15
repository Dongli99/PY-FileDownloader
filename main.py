import requests
from time import perf_counter
from argparse import ArgumentParser
from threading import Thread
import os # os ONLY ensure folder/ exists.

class FilesDownloader():
    ## Improvements:
    # 1. This project has been refactored to use a class-based structure, 
    #    enhancing maintainability, readability, and extensibility.
    # 2. The bad response has been handled.

    """
    Init Variables
    """
    def __init__(self):
        self.format = 'jpg'    # default file format
        self.folder = 'images' # default folder
        self.urls =  [         # urls to download files
        "https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.wcEy7Ow-TaAohBCz6USqCAAAAA?w=265&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.9FWt0sWpi4UOee5o3WdI-QHaFj?w=224&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.ZquJ_NwCCyWfvpAEeU-vngAAAA?w=142&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.zSyHBN9_rn_O9XBkdPx-agAAAA?w=189&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.5umgRLykyWn-v_5HmOS0NAHaE7?w=243&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.MPayRq2bYdhfVUj5O9BCnwAAAA?w=125&h=184&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7",
        "https://th.bing.com/th/id/OIP.HCpPn-IRV8SVidBlRoBRUwHaE7?w=287&h=191&c=7&r=0&o=5&pid=1.7",
    ]
        self.downloaded = 0 # num of downloaded files 

    """
    Function conduct downloading one file.
    """
    def download(self, url, path):
        # 1. get response
        response = requests.get(url, stream=True)
        if response.status_code != 200: # bad response will be discarded
            return
        # 2. open the file and write the chunks
        with open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=100):
                file.write(chunk)  # write file
            print(f"{path} download completed.")
        self.count += 1 # update count

    """
    Function record time of normal downloading.
    """
    def downLoadWithTimer(self):
        self.count = 0 # reset count
        # 1. start timer
        start = perf_counter()
        # 2. execute download
        for i in range(len(self.urls)):
            path = f"{self.folder}/{i+1}.{self.format}"
            url = self.urls[i]
            self.download(url, path)
        # 3. end timer and calculate elapse
        end = perf_counter()
        elapse = round(end - start, 2)
        print(f"{self.count} images downloaded in {elapse} seconds, {len(self.urls)-self.count} files failed to download.")

    """
    Function record time of threaded downloading.
    """
    def threadingDownloadWithTimer(self):
        self.count = 0 # reset count
        threads = []  # create a list for threads
        # 1. start timer
        start = perf_counter()
        # 2. execute threading download
        for i in range(len(self.urls)):  # add threads to the list
            path = f"{self.folder}/{i+1}.{self.format}"
            url = self.urls[i]
            t = Thread(target=self.download, args=(url, path))
            t.start()  # start current thread
            threads.append(t)
        for t in threads:  # wait for completing download
            t.join()
        # 3. end timer and calculate elapse
        end = perf_counter()
        elapse = round(end - start, 2)
        print(f"{self.count} images downloaded in {elapse} seconds, {len(self.urls)-self.count} files failed to download.")

    """
    Argument Parsing
    """
    def parse_arguments(self):
        # Create an ArgumentParser object
        parser = ArgumentParser(description="Download all images in one hit.")
        # Add arguments to the parser
        parser.add_argument("-f", "--folder", metavar="F", help="Download images in F folder.")
        parser.add_argument('mode', choices=['s', 't'], help='Select download mode, s for serial, t for threaded.')
        # Return a list of argument values
        return parser.parse_args()

    """
    Driver Method
    """
    def run(self):
        # Parse command line arguments
        args = self.parse_arguments()
        # Set the folder attribute based on the parsed arguments
        if args.folder:
            self.folder = args.folder
        if not os.path.exists(self.folder): # in case the folder is not found
            os.makedirs(self.folder)
        # Invoke the appropriate method based on the selected mode
        if args.mode == 's':
            self.downLoadWithTimer()
        elif args.mode == 't':
            self.threadingDownloadWithTimer()

if __name__ == "__main__":
    # run the application
    downloader = FilesDownloader()
    downloader.run()
