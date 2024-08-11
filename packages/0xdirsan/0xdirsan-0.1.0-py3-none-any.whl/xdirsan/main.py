import requests
import argparse
import os
from datetime import datetime
from colorama import Fore, Style
import threading
from queue import Queue

DEFAULT_WORDLIST = os.path.join(os.path.dirname(__file__), 'wordlist', 'wordlist.txt')

DEFAULT_THREADS = 30

def print_banner():
    banner = r"""
   ____       ____  _                     
  / __ \_  __/ __ \(_)_____________ _____ 
 / / / / |/_/ / / / / ___/ ___/ __ `/ __ \
/ /_/ />  </ /_/ / / /  (__  ) /_/ / / / /
\____/_/|_/_____/_/_/  /____/\__,_/_/ /_/ v0.1.0
        https://x-projetion.org/
    """
    print(banner)

def get_wordlist_info(wordlist):
    try:
        with open(wordlist, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)
            total_size = sum(len(line) for line in lines)
            print(f"{Fore.MAGENTA}Wordlist Info Number of Lines: {num_lines} Total Size: {total_size} threads: {DEFAULT_THREADS}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Wordlist file not found at {wordlist}. Using default wordlist.{Style.RESET_ALL}")
        wordlist = DEFAULT_WORDLIST  # Fallback to the default wordlist

def dir_search(url, wordlist, threads):
    get_wordlist_info(wordlist)
    print(f'Start : {url}\n')
    queue = Queue()

    def worker():
        while True:
            path = queue.get()
            full_url = f"{url}/{path}"
            try:
                response = requests.get(full_url)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                status_msg = f"{response.status_code}"
                redirect_msg = f"- Redirected to: {response.url}" if response.history else ""
                file_size = len(response.content) if 'Content-Length' in response.headers else "Unknown"
                if response.status_code == 200:
                    print(f"[{timestamp}] {Fore.GREEN}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
                else:
                    print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            except requests.exceptions.RequestException as e:
                print(f"[{timestamp}] {Fore.RED}[ERROR]{Style.RESET_ALL} {str(e)} for {full_url}")

            queue.task_done()

    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    with open(wordlist, 'r') as f:
        for line in f:
            queue.put(line.strip())

    queue.join()

def print_version():
    version_info = """
    0xdirsan Version 0.1.0

    Developed by: Lutfifakee
    Description: A simple program designed to search for directories 
    within the file system using brute-force with a given list of words.

    For more information, visit: https://x-projetion.org/
    """
    print(version_info)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="0xdirsan is a simple program designed to search for directories in a file system")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file", default=DEFAULT_WORDLIST)
    parser.add_argument("-u", "--urls", help="Target URLs separated by comma (e.g. x-projetion.org)")
    parser.add_argument("-f", "--file", help="File containing target URLs, one per line")
    parser.add_argument("-t", "--threads", help="Number of threads (default 30)", type=int, default=DEFAULT_THREADS)
    parser.add_argument("-v", "--version", action='store_true', help="Show version")
    args = parser.parse_args()

    if not os.path.exists(args.wordlist):
        args.wordlist = DEFAULT_WORDLIST

    urls = []
    if args.version:
        print_version()
        return
    
    if args.file:
        if os.path.exists(args.file):
            with open(args.file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            print("URL file not found.")
            exit(1)
    elif args.urls:
        urls = args.urls.split(",")

    if not urls:
        print("Oops! It seems you haven't provided any URLs. Please use the -u option for direct URLs or -f for a file containing your target URLs.")
        exit(1)

    urls = [url if url.startswith(('http://', 'https://')) else f"http://{url}" for url in urls]

    for url in urls:
        dir_search(url.strip(), args.wordlist, args.threads)

if __name__ == "__main__":
    main()
