class HelpTool():
    def __init__(self):
        self.tools = """
1) Port scan
2) Directory search
3) SSH Login
4) SSH Brute Force
5) Search exploit
6) View Exif data
7) Enum4linux (Get info about target)
8) Hping3 (Dos - DDos)
9) Ssh2john (Convert ssh hash to john hash)
10) John (Crack hash)

11) rlwrap (For better terminal)
12) Python shell/bash
13) Linpeas (Privilege escalation)

14) gtfobins (Documentary for privilege escalation)

15) Searchsploit (Search exploit)
16) smbmap -H 1.2.3.4 (List share folders)
17) smbget (Download file from smb server)
18) arp-scan -l (List devices in network)

99) Exit


"""

        self.portScan = """
Port scan tools: nmap 
nmap usage: nmap <paramaters> <website address or ip address>  |  nmap -sS -sV 127.0.0.1
"""

        self.directorySearch = """
Directory search tools: dirb, gobuster, dirsearcher (https://github.com/Lessyzz/Directory-Searcher)

dirb usage: dirb <ip address> <wordlist>  |  dirb http://127.0.0.1/ /usr/share/wordlists/dirb/common.txt

gobuster usage: gobuster -e -u http://127.0.0.1/ -w /usr/share/wordlists/dirb/common.txt

dirsearcher usage: dirsearcher.py -u <url> -t <threads> -w <wordlist>
"""

        self.sshLogin = """
SSH Login tools: ssh
ssh usage: ssh <Username>@<Server IP>  |  ssh lessy@127.0.0.1
"""

        self.sshBruteForce = """
SSH Burte force tools: Hydra
hydra usage: hydra -l <username> -P <path to wordlist> <IP> ssh  |  hydra -l admin -P wordlist.txt 127.0.0.1 ssh              
"""

        self.searchExploit = """
Search exploit tools: searchsploit 
searchsploit usage: searchsploit apache 2.4.49
Also you need to update searchsploit, for update > searchsploit -u
"""

        self.viewExifData = """
Exif data viewer tools: exiftool, strings
exiftool usage: exiftool image.png
strings usage: string image.png        
"""

        self.enum4linux = """
enum4linux usage: enum4linux -a 127.0.0.1        
"""

        self.hping3 = """
hping3 usage: hping3 -S --flood -V 127.0.0.1
Another dos - ddos tools: Slowloris, Hulk, HOIC, LOIC, Tor's Hammer
        """

        self.ssh2john = """
ssh2john usage: ssh2john id_rsa > hash.txt
        """

        self.john = """
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
        """

        self.rlwrap = """
rlwrap nc -lnvp 4444
        """

        self.pythonsell = """
python -c 'import pty; pty.spawn("/bin/bash")'
        """

        self.linpeas = """
linpeas.sh
        """

        self.searchExploit = """
searchsploit apache 2.4.49
        """

        self.smbmap = """
smbmap -H 1.2.3.4
        """

        self.smbget = """
smbget -R smb://10.20.30.40/sambashare -a
        """

        self.arpscan = """
arp-scan -l
        """

        self.run()

    def getInput(self):
        number = input("> ")

        match number:
            case "1":
                print(self.portScan)
            case "2":
                print(self.directorySearch)
            case "3":
                print(self.sshLogin)
            case "4":
                print(self.sshBruteForce)
            case "5":
                print(self.searchExploit)
            case "6":
                print(self.viewExifData)
            case "7":
                print(self.enum4linux)
            case "8":
                print(self.hping3)
            case "9":
                print(self.ssh2john)
            case "10":
                print(self.john)
            case "11":
                print(self.rlwrap)
            case "12":
                print(self.pythonsell)
            case "13":
                print(self.linpeas)
            case "15":
                print(self.searchExploit)
            case "16":
                print(self.smbmap)
            case "17":
                print(self.smbget)
            case "18":
                print(self.arpscan)
                
            case "99":  
                exit()


    def run(self):
        while True:
            print(self.tools)
            self.getInput()


HelpToolRun = HelpTool()