#!/usr/bin/python3
import sys

usage = """
./vieworbit.py <keplerian|vector>
"""

if len(sys.argv) != 2:
    print(usage)
    exit()

if sys.argv[1] == 'keplerian':
    e = float(input("Eccentricity: "))      
    a = float(input("Semi-Major: "))      
    i = float(input("Inclination: "))
    o = float(input("Long Asc Node: "))
    w = float(input("Perigee: "))
    f = float(input("True anomaly: "))

    
elif sys.argv[1] == 'vector':
    ######## GET STARTING ORBIT FROM STATE VECTOR ########
    io.recvuntil(b'Pos (km):   [')
    position = [float(i) for i in io.recvuntil(b']')[:-1].decode('ascii').split(', ')]

    io.recvuntil(b'Vel (km/s): [')
    velocity = [float(i) for i in io.recvuntil(b']')[:-1].decode('ascii').split(', ')]

    io.recvuntil(b'Time:       ')
    time = io.recvuntil(b'.000').decode('ascii')
    time = Time(f"{time[:10]}T{time[11:]}") #correct format

    transfer_orbit = Orbit.from_vectors(Earth,
            position * units.km,
            velocity * units.km / units.s,
            epoch=time)

    print(f'Got challenge state vector:\n\
    Position: {transfer_orbit.r}\n\
    Velocity: {transfer_orbit.v}\n\
    Time:     {transfer_orbit.epoch}\n\
    R(ICRF):  {norm(transfer_orbit.r.value)}\n')

    e = orbit.ecc                   #eccentricity
    a = orbit.a                     #semi-major axis
    i = orbit.inc.to(units.deg)     #inclination
    o = orbit.raan.to(units.deg)    #longitude ascending node
    w = orbit.argp.to(units.deg)    #argument of perigee
    f = orbit.nu.to(units.deg)      #true anomaly
else:
    print(usage)
    exit()





print(f'Resolved keplerian elements:\n\
Eccentricity:  {e}\n\
Semi-Major:    {a}\n\
Inclination:   {i}\n\
Longitude Asc: {o}\n\
Arg Perigee:   {w}\n\
True Anomaly:  {f}\n')