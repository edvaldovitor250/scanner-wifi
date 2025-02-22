class OSDetector:
    @staticmethod
    def detect(running_str, device_type_str):
        running_str = running_str.lower()
        device_type_str = device_type_str.lower()
        if "windows" in running_str:
            return "Windows"
        elif "android" in running_str:
            return "Android"
        elif "ios" in running_str or "apple" in running_str:
            return "iOS"
        elif "mac os" in running_str:
            return "MacOS"
        elif "linux" in running_str:
            if "phone" in device_type_str:
                return "Android"
            return "Linux"
        else:
            return "Desconhecido"
