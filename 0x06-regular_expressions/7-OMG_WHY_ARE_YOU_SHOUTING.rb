#!/usr/bin/env ruby
#regex matching only capital letters

arg = ARGV[0]
capital = /[A-Z]+/

matches = arg.scan(capital)
matches.each { |match| print match }
puts
