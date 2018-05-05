import time
import os
import pickle
from sys import stdout

class PROCESSES :
    def __init__(self):
        self.process_name=' '
        self.arrival_time=0
        self.brust_time=0
        self.waiting_time=0
        self.Turn_around_time=0
        
    def set_process_name(self,pname):
        self.process_name=pname
        
    def set_arrival_time(self,arival):
        self.arrival_time=arival
        
    def set_brust_time(self,brust):
        self.brust_time=brust
        
    def set_waiting_time(self,waiting):
        self.waiting_time=waiting
        
    def set_turnaround_time(self,turntime):
        self.Turn_around_time=turntime
        
    def get_process_name(self):
        return self.process_name

    def get_arrival_time(self):
        return self.arrival_time

    def get_brust_time(self):
        return self.brust_time

    def get_waiting_time(self):
        return self.waiting_time

    def get_turn_around_time(self):
        return self.Turn_around_time

#loading page function
stdout.write("LOADING")
def loading_page():
    for i in range(0,10):
        stdout.write("#")
        time.sleep(0.1)


def sjf():
        LIST_OF_PROCESSES=[]
        timer=0
        average_waiting_time=0
        average_turn_around_time=0
        #LOADING PAGE FUNCTION USED HERE
        loading_page()
        print('\n')
        os.system("cls")
        #GETTING COUNT FROM USER
        count=int(input("HOW MANY PROCESSES DO YOU WANT TO ENTER:"))
        LIST_OF_PROCESSES=[PROCESSES() for i in range (count)]
        QUEUE=[PROCESSES() for m in range (count)]
        print(' ')
        for i in range(count):
            process_name=str(input("ENTER THE NAME OF THE PROCESS HERE:"))
            brust_time=int(input("ENTER THE BRUST TIME OF THE PROCESS HERE:"))
            LIST_OF_PROCESSES[i].set_process_name(process_name)
            LIST_OF_PROCESSES[i].set_brust_time(brust_time)
    
            #SORTING ON THE BASIS OF BRUST TIME IN ASCENDING ORDER     
        for m in range(count):
           for n in range(count):
                if (LIST_OF_PROCESSES[m].get_brust_time() < LIST_OF_PROCESSES[n].get_brust_time()):
                    LIST_OF_PROCESSES[m],LIST_OF_PROCESSES[n]=LIST_OF_PROCESSES[n],LIST_OF_PROCESSES[m]
                    
                    
            
        for j in range(count):

            #CALCULATING AVERAGE WAITING TIME OF PROCESSES
            LIST_OF_PROCESSES[j].set_waiting_time(timer-LIST_OF_PROCESSES[j].get_arrival_time())
            timer+=LIST_OF_PROCESSES[j].get_brust_time()
            average_waiting_time+=LIST_OF_PROCESSES[j].get_waiting_time()
            
            
            #CALCULATING AVERAGE TURN AROUND TIME OF PROCESSES

            LIST_OF_PROCESSES[j].set_turnaround_time(LIST_OF_PROCESSES[j].get_brust_time()+LIST_OF_PROCESSES[j].get_waiting_time())
            average_turn_around_time+=LIST_OF_PROCESSES[j].get_turn_around_time()

        average_waiting_time=float(average_waiting_time)/count
        average_turn_around_time=float(average_turn_around_time)/count
        print("PROCESSNAME \t BURST TIME \t WAITING TIME \t TURN AROUND TIME")
        print("\n")
        # printing processes information
       
        for p in range(0,count):
             print(str(LIST_OF_PROCESSES[p].get_process_name())+" \t\t"+str(LIST_OF_PROCESSES[p].get_brust_time())+" \t\t"+str(LIST_OF_PROCESSES[p].get_waiting_time())+" \t\t"+str(LIST_OF_PROCESSES[p].get_turn_around_time()),end=' ')
             print("\n")
        print("AVERAGE WAITING TIME ="+str(average_waiting_time))
        print("AVERAGE TURN AROUND TIME ="+str(average_turn_around_time))
         
           
        
def main():
     sjf()
    
main()    
        
       
           
               
               
