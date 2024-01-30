#!/usr/bin/env ruby
#repetition of t character from one
arg = ARGV[0]

t_repeat = /hb[t]+n/

matches = arg.scan(t_repeat)
matches.each { |match| print match }
puts
