from sys import argv #load sys module to get arguments

script, filename = argv

txt = open(filename) # open a file using argument name

print "Here's your file %r:" % filename #print file name
print txt.read() #Output file to stdout

print "Type the file name again:"
file_again = raw_input("> ") # input new file name

txt_again = open(file_again) # open again

print txt_again.read() # output again
