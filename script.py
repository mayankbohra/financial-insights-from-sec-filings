from sec_edgar_downloader import Downloader
import os

path = os.environ.get("CUSTOM_PATH")
name = os.environ.get("CUSTOM_NAME")
email = os.environ.get("CUSTOM_EMAIL")

dl = Downloader(name, email, download_folder=path)

dl.get("10-K", "AAPL", after="1994-01-01", before="2024-01-01", download_details=False)
dl.get("10-K", "MSFT", after="1994-01-01", before="2024-01-01", download_details=False)
dl.get("10-K", "META", after="1994-01-01", before="2024-01-01", download_details=False)