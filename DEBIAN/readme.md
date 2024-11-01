# Command to build

```bash
chmod 644 cups-printer-http/lib/systemd/system/cups-printer-http.service
chmod 755 cups-printer-http/usr/local/bin/cups-printer-http.py
chmod 755 cups-printer-http/DEBIAN/postinst

sudo dpkg-deb --build cups-printer-http/
```
