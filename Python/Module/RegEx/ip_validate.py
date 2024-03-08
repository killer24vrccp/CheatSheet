from colorama import Fore, Style
import re

info_color, info = (Fore.LIGHTGREEN_EX, "[!]")
question_color, question = (Fore.LIGHTBLUE_EX, "[?]")
invalid_color, invalid = (Fore.RED, "[^]")


def ip_validation(ip_address):
    parts = ip_address.split('.')
    if len(parts) == 4:
        for part in parts:
            if not part.isdigit() or int(part) < 0 or int(part) > 255:
                return f"{invalid_color}{invalid}{Style.RESET_ALL} Invalid IP address\nMake sure you entered a valid IP address with the format: {Fore.RED}xxx.xxx.xxx.xxx!"
        return f"{info_color}{info}{Style.RESET_ALL} Valid IP address"
    else:
        return f"{invalid_color}{invalid}{Style.RESET_ALL} Invalid IP address\nMake sure you entered a valid IP address with the format: {Fore.RED}xxx.xxx.xxx.xxx!"


def main(ip_address):
    non_alpha_num = re.findall(r'\W', ip_address)
    if any(non_alpha_num) and "." not in ip_address:
        print(f"{invalid_color}{invalid}{Style.RESET_ALL} The IP address should only contain digits and dots.")
    else:
        print(ip_validation(ip_address))


if __name__ == "__main__":
    my_ip = input(f"{question_color}{question}{Style.RESET_ALL} Enter your IP address: ")
    main(my_ip)