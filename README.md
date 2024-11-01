# ☕️🖨️ cups-printer-http

CUPS is a printing system for Linux and Mac that allows you to print documents to a physical printer. This service allows you to print documents to a printer using an HTTP POST request.

## 📜 API

### POST /print

Prints a document to a printer.

#### Parameters

- `file`: The file to be printed. 🗂️
- `printer`: The name of the printer to print to. 🖨️
- `job`: Optional. The job name to be used when printing the document. If not specified, a default job name will be used. 🏷️
- `server`: Optional. The hostname or IP address of the CUPS server. Defaults to `127.0.0.1`. 🌐

#### Response

The response will be a JSON object with the following properties:

- `status`: The HTTP status code of the response. ✅
- `error`: A boolean indicating whether an error occurred. ❌
- `message`: A human-readable message describing the result of the print request. 📝
- `request_id`: The request ID of the print job. 🔢

## 📚 Tutorial

1. Install the required dependencies (Python 3, Flask, and CUPS client):
   ```bash
   sudo apt-get install python3 python3-flask cups-client
   ```

2. Download the package from the latest release:
   ```bash
   wget https://github.com/RafaelCecchin/cups-printer-http/releases/download/v1.0.0/cups-printer-http.deb
   ```

3. Install the package:
   ```bash
   sudo dpkg -i cups-printer-http.deb
   ```
