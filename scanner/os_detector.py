import re

class OSDetector:
    @staticmethod
    def detect(running_str, device_type_str):
        mapping = {
            r'windows': 'Windows',
            r'android': 'Android',
            r'(ios|apple)': 'iOS',
            r'mac os': 'MacOS',
            r'linux': 'Linux'
        }
        r_str = running_str.lower()
        d_str = device_type_str.lower()
        for pattern, os_name in mapping.items():
            if re.search(pattern, r_str):
                if os_name == "Linux" and "phone" in d_str:
                    return "Android"
                return os_name
        return "Desconhecido"
