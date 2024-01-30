#!/usr/bin/env ruby
#repetition token ignored

arg = ARGV[0]
repeat = //h[b]?tn/

matches = arg.scan(repeat)
matches.each { |match| print match }
puts
