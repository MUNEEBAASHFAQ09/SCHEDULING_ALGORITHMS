import time
import os
import pickle
from sys import stdout

class PROCESSES :
    def __init__(self):
        self.process_name=' '
        self.arrival_time=0
        self.brust_time=0
        self.remaining_brust_time=0
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

    def set_remaining_brust_time(self,remaining):
        self.remaining_brust_time=remaining
        
    def set_turnaround_time(self,turntime):
        self.Turn_around_time=turntime
        
    def get_process_name(self):
        return self.process_name

    def get_remaining_brust_time(self):
        return self.remaining_brust_time

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


def multi_level_queue():
    LIST_OF_PROCESSES=[]
    NEW_QUEUE_1=[]
    NEW_QUEUE_2=[]
    NEW_QUEUE_3=[]
    current_time=0
    average_waiting_time=0
    average_turn_around_time=0
    #LOADING PAGE USED HERE TO MAKE PROGRAM ATTRACTIVE
    loading_page()
    print('\n')
    os.system("clear")
    #TAKING COUNT FROM USER
    count=int(input("HOW MANY PROCESSES DO YOU WANT TO ENTER:"))
    LIST_OF_PROCESSES=[PROCESSES() for i in range (count)]

    print(' ')
    for i in range(count):
            process_name=str(input("ENTER THE NAME OF THE PROCESS HERE:"))
            arrival_time=int(input("ENTER THE ARRIVAL TIME OF THE PROCESS HERE:"))
            brust_time=int(input("ENTER THE BRUST TIME OF THE PROCESS HERE:"))
            

            LIST_OF_PROCESSES[i].set_process_name(process_name)
            LIST_OF_PROCESSES[i].set_brust_time(brust_time)
            LIST_OF_PROCESSES[i].set_arrival_time(arrival_time)
           
     #TAKING QUANTUM TIME FROM USER HERE       
    quantum_time_1=int(input("ENTER THE TIME SLICE FOR PROCESSES FOR FIRST QUEUE:"))
    quantum_time_2=int(input("ENTER THE TIME SLICE FOR PROCESSES FOR SECOND QUEUE:"))
    
    
    for m in range(count):
           for n in range(count):
                if (LIST_OF_PROCESSES[m].get_arrival_time()< LIST_OF_PROCESSES[n].get_arrival_time()):
                   LIST_OF_PROCESSES[m],LIST_OF_PROCESSES[n]=LIST_OF_PROCESSES[n],LIST_OF_PROCESSES[m]
               
    timer=LIST_OF_PROCESSES[0].arrival_time
    for i in range(len(LIST_OF_PROCESSES)):
        if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()<= quantum_time_1:
            NEW_QUEUE_1.append(LIST_OF_PROCESSES[i])

    for i in range(len(LIST_OF_PROCESSES)):
        if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()<=quantum_time_1 and LIST_OF_PROCESSES.get_brust_time()> quantum_time_2:
            NEW_QUEUE_2.append(LIST_OF_PROCESSES[i])

    for i in range(len(LIST_OF_PROCESSES)):
        if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()>quantum_time_2:
            NEW_QUEUE_3.append(LIST_OF_PROCESSES[i])
       #incrementing timer
    timer=timer+1
    while len(NEW_QUEUE_1)!=0 or len(NEW_QUEUE_2)!=0 or len(NEW_QUEUE_3)!=0:
        if len(NEW_QUEUE_1)==0:
            if len(NEW_QUEUE_2)==0:
                if NEW_QUEUE_3[0].get_burst_time()<=quantum_time:
                    found=0
                    while (found<NEW_QUEUE_3[0].get_burst_time()):
                         for i in range(len(LIST_OF_PROCESSES)):
                             if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_burst_time()<= quantum_time_1:
                                 NEW_QUEUE_1.append(LIST_OF_PROCESSES[i])
                         for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()<=quantum_time_1 and LIST_OF_PROCESSES.get_brust_time()> quantum_time_2:
                                      NEW_QUEUE_2.append(LIST_OF_PROCESSES[i])
                                  
                         for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()>quantum_time_2:
                                      NEW_QUEUE_3.append(LIST_OF_PROCESSES[i])
                                       #incrementing timer
                                      timer=timer+1
                                      found=found+1
        
                    
                    if (LIST_OF_PROCESSES[i].get_process_name()==NEW_QUEUE_2[0].get_process_name() and LIST_OF_PROCESSES[i].get_arrival_time==NEW_QUEUE_2[0].get_arrival_time()):
                                  LIST_OF_PROCESSES[i].set_waiting_time(timer-LIST_OF_PROCESSES[i].get_burst_time-LIST_OF_PROCESSES[i].get_arrival_time)
                                  LIST_OF_PROCESSES[i].set_turnaround_time(timer-process_LIST_OF_PROCESSES[i].get_arrival_time())
                                  NEW_QUEUE_1.remove(NEW_QUEUE_1[0])

                     #next queue
                    elif (NEW_QUEUE_3[0].get_burst_time()>quantum_time):
                        found=0
                        while found<quantum_time:
                          for i in range(len(LIST_OF_PROCESSES)):
                             if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_burst_time()<= quantum_time_1:
                                 NEW_QUEUE_1.append(LIST_OF_PROCESSES[i])
                             for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()<=quantum_time_1 and LIST_OF_PROCESSES.get_brust_time()> quantum_time_2:
                                      NEW_QUEUE_2.append(LIST_OF_PROCESSES[i])
                             for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()>quantum_time_2:
                                      NEW_QUEUE_3.append(LIST_OF_PROCESSES[i])
                                       #incrementing timer
                                      timer=timer+1
                                      found=found+1
   
                        m=LIST_OF_PROCESSES()
                        m.set_process_name(NEW_QUEUE_3[0].get_process_name())
                        m.set_arrival_time(NEW_QUEUE_3[0].get_arrival_time())
                        m.set_burst_time(NEW_QUEUE_3[0].get_brust_time())
                        m.set_burst_time(m.get_brust_time()-quantum_time())
                        NEW_QUEUE_3.append(m)
                        NEW_QUEUE_3.remove(NEW_QUEUE_3[0])
                    elif (NEW_QUEUE_2[0].get_burst_time()>quantum_time):
                        found=0
                        while (found<quantum_time):
                          for i in range(len(LIST_OF_PROCESSES)):
                             if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_burst_time()<= quantum_time_1:
                                 NEW_QUEUE_1.append(LIST_OF_PROCESSES[i])
                          for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()<=quantum_time_1 and LIST_OF_PROCESSES[i].get_brust_time()> quantum_time_2:
                                      NEW_QUEUE_2.append(LIST_OF_PROCESSES[i])
                       
                          
                          for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()>quantum_time_2:
                                      NEW_QUEUE_3.append(LIST_OF_PROCESSES[i])
                                       #incrementing timer
                                      timer=timer+1
                                      found=found+1
                        m=LIST_OF_PROCESSES()
                        m.set_process_name(NEW_QUEUE_2[0].get_process_name())
                        m.set_arrival_time(NEW_QUEUE_2[0].get_arrival_time())
                        m.set_burst_time(NEW_QUEUE_2[0].get_brust_time())
                        m.set_burst_time(m.get_brust_time()-quantum_time())
                        NEW_QUEUE_2.append(m)
                        NEW_QUEUE_2.remove(NEW_QUEUE_2[0])
                else :
                        if (NEW_QUEUE_1[0].get_burst_time()<=quantum_time):
                            found=0
                            while (found<NEW_QUEUE_1[0].get_burst_time()):
                                for i in range(len(LIST_OF_PROCESSES)):
                                    if (LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_burst_time()<= quantum_time_1):
                                        NEW_QUEUE_1.append(LIST_OF_PROCESSES[i])
                    
                                 
                                for i in range(len(LIST_OF_PROCESSES)):
                                    if (LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()<=quantum_time_1 and LIST_OF_PROCESSES[i].get_brust_time()> quantum_time_2):
                                        NEW_QUEUE_2.append(LIST_OF_PROCESSES[i])

            
                
                                for i in range(len(LIST_OF_PROCESSES)):
                                  if LIST_OF_PROCESSES[i].get_arrival_time()==timer and LIST_OF_PROCESSES[i].get_brust_time()>quantum_time_2:
                                      NEW_QUEUE_3.append(LIST_OF_PROCESSES[i])
                                       #incrementing timer
                                      timer=timer+1
                                      found=found+1
                        
                         
                                                         
                                  
                         
                        m=LIST_OF_PROCESSES()
                        m.set_process_name(NEW_QUEUE_1[0].get_process_name())
                        m.set_arrival_time(NEW_QUEUE_1[0].get_arrival_time())
                        m.set_burst_time(NEW_QUEUE_1[0].get_brust_time())
                        m.set_burst_time(m.get_brust_time()-quantum_time())
                        NEW_QUEUE_1.append(m)
                        NEW_QUEUE_1.remove(NEW_QUEUE_1[0])                      
                         

    
          #CALCULATING AVERAGE TURN AROUND AND AVERAGE WAITING TIME HERE        
            
    for j in range(count):
        average_waiting_time=float(average_waiting_time)/count      
        average_turn_around_time=float(average_turn_around_time)/count
         
       
           
    
    print("PROCESSNAME \t ARRIVAL TIME \t BURST TIME \t WAITING TIME \t TURN AROUND TIME")
    print("\n")
        # printing processes information
       
    for p in range(0,count):
       print(str(LIST_OF_PROCESSES[p].get_process_name())+" \t \t"+str(LIST_OF_PROCESSES[p].get_arrival_time())+" \t\t"+str(LIST_OF_PROCESSES[p].get_brust_time())+" \t\t"+str(LIST_OF_PROCESSES[p].get_waiting_time())+" \t\t"+str(LIST_OF_PROCESSES[p].get_turn_around_time()),end=' ')
       print("\n")
             
    print("AVERAGE WAITING TIME ="+str(average_waiting_time))
    print("AVERAGE TURN AROUND TIME ="+str(average_turn_around_time))
         
           
        
def main():

    #CALIING ROUND ROBIN FUNCTION MADE ABOVE
    os.system("cls")    
    multi_level_queue()
    
main()    
        
       

         
                    
                
    
    
   
       
        
