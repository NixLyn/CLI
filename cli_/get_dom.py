# LOCAL
from File_man import File_Man

# SYS_BASE
from torrequest import TorRequest

import subprocess
from threading import Thread
import time
import socket
import struct
import textwrap
import requests


# ! USES:
# ! ~ AMASS
# ! ~ HTTP PROBE -> Prove the sub domain
# ! ~ GoBust each SubDomain
class The_Doms_():
    def __init__(self, **kw):
        super(The_Doms_, self).__init__(**kw)
        self.FM             = File_Man()



    # ? OBSOLETE, BUT EDUCATIONAL
    def mass_thread_(self, to_run):
        try:
            print("[STARTED THREAD FOR AMASS]")
            ret_mass = subprocess.getoutput(to_run)
            print(f"[RET_MASS]:~~[!]:[{str(ret_mass)}]")
            for i, sub_ in enumerate(ret_mass):
                print(f"[{str(i)}]:[{str(sub_)}]")
                r_ = requests.get(str(sub_))
                print(f"\n~~[REQUEST_RET]:\n ~~~[>> {str(r_)} <<]")

        except Exception as e:
            print(f"[E]:[THE_DOMS]:[AMASS_THREAD]:[{str(e)}]")





    # ! CHANGE IP FOR EACH PROBE
    def set_tor_(self,  uri_):
        try:
            with TorRequest() as tr:
                print("[CHANGING]:[IP]")
                tr.reset_identity()
                response =tr.get('http://ifconfig.me')
                if len(str(response)) < 20:
                    print(response.text)
                    probe_ = tr.get(f"{uri_}")
                    if probe_:
                        return probe_
                else:
                    print("[E]:[FETCHING]:[NEW_IP]")
            return
        except Exception as e:
            print(f"[E]:[{str(e)}]")
            return "ERROR"




 # TODO 
 # ! FIX GO-BUSTER ...



    # ! GoBuster -> URI_
    def buster_(self, uri_, prof_dir):
        try:
            l_dir = prof_dir+f"/busts_{uri}"
            self.FM.make_dir(l_dir)
            local_ = prof_dir+f"/busts_{uri}/subs.csv"
            self.FM.write_file(local_, "", "", "w+")
            if "https" not in uri_:
                to_run = f"gobuster dir -u https://{uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"
            else:
                to_run = f"gobuster dir -u {uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"
            print(f"[TO_BUST]:[{uri_}]")

            ret_bust = subprocess.getoutput(to_run)
            if "Error" not in str(ret_bust):
                print(f"[{str(uri_)}]:[BUST_COMPLETED]")
            else:
                print(f"[BUST_ERROR]:[{str(ret_bust)}]")
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[BUSTER_]:[{str(e)}]")


    # ? BUST EACH SUB 
    def da_subs_buster(self, sub_list, prof_dir):
        try:
            if len(sub_list) > 1:
                for i, p_ in enumerate(sub_list):
                    print(f"[BUSTING]:[{str(i)}]:[{str(p_)}]")
                    self.buster_(str(p_), prof_dir)
                # ? SAVE THE PROBED SUB DOMAINS
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[DA_SUBS]:[{str(e)}]")


    # ? CHECK ACTIVE SUBS
    def check_sub_act(self, sub_list):
        try:
            ret_list = []
            for j, sub_ in enumerate(sub_list):
                print(f"~[{j}]:[{str(sub_)}]")
                time.sleep(0.05)
            time.sleep(1.3)
            print("[SO NOW WE HAVE THIS LIST..]")
            time.sleep(1.3)
            print("[BUT WHAT CAN WE DO WITH IT..?]")
            time.sleep(1.3)
            print("[WELL FOR STARTERS, LET'S CHECK IF THEY ARE EVEN ACTIVE]")
            time.sleep(1.3)
            print("[TO DO SO, THERE ARE MANY TOOLS]")
            time.sleep(1.3)
            print("[BUT, THE EASIEST FOR MY LAZINESS]")
            time.sleep(1.3)
            print("[IS A SIMPLE 'GET' REQUEST]")
            time.sleep(1.3)
            print("[(since you know by now that I love the 'docs')]")
            print("[> https://requests.readthedocs.io/en/latest/user/quickstart/ <]")
            time.sleep(1.5)
            print("[THIS IS WHERE WE WILL ADD 'http://'...]")
            print("[(so if you added that before, it might cause problems here.. just type'n)]")
            time.sleep(1.3)
            re_ = input("[CONTINUE..?]")

            for j, sub_ in enumerate(sub_list):
                to_req = "https://"+str(sub_)
                print(f"~[{j}]:[{to_req}]")
                # ? DO A GET REQUEST TO TEST ACTIVITY
                try:
                    r = requests.get(to_req, timeout=5)
                    if r:
                        print(f"[RET_]:[{str(r)}]")
                    if "200" in r or "201" in r:
                        print(f"[ADDING]:[{sub_}]:[TO ACTIVE LIST]")
                        ret_list.append(str(sub_))
                except Exception as e:
                    print(f"[-]:[REQUEST_FAILED]:[{str(e)}]")

                time.sleep(0.5)
            if len(ret_list) > 1:
                print(f"[LOOKS LIKE WE HAVE FILTERED OUT ALL ACTIVE SUB_DOMAINS]")
            else:
                print("[LOOKS LIKE THERE AREN'T ANY ACTIVE SUB_DOMAINS..]")
            return ret_list
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[DA_MASS]:[{str(e)}]")
            return "ERROR"



    # ! AMASS + Bits_&_Pieces
    def da_mass(self, prof_dir, tar_, typ_):
        try:
            da_subs = ""
            subs_list = []
            clean_subs = []

            print(f'[DA_MASS]::\n    [!]:[TARGET_]:[{tar_}]\n    [!]:[TYPE_]:[{typ_}]\n')
            probes_ = []
            if "URL" in typ_:
                to_run = f"amass enum -d {tar_}"
                print(f'[WE CAN NOW RUN]:\n{to_run}')
                time.sleep(0.5)
                print("[THIS WILL TAKE SOME TIME..]")
                time.sleep(0.5)
                print("[SINCE THAT IS AN ANCIENT RELIC..]")
                time.sleep(0.5)
                mass_ = input("[DO YOU WANT TO RUN IT ANYWAY?]\n[y/N]: ")
                if "Y" in mass_.upper():
                    print("[OK.. ]")
                    print("[BUT WE'LL NEED TO USE MULTI_THREADING... CAUSE DAMN..]")
                    Thread(target=self.mass_thread_, args=(to_run,)).start()
                else:
                    print("..\n[GOOD]")
                time.sleep(0.3)
                print("[SO LET'S USE SOMETHING BETTER]")
                time.sleep(0.5)
                print("[SUBFINDER]")
                time.sleep(1)
                print("[(once again, reading the docs is always best practice)]")
                print("[(but since this is on github.. goodluck)]")
                print(">> subfinder -d <url> -silent")
                to_run_ = f"subfinder -d {tar_} -silent"
                print(f"[RUNNING]:[>{to_run_}<]")
                t_1 = time.time()
                try:
                    da_subs = ""
                    da_subs = subprocess.getoutput(to_run_)
                except Exception as e:
                    print(f"[E]:[SUBFINDER]:[SUB_PROCESS]:[>{str(e)}<]")
                t_2 = time.time()
                tot_ = t_2 - t_1
                tot_i = int(tot_)
                print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
                if da_subs:
                    print("[LET'S SEE WHAT WE FOUND]:")
                    subs_list = da_subs.split("\n")
                    clean_subs = self.check_sub_act(subs_list)
                    return clean_subs
                else:
                    print("** [LAB_FIRE]:[NO SUBS FOUND] **")
                    print("[(the next step might cause problems.. i think, :~| )]")
                    return ["error", "no", "subs"]




                #ret_mass = subprocess.getoutput(to_run)
                #print(f"[RET_MASS]:~~[!]:[{str(ret_mass)}]")
                #for i, sub_ in enumerate(ret_mass):
                #    print(f"[{str(i)}]:[{str(sub_)}]")
                #    r_ = requests.get(str(sub_))
                #    print(f"\n~~[REQUEST_RET]:\n ~~~[>> {str(r_)} <<]")
                #    # ? TOR PROBE EACH SUB DOMAIN
                #    #probe_ = self.set_tor_(str(sub_))
                #    #if probe_:
                #    #    print(f"[PROBE_]:[{str(probe_)}]")
                #    #    # ? APPEND TO A LIST
                #    #    probes_.append(probe_)
                #
                #
                ## ? run GoBuster on each sub domain
                #self.da_subs_(probes_, prof_dir)

        except Exception as e:
            print(f"[E]:[THE_DOMS]:[DA_MASS]:[{str(e)}]")
            return "ERROR"




    def start_here(self, prof_dir, target_, typ_):
        try:
            t_1 = time.time()
            print("[LAB TOOL @ HAND]:[GET_DOMS]")
            sub_list = self.da_mass(prof_dir, target_, typ_)
            t_2 = time.time()
            tot_ = t_2 - t_1
            tot_i = int(tot_)
            print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
            return "DONE"
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[START_FUNC]:[{str(e)}]")
            return "ERROR"




