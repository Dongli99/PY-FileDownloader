<h1 align='center'> Files Downloader </h1>

<div align='center'>

![Static Badge](https://img.shields.io/badge/-python-yellow?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/-argparse-brown?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/-requests-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/-thread-green?style=for-the-badge)
</div>

## Overview

Files Downloader is a Python application for downloading multiple image files from a list of URLs. It offers two modes of operation: serial and threaded.

## Features

- Download images either serially or using multiple threads.
- Accept user-defined output folder for downloaded images.
- Measure and display download time.
- Discarding failed downloads.

## Installation

1. Clone the repository: `git clone https://github.com/Dongli99/PY-FileDownloader.git`
2. Navigate to the project directory: `cd PY-FileDownloader`
3. Install dependencies: `pip install requests`

## Usage

Run the application using the following command:
`python main.py <mode> [-f <folder>]`

- `<mode>`: Specify the download mode. Use `s` for serial mode and `t` for threaded mode.
- `-f, --folder <folder>`: (Optional) Specify the folder where images will be downloaded. If not provided, images will be saved to the default `images` folder.

## Examples

1. Download images serially to the default folder:
`python main.py s`
2. Download images using threads to a custom folder named `downloads`:
`python main.py t -f downloads`
