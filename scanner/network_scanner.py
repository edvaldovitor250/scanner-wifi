import nmap
from scanner.os_detector import OSDetector


class NetworkScanner:
    def __init__(self, network_range):
        self.network_range = network_range
        self.scanner = nmap.PortScanner()

    def scan(self):
        self.scanner.scan(hosts=self.network_range, arguments='-O')
        return self.scanner

    def process_results(self):
        results = []
        for host in self.scanner.all_hosts():
            if self.scanner[host].state() != 'up':
                continue
            running_str = ""
            device_type_str = ""
            if 'osmatch' in self.scanner[host] and self.scanner[host]['osmatch']:
                try:
                    osmatch = self.scanner[host]['osmatch'][0]
                    if 'osclass' in osmatch and osmatch['osclass']:
                        osclass = osmatch['osclass'][0]
                        running_str = osclass.get('osfamily', "")
                        device_type_str = osclass.get('type', "")
                except Exception:
                    pass
            os_detected = OSDetector.detect(running_str, device_type_str)
            results.append({'ip': host, 'os': os_detected})
        return results
