import argparse

def ArgumentParser():
    parser = argparse.ArgumentParser(prog='Shu', description='Otomatik reverse shell yükleyen bir program.', epilog='Github adresi: https://github.com/Narisca/Shu')

    parser.add_argument("--plugin",     "-x", help="Plugin dizininde ki içerik yönetim sistemlerini kullanabilirsiniz.", required=True, type=str, metavar="")
    parser.add_argument("--target-url", "-t", help="Hedef sitenin url adresini belirtmenizi sağlar.", required=True, type=str, metavar="")
    parser.add_argument("--username",   "-u", help="Kullanılacak kullanıcı adının belirtmenizi sağlar.", required=True, type=str, metavar="")
    parser.add_argument("--password",   "-p", help="Kullanılacak kullanıcı şifresini belirtmenizi sağlar.", required=True, type=str, metavar="")
    parser.add_argument("--local-host", "-L", help="Yerel ağ adresinizi belirtmenizi sağlar.", required=True, type=str, metavar="")
    parser.add_argument("--local-port", "-P", help="Dinlenilen port'u berlirtmenizi sağlar.", required=True, type=int, metavar="")

    return parser.parse_args()