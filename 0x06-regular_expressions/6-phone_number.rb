#!/usr/bin/env ruby
rex = /^\d{10}$/
prex = ARGV[0].scan(rex).join
puts prex
