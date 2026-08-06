from api.abuseipdb import lookup_ip
from utils.formatter import format_abuseipdb_ip

result = lookup_ip("8.8.8.8")

print(format_abuseipdb_ip(result))
