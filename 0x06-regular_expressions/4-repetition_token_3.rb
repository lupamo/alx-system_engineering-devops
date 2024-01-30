#!/usr/bin/env ruby
#the string should only contain t and b in the middle

repeat = /hb[t]*n/

matches = arg.scan(repeat)
matches.each { |match| print match }
puts
