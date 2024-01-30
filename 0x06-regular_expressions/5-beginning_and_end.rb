#!/usr/bin/env ruby
#not accepting strings starting h and ending with n

arg = ARGV[0]
repeat = /^h.n$/

matches = arg.scan(repeat)
matches.each { |match| print match }
puts
