"""
Adiabatic system; KE+PE=constant
Equations derived from classical equations of motion which analyse a body with a changing velocity
G=gravitational constant
Rp=perigree height
Ra=apogee height
u=initial velocity
v=final velocity
Mp=mass primary, the big guy
Ms=mass secondary, the smaller guy
x=change in orbital height from perigee aka perigree change
"""
def altitude_change(G,Rp,v,u,Mp,Ms):
    return ((G/((((v*v)-(u*u))/(2*Mp))+(G/Rp))) - Rp)
def final_velocity(G,Rp,u,perigree_change,Mp):
    return ((2*G*Mp*( (1/(Rp+perigree_change))-(1/Rp) )) + (u*u))**0.5
def initial_velocity(G,Rp,u,perigree_change,Mp):
    return (((2*G*Mp*( (1/(Rp+perigree_change))-(1/Rp) )) - (v*v))*-1)**0.5
def mass_primary(v,u,G,max_perigree_change,Rp):
    return ((v*v)-(u*u))/(2*G*((1/(Rp+max_perigree_change))-(1/Rp)))
def eccentricity(max_perigree_change,Rp):
    return (max_perigree_change/2)/((max_perigree_change/2)+Rp)
def micro_altitude_change(current_altitude,u,micro_velocity_change,G,Mp):
    return (-1*current_altitude*current_altitude*u*micro_velocity_change/(G*Mp))
