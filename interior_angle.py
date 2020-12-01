import math
class coords:
           
    def __init__(self,from_yukari,from_saga,to_yukari,to_saga):
        """
        --------------
        Description
        --------------
        Consider : A----------------------B and the "interior angle" of from A to B=t(a,b)  
        Input params:

        from_yukari: int
        from_saga: int
        to_yukari: int
        to_saga: int

        for_ex : example=coords(455496.970,4542850.180,455628.060,4542921.670)
                 example.aciklik_calc_T_a_b()

        Example Output:
        ---------------
        GRAD:Ta,b açıklık açısı =  68.21570440840306
        DERECE:Ta,b açıklık açısı =  61.39413396756275 
        ---------------
        """
        self.from_yukari=from_yukari
        self.from_saga=from_saga
        self.to_yukari=to_yukari
        self.to_saga=to_saga
        self.interior_angle_grad=0
        self.interior_angle_degrees=0
    
    def aciklik_calc_T_a_b(self):
        dy=(self.to_yukari -self.from_yukari)
        dx=(self.to_saga - self.from_saga)
        interior_angle_grad=math.atan(dy/dx)*(200/math.pi)
        interior_angle_degrees=math.atan(dy/dx)*(180/math.pi)
        
        if dy<0 and dx<0:
            print("dy:eksi,dx:eksi")
            print("AREA 3")
            Tab_in_grads = interior_angle_grad + 200
            Tab_in_degrees = interior_angle_degrees + 180
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
            
        elif dy<0 and dx>0:
            print("dy:eksi,dx:artı")
            print("AREA 4")
            Tab_in_grads = interior_angle_grad + 400
            Tab_in_degrees = interior_angle_degrees + 360
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
                 
        elif dy>0 and dx>0:
            print("dy:artı,dx:artı")
            print("AREA 1")
            Tab_in_grads = interior_angle_grad
            Tab_in_degrees = interior_angle_degrees
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
            
        elif dy>0 and dx<0:
            print("dy:artı,dx:eksi")
            print("AREA 2")
            Tab_in_grads = interior_angle_grad + 200
            Tab_in_degrees = interior_angle_degrees + 180
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
        
        self.interior_angle_grad = Tab_in_grads
        self.interior_angle_degrees = Tab_in_degrees
            

        
tfrom1to2=coords(322701.642,4507492.016,322132.043,4507178.876)
tfrom1to2.aciklik_calc_T_a_b()
print(tfrom1to2.interior_angle_grad-tfrom1to2.interior_angle_degrees)


