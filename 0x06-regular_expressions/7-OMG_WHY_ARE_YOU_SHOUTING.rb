#!/usr/bin/env ruby
rex = /[A-Z]/
prex = ARGV[0].scan(rex).join
puts prex
