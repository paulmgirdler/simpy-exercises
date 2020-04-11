#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:52:20 2020
@author: paul

Car example

Covers:

- Introduction

Scenario:
  A car will alternately drive and park for a while.
  
- Model parking and driving time.
- Model distance driven.
  
"""
# Define variables
SIM_TIME = 100 # Time in hours
SPEED = 60 # Speed in mph
ODOMETER = 0

import simpy

def car(env):
    while True:
        # Start parking
        print('Start parking at %d' % env.now)
        parking_duration = 5 # Time in hours
        yield env.timeout(parking_duration)
        
        # Start driving
        print('Start driving at %d' % env.now)
        trip_duration = 5 # Time in hours
        global ODOMETER 
        ODOMETER += 60*5 # Distance drive
        print('Distance driven %d miles' % ODOMETER)
        yield env.timeout(trip_duration)
        
# Setup and start the simulation
print('Car')
env = simpy.Environment()
env.process(car(env))
env.run(until=SIM_TIME)