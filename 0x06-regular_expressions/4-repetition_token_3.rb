#!/usr/bin/env ruby
rex = /hbt*n/
prex = ARGV[0].scan(rex).join
puts prex
