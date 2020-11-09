#!/usr/bin/env ruby
rex = /hbt{2,5}n/
prex = ARGV[0].scan(rex).join
puts prex
