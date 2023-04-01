# LOCAL
from File_man import File_Man

# LAB TOOLS
from brute_ssh import BruteSSH
from net_map import NetMap
from micro_scans import MicroScans
from meta_fab import MetaFab
from dir_scan import DirScan_

# SYS_BASE
import sys
import threading
import ipaddress
import time


class Da_Lab():
    def __init__(self, **kw):
        super(Da_Lab, self).__init__(**kw)
        self.FM         = File_Man()
        self.BSS        = BruteSSH()
        self.NM         = NetMap()
        self.MS         = MicroScans()
        self.META       = MetaFab()
        self.DiS        = DirScan_()


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
    # @ ? AmAss & GoBuster..
    # @ ? NET SNIFFER..
    # @ ? PACKET CAPTURE & DECRYPTION..
    # @ ? SQL INJECTOR..






    # ! # # # # # # # # ! # 
    # ! OPEN LAB TOOLS  ! #
    # ! # # # # # # # # ! # 
    def open_lab(self, prof_dir):
        prnt("[LET'S BEGIN LOOKING AT OUR LAB TOOLS]")






    #def some_stuf(self, prof_dir)


                # ! Don't Remember, LoL
                #try:
                #    ip_cat = ipaddress.ip_address(IP_)
                #    tar_type = "IP"
                #except:
                #    tar_type = "URL"
                #    print("[URL]->[DIR_SCAN]")
                #    self.DiS.dir_seach(target_, prof_dir)


#                time.sleep(1.5)
#                print("[COOL, NOW LET'S FIND OUT A BIT MORE ABOUT OUR TARGET]")
#                if "ERROR" not in str(prof_dir):
#                    print("[STRATING..]")
#                    time.sleep(1.5)
#                    tcp_ =self.start_scan(type_, IP_, port_, prof_dir)
#                    print("\n************\n[SCANS_COMPLETE]\n")
#                    print("[IP_TARGET]:", str(IP_))
#                    self.launch_att(l_host, l_port, IP_, prof_dir, type_, tcp_, thr_lvl)
#                    print("[_McBRETA_COMPLETED]\n!*!")
#                else:
#                    print(f"[E]:[SCAN_NOT_STARTED]")


