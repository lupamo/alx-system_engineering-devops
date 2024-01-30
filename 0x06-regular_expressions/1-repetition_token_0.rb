#!/usr/bin/env ruby
#repetition token

arg = ARGV[0]
t_repeat = /hbtt+n/

matches = arg.scan(t_repeat)
matches.each { |match| print match }
puts
