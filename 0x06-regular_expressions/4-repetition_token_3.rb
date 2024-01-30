#!/usr/bin/env ruby
#the string should only contain t and b in the middle

repeat = /hbt*n/

matches = arg.scan(repeat)
matches.each { |match| print match }
puts
