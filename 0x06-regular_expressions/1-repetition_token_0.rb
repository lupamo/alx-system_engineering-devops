#!/usr/bin/env ruby
#repetition token

arg = ARGV[0]
t_repeat = /(hbtt){2,4}n/

matches = arg.scan(t_repeat)
matches.each { |match| print match }
puts
