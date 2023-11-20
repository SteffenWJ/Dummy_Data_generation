import random

#Todo Joint type and some sort of measurment data

class segment_dummy:
    def __init__(self):
        self.ID = self.generate_id()
        self.unit_data = self.generate_unit_data() #Height, Width, Length , mass
        self.unit_adjusted = [0.0,0.0,0.0,0.0]
        self.joint_type = []
        self.measurments_data = [] #Want to add this
        self.adjustments_data = []
        self.gab_data = [] #Would be left and right
        self.gab_accpatable = [False, False, False, False]
        self.point_cloud = None  
    
    def get_unit_data(self):
        return self.unit_data
    
    def get_measurements_data(self):
        return self.measurments_data
    
    def get_adjustments_data(self):
        return self.adjustments_data
    
    def get_gab_data(self):
        return self.gab_data
    
    def get_gab_accpatable(self):
        return self.gab_accpatable
    
    def generate_id(self):
        ID = "seg: "+str(random.randint(1000, 9999))
        return ID
    
    def generate_unit_data(self, width_low = 100, width_high = 300, length_low = 20, length_high = 40, height_low = 600, height_high = 700, mass_low = 20, mass_high = 20):
        width = random.randint(width_low, width_high)
        length = random.randint(length_low, length_high)
        height = random.randint(height_low, height_high)
        #mass = width*length*height*random.randint(mass_low, mass_high)
        mass = width*length*height
        return [width, length, height, mass]
    
    def take_measurements(self, width_mod = 10, length_mod = 5, height_mod = 20):
        width, length, height, mass = self.unit_data
        width += random.randint(-width_mod, width_mod)
        length += random.randint(-length_mod, length_mod)
        height += random.randint(-height_mod, height_mod)
        self.take_measurements = [width, length, height, mass]
        return [width, length, height, mass]
    
    def make_adjustment(self):
        width_dif = self.take_measurements[0] - self.unit_data[0]
        length_dif = self.take_measurements[1] - self.unit_data[1]
        height_dif = self.take_measurements[2] - self.unit_data[2]
        #mass_dif = self.take_measurements[3] - self.unit_data[3] #Should haven no change
        self.unit_adjusted[0] = self.unit_data[0] + width_dif
        self.unit_adjusted[1] = self.unit_data[1] + length_dif
        self.unit_adjusted[2] = self.unit_data[2] + height_dif
        #self.unit_adjusted[3] = self.unit_data[3] + mass_dif
        return self.unit_adjusted
    
    def measure_gap_data(self, threshold = 10, low_lim = 2 , high = 11):
        top_left = random.randint(low_lim, high)
        top_right = random.randint(low_lim, high)
        bottom_left = random.randint(low_lim, high)
        bottom_right = random.randint(low_lim, high)
        if top_left > threshold:
            self.gab_accpatable[0] = False
        else:
            self.gab_accpatable[0] = True
        if top_right > threshold:
            self.gab_accpatable[1] = False
        else:
            self.gab_accpatable[1] = True
        if bottom_left > threshold:
            self.gab_accpatable[2] = False
        else:
            self.gab_accpatable[2] = True
        if bottom_right > threshold:
            self.gab_accpatable[3] = False
        else:
            self.gab_accpatable[3] = True
        self.gab_data = [top_left, top_right, bottom_left, bottom_right]
        return self.gab_data, self.gab_accpatable
        
        

    
    
bla = segment_dummy()

print(bla.measure_gap_data())
