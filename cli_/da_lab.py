# LOCAL
from File_man import File_Man

# LAB TOOLS
from brute_ssh import BruteSSH
from net_map import NetMap
from micro_scans import MicroScans
from meta_fab import MetaFab
from dir_scan import DirScan_
from get_dom import The_Doms_

# SYS_BASE
import subprocess
import sys
import threading
import ipaddress
import time
import requests


class Da_Lab():
    def __init__(self, **kw):
        super(Da_Lab, self).__init__(**kw)
        self.FM         = File_Man()
        self.BSS        = BruteSSH()
        self.NM         = NetMap()
        self.MS         = MicroScans()
        self.META       = MetaFab()
        self.DiS        = DirScan_()
        self.TD         = The_Doms_()


    # ? SCANS

    # ! BASE SCANS
    # ! THREAD TO FINISH BEFORE NEXT ONE CAN START
    def start_scan(self, type_, target_, port_, file_dir):
        IP_ = ""
        try:
            IP_ = ""
            if type_ == "URL":
                print("[TYPE_URL]...\n[FETCHING_IP]...")
                # ! NS_LOOK_UP -> IP_
                IP_ = self.MS.dis_lookup(target_)
                print(f"[IP_FOUND]:[>{str(IP_)}<]")
                print(f"[STARTING_]:[MICRO_SCANS]:[&&]:[NET_MAP]")
            try:
                # @ BASE SCANNS
                # ! ALL_MICRO_SCANS
                self.MS.all_scans(type_, target_, file_dir)
                # ! NET_MAP_URL -> TCP_LIST
                tcp_ = self.NM.og_scan(type_, target_, file_dir, " ", port_)
                return tcp_
            except Exception as e:
                print(f"[E]:[STD_SCANS]:[>{str(e)}<]")
            print("[SCANS_COMPLETED]")

        except Exception as e:
            print(f"[E]:[START_SCAN]:[>{str(e)}<]")
            return ["ERROR", "OG_SCAN", "START_SCAN"]


    # ? EDUCATIONAL ATTACKS

    # ! LOW_GRADE_BRUTES
    def base_brutes(self, type_, target_,  file_dir):
        IP_ = ""
        try:
            IP_ = ""
            if type_ == "URL":
                print("[TYPE_URL]...\n[FETCHING_IP]...")
                # ! NS_LOOK_UP -> IP_
                IP_ = self.MS.dis_lookup(target_)
                print(f"[IP_FOUND]:[>{str(IP_)}<]")
                print(f"[STARTING_]:[BASE_BRUTES]")

            # INITS
            try:
                # @ BASE BRUTES
                # ! HYDRA
                self.hydra_ = threading.Thread(target=self.BSS.go_hydra, args=(IP_, file_dir, ))
                # !MEDUSA
                self.medusa_ = threading.Thread(target=self.BSS.go_medusa, args=(IP_, file_dir, ))
            except Exception as e:
                print(f"[E]:[BRUTE_TRHEADS]:[>{str(e)}<]")

            # RUN_THREADS
            try:
                print("[$]:[HYDRA]:[START]")
                self.hydra_.start()
                print("[$]:[MEDUSA]:[START]")
                self.medusa_.start()
            except Exception as e:
                print(f"[E]:[START_THREADS]:[>{str(e)}<]")
            print("[BRUTES_LAUNCHED]")
            return True
        except Exception as e:
            print(f"[E]:[BASE_BRUTES]:[>{str(e)}<]")
            return False



    # ? BASIC EXPLOIT METHODS

    # ! META_SPLOIT_ATTACK
    def launch_att(self,l_host, l_port, target_, prof_dir, type_, tcp_, thr_):
        try:
            to_brute = input("[LAUNCH_BRUTES]:[y/N]?:")
            if "Y" in to_brute.upper():
                self.base_brutes(type_, target_, prof_dir)

            to_breta = input("[LAUNCH_McBrEtA_]:[Y/n]:")
            if "N" not in to_breta.upper():
                IP_ = self.MS.dis_lookup(target_)
                print("\n[IP_TAGERT]:",str(target_))
                # ! META_SPLOIT
                self.META.set_meta_stack_(l_host, l_port, target_, prof_dir, type_, tcp_, thr_)
                # ! WATCH_FILE ! TODO
                print("[McBRETA_RUN_COMPLETE]")
        except Exception as e:
            print(f"[E]:[McBRETA]:[MAIN]:[>{str(e)}<]")


    # TODO:
    # @ ? NET_MAP : 
        # @ ~ PORTS
        # @ ~ ENCRYPTS
        # @ ~ SERVICES + VERSIONS
    # @ ? AmAss & GoBuster..
    # @ ? NET SNIFFER..
        # @ ~ PACKET CAPTURE
        # @ ~ PACKET DECRYPTION..
    # @ ? SQL INJECTOR..



    # ? STEP_ONE_A : BASIC NMAP
    def step_one_a(self, target_, typ_, prof_dir):
        try:
            port_list = []
            da_ports_ = []
            ports_ = ""
            print("[IF YOU ARE NOT FAMILIAR WITH 'nmap']")
            time.sleep(1)
            print("[IT IS HIGHLY SUGGESTED TO READ UP IT]")
            print("[THERE ARE MULTIPLE SOURCES ON THE WEB]")
            print("[BUT IT IS ALWAYS BEST PRACTICE TO START WITH THE 'docs']")
            print("[> https://nmap.org <]")
            print("[(if you are using the git clone version of this, have a look at 'net_map.py')]")
            print("[IF YOU ARE FAMILIAR WITH 'nmap']")
            print("[THEN YOU CAN ADD SOME FLAGS]")
            print("[BY DEFAULT WE JUST USE '-A']")
            print("[(please use spaces to seperate the flags, same as you would in a terminal cmd)]")
            print("[(some eg.):")
            print(" ~ [(-v = Verbose)]")
            time.sleep(0.2)
            print(" ~ [(-Pn = quite port scan)]")
            time.sleep(0.2)
            print(" ~ [(-F (Fast (limited port) scan))]")
            time.sleep(0.2)
            print(" ~ [(-sV (Version detection))]")
            time.sleep(0.2)
            print(" ~ [(-O: Enable OS detection ) <- (requires root)]")
            time.sleep(0.2)
            print(" ~ [(-6: Enable IPv6 scanning) <- (usually needed when using 'https://')]")
            flags_ = input("[FLAGS]:(optional): ")
            time.sleep(0.5)
            try:
                print("[THIS MIGHT TAKE SOME TIME, PATIENCE IS KEY..]")
                t_1 = time.time()
                ports_ = ""
                ports_ = self.NM.og_scan(typ_, target_, prof_dir, flags_, "params_")
                t_2 = time.time()
                tot_ = t_2 - t_1
                tot_i = int(tot_)
                print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
                print("[IF THAT WORKED, WE SHOULD HAVE A LIST OF OPEN PORTS]")
                if ports_:
                    da_ports_ = ports_.split(",")
                    for i, p_ in enumerate(da_ports_):
                        if p_:
                            port_list.append(str(p_))
                            print(f"[{str(i)}]:[{str(p_)}]")
                else:
                    print("[CHECK THE PROFILE DIR TO SEE IF THERE'S ANY CLUE AS TO WHAT WENT WRONG]")
                
            except Exception as e:
                print(f"[E]:[Da_Lab]:[S_1]:[OG_SCAN]:[{str(e)}]")

        except Exception as e:
            print(f"[E]:[Da_Lab]:[STEP_ONE]:[{str(e)}]")


    # ? STEP_ONE_B : ENUM NMAP


    # ? STEP_TWO_A : BREAK DOMAINS
    def step_two_a(self, target_, typ_, prof_dir):
        try:
            print("[TO BREAK THE DOMAINS OPEN]")
            time.sleep(1.3)
            print("[WE WILL NEED TO FIRST FIND ALL 'SUB' DOMAINS]")
            time.sleep(1.3)
            print("[(eg. services.domain.com)]")
            time.sleep(1.3)
            print("[THEN WE CAN START BUSTING EACH DOMAIN's DIRECTORY]")
            time.sleep(1.3)
            print("[STARTING 'GET_DOM' TOOL]")
            doms_ = self.TD.start_here(target_, typ_, prof_dir)
            if "DONE" in doms_:
                print("[NOW THAT WE'VE BUSTED ALL THE DOMAINS]")
                time.sleep(1.3)
                print("[LET'S SEE WHAT'S THERE]")
                print("[IF ALL WENT WELL, THERE SHOULD BE SOME NEW STUFF IN THE PROFILE DIRECTORY :) ]")
            if "ERROR" in doms_:
                print("[LAB_FIRE]:[GET_DOMS]")

        except Exception as e:
            print(f"[E]:[Da_Lab]:[STEP_THREE]:[{str(e)}]")



    # ! # # # # # # # # ! # 
    # ! OPEN LAB TOOLS  ! #
    # ! # # # # # # # # ! # 
    def open_lab(self, target_, typ_, prof_dir):
        try:
            os.system('cls||clear')
            print("\n")
            print("@ ! ^^^^^^^^^^^^^^ ! @")
            print("@ !  LAB NOW OPEN  ! @")
            print("@ ! vvvvvvvvvvvvvv ! @")
            print("\n")

            print("[LET'S BEGIN LOOKING AT OUR LAB TOOLS]")
            time.sleep(1)
            print("[FIRST LET'S GET SOME INFO ON OUR TARGET]")
            time.sleep(1)
            print(f"[SINCE WE ARE WORKING WITH]:[{typ_}]")
            time.sleep(1)
            if "URL" in typ_:
                time.sleep(0.5)
                print(f"[IT MEANS WE HAVE SOME ACTIVE RECON TOOLS WE CAN USE]:")
                time.sleep(0.5)
                print(f"~[NMAP]")
                time.sleep(0.5)
                print(f"~[CURL]")
                time.sleep(0.5)
                print(f"~[CEWL]")
                time.sleep(0.5)
                print(f"~[WHOIS]")
                time.sleep(0.5)
                print(f"~[AMASS]")
                time.sleep(0.5)
                print(f"~[GOBUSTER]")
                time.sleep(0.6)
                print("~[AND MORE, WHICH WE'LL GET INTO LATER]")
            if "IP" in typ_:
                print("[CAN'T REALLY DO MUCH WITH ONLY THIS]")
                time.sleep(1.2)
                print("[BUT WE WILL GET TO THAT IN A LATER UPDATE]")

            print("\n[AS ANY SELF RESPECTING PEN_TESTER/HACKER WILL KNOW]")
            time.sleep(1)
            print("[THE FIRST PLACE TO START IS ALWAYS >> NMAP << ]")
            time.sleep(1)

            # ! STEP_ONE_A : NMAP 
            self.step_one_a(target_, typ_, prof_dir)

            # TODO 
            # ! STEP_ONE_B : GET_ENCRYPTS
            print("[NMAP PROVIDES LOTS OF INFO ON A TARGET]")
            time.sleep(1)
            print("[ONE OF THEM BEING ENCRYPTION METHODS BEING USED]")
            time.sleep(1)
            print("[BUT WE WILL GET BACK TO THAT LATER..]")


            # ! STEP_TWO : DOMAIN BREAKER
            print("\n[NOW LET'S FIND ALL SUB DOMAINS AND THEIR SUB DIRECTORIES]")

            time.sleep(0.2)
            ready_ = input("[READY FOR STEP TWO?]:[Y/n]: ")
            if "N" not in str(ready_).upper():
                self.step_two_a(prof_dir, target_, typ_)


            # ! STEP_THREE : 

        except Exception as e:
            print(f"[E]:[Da_Lab]:[OPEN_LAB]:[{str(e)}]")



                # ! Don't Remember, LoL
                #try:
                #    ip_cat = ipaddress.ip_address(IP_)
                #    tar_type = "IP"
                #except:
                #    tar_type = "URL"
                #    print("[URL]->[DIR_SCAN]")
                #    self.DiS.dir_seach(target_, prof_dir)

