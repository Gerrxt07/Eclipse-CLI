import asyncio
import os
from pathlib import Path

def initialize_directories():
    # Create AppData directory
    parent_appdata_path = os.path.join(os.getenv('APPDATA'), 'Eclipse')
    os.makedirs(parent_appdata_path, exist_ok=True)
    
    # Create CLI directory
    appdata_path = os.path.join(parent_appdata_path, 'CLI')
    os.makedirs(appdata_path, exist_ok=True)

    # Create logs and cache directories
    logs_path = os.path.join(appdata_path, 'Logs')
    sentry_path = os.path.join(appdata_path, 'Sentry')
    storage_path = os.path.join(appdata_path, 'Storage')
    os.makedirs(logs_path, exist_ok=True)
    os.makedirs(sentry_path, exist_ok=True)
    os.makedirs(storage_path, exist_ok=True)

async def Main():
    initialize_directories()
    await asyncio.sleep(1)
    print("Hello World!")
    print("Press any key to continue...")
    
def Run():
    asyncio.run(Main())