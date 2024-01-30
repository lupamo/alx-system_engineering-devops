#!/usr/bin/env ruby
#the string should only contain t and b in the middle

repeat = /\bh(?:t|b)+n\b/

matches = arg.scan(repeat)
matches.each { |match| print match }
puts
