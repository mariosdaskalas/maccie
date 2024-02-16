import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address.")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface. Please use --help for more information.")
    elif not options.mac:
        parser.error("Please specify a MAC. Please use --help for more information.")
    return options


def change(interface, mac):
    print(f"Changing MAC for {interface} to this {mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_mac(interface):
    result = subprocess.check_output(["ifconfig", options.interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("Could not read MAC.")


options = get_args()
current_mac = get_mac(options.interface)
print(f"Current MAC = {current_mac}")
change(options.interface, options.mac)

current_mac = get_mac(options.interface)
if current_mac == options.mac:
    print(f"MAC address was changed to {current_mac}.")
else:
    print(f"MAC address was not changed.")
