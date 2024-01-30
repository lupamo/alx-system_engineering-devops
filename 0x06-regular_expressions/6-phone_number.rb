#!/usr/bin/env ruby
#regex for a 10 digit phone number

arg = ARGV[0]
number = /^[0-9]{10}$/

matches = arg.scan(number)
matches.each { |match| print match }
puts
