#!/usr/bin/python3
from pwn import *
from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit, angles
import numpy as np


host = "matters_of_state.satellitesabove.me"
port = 5300
ticket = b"ticket{victor234519juliet3:GPaKWC8OIYDU7cP1AT-rDrc02fMDUPsWTqzun-bIQ02UxQawSREtsUiLD4M5VZ-wsw}"


io = remote(host, port)
io.recvuntil(b"Ticket please")
io.sendline(ticket)
io.recvuntil(b'Position: X,Y,Z \n')


a = 63780.0 * u.km #km, semi-major
e = 0.3 * u.one #ecc
i = 63 * u.deg #inclination, deg
raan = 25 * u.deg #lon asc node, deg
M = 10 * u.deg #mean anomaly, deg

if e < 1:
    M = (M + np.pi * u.rad) % (2 * np.pi * u.rad) - np.pi * u.rad 
    nu = angles.E_to_nu(angles.M_to_E(M, e), e) 
elif e == 1: 
    nu = angles.D_to_nu(angles.M_to_D(M)) 
else: 
    nu = angles.F_to_nu(angles.M_to_F(M, e), e) 

w = 78 * u.deg #arg peri, deg


orb = Orbit.from_classical(Earth, a, e, i, raan, w, nu)

print(orb.r)
print(orb.v)


io.interactive()


