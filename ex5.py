name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # Inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky try and get it exactly right.
print "If i add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)
