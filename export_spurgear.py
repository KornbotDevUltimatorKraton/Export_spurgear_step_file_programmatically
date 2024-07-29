import cadquery as cq
from cq_gears import SpurGear

# Define the spur gear parameters
module = 1.0
teeth_number = 19
width = 5.0
bore_d = 5.0

# Create the spur gear
spur_gear = SpurGear(module=module, teeth_number=teeth_number, width=width, bore_d=bore_d)
wp = cq.Workplane('XY').gear(spur_gear)

# Export the gear to an STL file
cq.exporters.export(wp, 'spur_gear.STEP')

# Alternatively, export the gear to a STEP file
# cq.exporters.export(wp, 'spur_gear.step')
