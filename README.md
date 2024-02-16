This is a Python CLI program dedicated for changing the MAC address for various interfaces.

```shell
git clone https://github.com/mariosdaskalas/maccie
cd maccie
python3 main.py --help
```

or a one-liner command.

```shell
git clone https://github.com/mariosdaskalas/maccie && cd maccie && python3 main.py --help
```

```shell
Notice: ⚠️
You need to run the program with root privileges.
```

```shell
To change the MAC address of eth0 interface to 00:11:22:33:44:55
python3 main.py -i eth0 -m 00:11:22:33:44:55
```