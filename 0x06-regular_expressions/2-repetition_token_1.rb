#!/usr/bin/env ruby
rex = /hb?tn/
prex = ARGV[0].scan(rex).join
puts prex
