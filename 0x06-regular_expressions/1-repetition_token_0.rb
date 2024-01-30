#!/usr/bin/env ruby
#repetition token

arg = ARGV[0]
t_repeat = /hbt{2,5}n/

matches = arg.scan(t_repeat)
matches.each { |match| print match }
puts
