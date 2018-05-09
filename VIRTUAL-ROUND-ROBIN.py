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


def virtual_round_robin():
    LIST_OF_PROCESSES=[]
    WAITING_QUEUE=[]
    AUXILARY_QUEUE=[]
    clock_tick=0
    average_waiting_time=0
    average_turn_around_time=0
    loading_page()
    print('\n')
    os.system("cls")
    count=int(input("HOW MANY PROCESSES DO YOU WANT TO ENTER:"))
    

    LIST_OF_PROCESSES=[PROCESSES() for i in range (count)]
    WAITING_QUEUE=[PROCESSES()]
    AUXILARY_QUEUE=[PROCESSES()]
    print(' ')
    for i in range(count):
            process_name=str(input("ENTER THE NAME OF THE PROCESS HERE:"))
            arrival_time=int(input("ENTER THE ARRIVAL TIME OF THE PROCESS HERE:"))
            brust_time=int(input("ENTER THE BRUST TIME OF THE PROCESS HERE:"))
            
            clock_tick=LIST_OF_PROCESSES[0].get_arrival_time()
       
            LIST_OF_PROCESSES[i].set_process_name(process_name)
            LIST_OF_PROCESSES[i].set_brust_time(brust_time)
            LIST_OF_PROCESSES[i].set_arrival_time(arrival_time)
            
    quantum_time=int(input("ENTER THE TIME SLICE FOR PROCESSES:"))
    input1=int(input("ENTER THE I/O TIME FOR PROCESSES:"))
    #LIST_OF_PROCESSES.set_quantum_time(quantum_time)
    for m in range(0,count):
           for n in range(0,count-1):
                if (LIST_OF_PROCESSES[n].get_arrival_time()> LIST_OF_PROCESSES[n+1].get_arrival_time()):
                   LIST_OF_PROCESSES[n],LIST_OF_PROCESSES[n+1]=LIST_OF_PROCESSES[n+1],LIST_OF_PROCESSES[n]
               
    for i in range(0,count):
        LIST_OF_PROCESSES[i].set_remaining_brust_time(LIST_OF_PROCESSES[i].get_brust_time())
    
    #NOW KEEP TRAVERSING PROCESSES IN ROUND ROBIN WAY

    while(1):
        found=1
        for i in range (0,count):
             # checking boundary case
             if(LIST_OF_PROCESSES[i].get_remaining_brust_time()>0):
                  #showing a pending process
                  found=0
                 
                 
                 
                  # some quantum time left
                  
                  if (LIST_OF_PROCESSES[i].get_remaining_brust_time()>quantum_time):
                      clock_tick=clock_tick+quantum_time
                      LIST_OF_PROCESSES[i].set_remaining_brust_time(LIST_OF_PROCESSES[i].get_remaining_brust_time()-quantum_time)
                  
                  
                  else:
                    clock_tick=clock_tick+LIST_OF_PROCESSES[i].get_remaining_brust_time()
                    LIST_OF_PROCESSES[i].set_waiting_time(clock_tick-LIST_OF_PROCESSES[i].get_brust_time()-LIST_OF_PROCESSES[i].get_arrival_time())
                    LIST_OF_PROCESSES[i].set_turnaround_time(clock_tick-LIST_OF_PROCESSES[i].get_arrival_time())
                    #if no remaining quantum time left processes finished execution

                    LIST_OF_PROCESSES[i].set_remaining_brust_time(0)
                      

                    #comparing the processes with the first process in the ready or new queue
             for i in range(len(LIST_OF_PROCESSES)):
                    if(LIST_OF_PROCESSES[i].get_process_name()==WAITING_QUEUE[0].get_process_name() and LIST_OF_PROCESSES[i].get_arrival_time()==WAITING_QUEUE[0].get_arrival_time()):
                        LIST_OF_PROCESSES[i].set_waiting_time(clock_tick-(LIST_OF_PROCESSES[i].get_brust_time()+LIST_OF_PROCESSES[i].get_arrival_time()))
                        LIST_OF_PROCESSES[i].set_turnaround_time(clock_tick-LIST_OF_PROCESSES[i].get_arrival_time())
                        clock_tick=clock_tick+1
                        found=found+1
                       
                    temp_obj=PROCESSES()
                    temp_obj.process_name=WAITING_QUEUE[0].process_name
                    temp_obj.arrival_time=WAITING_QUEUE[0].arrival_time
                    temp_obj.brust_time=WAITING_QUEUE[0].brust_time
                    temp_obj.brust_time=WAITING_QUEUE[0].brust_time-quantum_time
                    WAITING_QUEUE.append(temp_obj) 
                    WAITING_QUEUE.remove(temp_obj)
          
                 
            #QUANTUM TIME GREATER SO APPENDING THE PROCESS AND THEN REMOVING FIRST ONE           
        
             for i in range(len(LIST_OF_PROCESSES)):
                 if(LIST_OF_PROCESSES[i].get_arrival_time()==clock_tick and LIST_OF_PROCESSES[i].get_brust_time()>quantum_time):
                     WAITING_QUEUE.append(LIST_OF_PROCESSES[i])
                     clock_tick=clock_tick+1
                     found=found+1
                 temperory=PROCESSES()
                 temperory.process_name=WAITING_QUEUE[0].process_name
                 temperory.arrival_time=WAITING_QUEUE[0].arrival_time
                 temperory.brust_time=WAITING_QUEUE[0].brust_time
                 temperory.brust_time=WAITING_QUEUE[0].brust_time-quantum_time
                 WAITING_QUEUE.append(temperory)           
                 WAITING_QUEUE.remove(WAITING_QUEUE[0])
                 
                         
            #IF THE PROCESSES ENTERED BY THE USER ARE COMPLETED THEN FININISHED LOOP BREAK BECAUSE LENGTH OF PROCESSES FININSHED
          
        if(found==1):
          break
                    
            
    for j in range(count):
         #calculating turn around time
                average_waiting_time=average_waiting_time+LIST_OF_PROCESSES[j].get_waiting_time()
                average_turn_around_time+=LIST_OF_PROCESSES[j].get_turn_around_time() 
 
       
              
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
    
    os.system("cls")    
    virtual_round_robin()
    
main()    
        
       

         
                    
                
    
    
   
       
        

