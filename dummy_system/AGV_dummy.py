import time
import random

#Todo:
# Add comments
# Add more states
# Add more tasks

class AGV_dummy:
    def __init__(self , waypoint_list_given = None):
        self.op_state = None
        self.task_list = ["Transporting", "Charging", "Idle", "Waiting", "Placing Segment", "Getting Segment"]
        self.current_task = self.task_list[3] #Set to idel from start
        print(waypoint_list_given)
        if waypoint_list_given == None:
            print("Random path generated")
            self.waypoint_list = self.generate_random_path()
        else:
            self.waypoint_list = waypoint_list_given
        self.current_path = self.calculate_path_steps(self.waypoint_list) #This is the first step list
        self.where_on_path = 0 #Internal Ticker to keep a eye on where we are
        self.forward_bool = True
        self.current_postion = self.waypoint_list[0]
        self.next_waypoint = self.waypoint_list[1]
        self.current_speed = None #Will not be used as random numbers
        self.current_battery = None #Extra
        self.current_wait_time_start = None
        self.current_wait_time_end = None 
        self.API = None
        self.token = None
        self.error_log = []
        self.error_types = [] #Need to be added
        self.start_time = time.time()
    
    def generate_random_path(self, length = 5, low_span = 0, high_span = 9):
        the_path = []
        which = random.randint(0, 1)
        x = random.randint(low_span, high_span)
        y = random.randint(low_span, high_span)
        for _ in range(0, length):
            which = random.randint(0, 1)
            if which == 0:
                x = random.randint(low_span, high_span)
                the_path.append([x,y])
                #which = 1
            else:
                y = random.randint(low_span, high_span)
                the_path.append([x,y])
                #which = 0
        return the_path
                
    def calculate_path_steps(self, the_path):
        path_steps = []
        for i in range(0, len(the_path)-1):
            start = the_path[i]
            end = the_path[i+1]
            x1, y1 = start
            x2, y2 = end
            dx = (x2 - x1) / 10
            dy = (y2 - y1) / 10

            for j in range(1, 11):
                x = x1 + j * dx
                y = y1 + j * dy
                path_steps.append([x, y])
        return path_steps
    
    def get_current_task(self):
        return self.current_task
    
    def get_waypoint_list(self):
        return self.waypoint_list
    
    def get_path(self):
        return self.current_path
    
    def next_step(self):
        if self.forward_bool == True:
            self.current_postion = self.current_path[self.where_on_path]
            self.where_on_path += 1
            if self.where_on_path == len(self.current_path)-1:
                self.forward_bool = False
        else:
            self.current_postion = self.current_path[self.where_on_path]
            self.where_on_path -= 1
            if self.where_on_path == 0:
                self.forward_bool = True
    
    def get_current_position(self):
        return self.current_postion
    
    def get_where_on_path(self):
        #Becaus the logic is one step a head this most be done Easy solution
        if self.forward_bool == True:
            return self.where_on_path-1
        else:
            return self.where_on_path+1


