#promtping the user
mass=input("what is the mass? ")
velocity=input("what is the velocity? ")
#def fuction that has the equation in it but also calling varibles out side it 
def Kinetic_energy(mass,velocity):
    #I don't know if i can put the full equation "Ke=1/2Mass*Velocity^2 in one line so i order them "
    num1=int(mass)/2
    num2=int(velocity)**2
    num3=num1*num2
    print(num3)
Kinetic_energy(mass,velocity)

   
