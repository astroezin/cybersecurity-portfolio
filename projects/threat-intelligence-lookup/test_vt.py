from api.virustotal import lookup_ip
from utils.formatter import format_virustotal_ip

result = lookup_ip("8.8.8.8")

print(format_virustotal_ip(result))
