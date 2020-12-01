import math
class coords:
    
    def __init__(self,a_yukari,a_saga,b_yukari,b_saga):
        """
        --------------
        Description
        --------------
        Consider : A----------------------B and the "açıklık açısı" of from A to B=t(a,b)  
        Input params:

        a_yukari: int
        a_saga: int
        b_yukari: int
        b_saga: int

        for_ex : example=coords(455496.970,4542850.180,455628.060,4542921.670)
                 example.aciklik_calc_T_a_b()

        Example Output:
        ---------------
        GRAD:Ta,b açıklık açısı =  68.21570440840306
        DERECE:Ta,b açıklık açısı =  61.39413396756275 
        ---------------
        """
        self.a_yukari=a_yukari
        self.a_saga=a_saga
        self.b_yukari=b_yukari
        self.b_saga=b_saga

    def aciklik_calc_T_a_b(self):
        dy=(self.b_yukari -self.a_yukari)
        dx=(self.b_saga - self.a_saga)
        T_a_b_in_grads=math.atan(dy/dx)*(200/math.pi)
        T_a_b_in_degrees=math.atan(dy/dx)*(180/math.pi)
        if dy<0 and dx<0:
            print("dy:eksi,dx:eksi")
            print("3.bölge!")
            Tab_in_grads = T_a_b_in_grads + 200
            Tab_in_degrees = T_a_b_in_degrees +180
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
            
        elif dy<0 and dx>0:
            print("dy:eksi,dx:artı")
            print("2.bölge")
            Tab_in_grads = T_a_b_in_grads - 200
            Tab_in_degrees = T_a_b_in_degrees - 180
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
            
            
        elif dy>0 and dx>0:
            print("dy:artı,dx:artı")
            print("1.bölge")
            Tab_in_grads = T_a_b_in_grads
            Tab_in_degrees = T_a_b_in_degrees
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
            
        elif dy>0 and dx<0:
            print("dy:artı,dx:eksi")
            print("4.bölge")
            Tab_in_grads = T_a_b_in_degrees + 400
            Tab_in_degrees = T_a_b_in_grads + 360
            print(f"GRAD:Ta,b açıklık açısı = {Tab_in_grads:.4f} grad")
            print(f"DERECE:Ta,b açıklık açısı = {Tab_in_degrees:.4f} degrees")
        
        return T_a_b_in_degrees,T_a_b_in_grads

            
example=coords(455496.970,4542850.180,455628.060,4542921.670)
example.aciklik_calc_T_a_b()
