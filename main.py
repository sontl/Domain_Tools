from use_inet import Inet
import pathlib
class Main:

    current_directory = str(pathlib.Path(__file__).parent.absolute()) 

    def start(self):
        #input file
        fin = open(self.current_directory + "/domain_list.txt", "rt")
        #for each line in the input file
        line_index = 0
        for line in fin:
            line = line.strip()
            index = line.find(".")
            domain = line[:index]
            tld = line[index+1:]
            self.check_status(domain, tld)
            line_index=line_index+1
        #close input and output files
        fin.close()

    def notification(self, domain, tld):
            # Call phone number to alert
            from notification import Notification
            notification = Notification(domain, tld)
            notification.call()

    def check_status(self, domain, tld):
        inet = Inet(domain, tld)

        print("------------ {}.{} ------------\n|".format(domain, tld) )
        status = inet.check_status()
        print("| INET status : {}".format(status))

        if(status == False):
            from use_digistar import Digistar
            digistar = Digistar(domain, tld)
            status = digistar.check_status()
            print("| DigiStar status: {}".format(status))
            
            if (status == False):
                from use_hostvn import HostVN
                hostvn = HostVN(domain, tld)
                status = hostvn.check_status()
                print("| HostVN status: {}".format(status))

                if (status == False):
                    from use_nhanhoa import NhanHoa
                    nhanhoa = NhanHoa(domain, tld)
                    status = nhanhoa.check_status()
                    print("| NhanHoa status: {}".format(status))

        if (status):
            self.notification(domain, tld)
        print("|\n----------------------------------------")

        

main = Main()
main.start()
#main.notification("code", "vn") # testing purpose

# log cron task
from datetime import datetime
myFile = open('~/log.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()))