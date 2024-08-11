from datetime import datetime, timedelta
import os
import platform

def get_date(n, unit):
    """
    Return YYYY-mm-dd value from today to n days, months or years in the past
    Parameters:
        n: number of days, months or years
        unit: 'day', 'month' or 'year'
    """
    if unit == 'day':
        return (datetime.now() - timedelta(days=n)).strftime('%Y-%m-%d')
    elif unit == 'month':
        return (datetime.now() - relativedelta(months=n)).strftime('%Y-%m-%d')
    elif unit == 'year':
        return (datetime.now() - relativedelta(years=n)).strftime('%Y-%m-%d')

def get_username():
    try:
        username = os.getlogin()
        return username
    except OSError as e:
        print(f"Error: {e}")
        return None
    
def get_os():
    try:
        os = platform.system()
        return os
    except OSError as e:
        print(f"Error: {e}")
        return None

def get_cwd():
    """Return current working directory"""
    try:
        cwd = os.getcwd()
        return cwd
    except OSError as e:
        print(f"Error: {e}")
        return None

def get_path_delimiter():
    """
    Detect the running OS and return the appropriate file path delimiter.
    """
    return '\\' if os.name == 'nt' else '/'

# UPDATE NOTICE

import warnings
import requests
from packaging import version
from importlib.metadata import version as get_version

def update_notice():
    try:
        installed_version = get_version("vnstock")
        response = requests.get("https://pypi.org/pypi/vnstock3/json", timeout=5)
        response.raise_for_status()
        latest_version = response.json().get("info", {}).get("version")

        if latest_version and version.parse(installed_version) < version.parse(latest_version):
            warnings.warn(
                f"Phiên bản Vnstock Legacy ({installed_version}) bạn đang được sử dụng không được nâng cấp và sửa lỗi thêm.\n"
                f"Vui lòng sử dụng Vnstock thế hệ mới nhất ({latest_version}) với câu lệnh "
                f"'pip install vnstock3 --upgrade'.\n"
                "Từ 1/1/2025, vnstock3 sẽ được cài đặt khi sử dụng cú pháp `pip install vnstock` thay cho Vnstock Legacy hiện tại.\n"
                "Xem chi tiết tại: https://vnstocks.com/docs/tai-lieu/migration-chuyen-doi-sang-vnstock3",
                UserWarning
            )
    except requests.exceptions.RequestException:
        # Handle the exception, e.g., log the error or pass silently
        pass