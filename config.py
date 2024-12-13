import os

BASE_URL = os.getenv('OPENSPOOLMAN_BASE_URL') # Where will this app be accessible
PRINTER_ID = os.getenv('PRINTER_ID')  # Printer serial number - Run init_bambulab.py
PRINTER_CODE = os.getenv('PRINTER_ACCESS_CODE')       # Printer access code - Run init_bambulab.py
PRINTER_IP = os.getenv('PRINTER_IP')     # Printer local IP address - Check wireless on printer
SPOOLMAN_BASE_URL = os.getenv('SPOOLMAN_BASE_URL')
SPOOLMAN_API_URL = f"{SPOOLMAN_BASE_URL}/api/v1"