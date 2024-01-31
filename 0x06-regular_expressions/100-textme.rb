#!/usr/bin/env ruby
#regex to match text files

arg = ARGV[0]
text = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

matches = arg.scan(text)
matches.each { |match| print match }
puts
