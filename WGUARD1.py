import subprocess

def configure_wireguard(interface, private_key, address, dns):
    try:
        subprocess.run(['sudo', 'wg', 'set', interface, 'private-key', private_key])
        subprocess.run(['sudo', 'ip', 'addr', 'add', address, 'dev', interface])
        subprocess.run(['sudo', 'ip', 'link', 'set', 'up', 'dev', interface])
        subprocess.run(['sudo', 'ip', 'route', 'add', 'default', 'via', address.split('/')[0], 'dev', interface])
        subprocess.run(['sudo', 'echo', f'nameserver {dns}', '>>', '/etc/resolv.conf'], shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

wireguard_private_key = "YOUR_WIREGUARD_PRIVATE_KEY"
wireguard_address = "ADAPTER ADDRESS
wireguard_dns = "10.2.0.2"
if configure_wireguard("wlan1", wireguard_private_key, wireguard_address, wireguard_dns):
    print("Wireguard interface configured successfully")
else:
    print("FAILED! YOU SUCK")
