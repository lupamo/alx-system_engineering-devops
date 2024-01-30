#!/usr/bin/env ruby
#regular Expression matching Holberton name

arg = ARGV[0]

school = /School/

matches = arg.scan(school)
matches.each { |match| print match }
puts
