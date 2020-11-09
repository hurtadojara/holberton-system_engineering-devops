#!/usr/bin/env ruby
rex = /h\wn/
prex = ARGV[0].scan(rex).join
puts prex
