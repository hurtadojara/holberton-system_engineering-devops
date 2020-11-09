#!/usr/bin/ruby
rex = /[H][o][l][b][e][r][t][o][n]/
prex = ARGV[0].scan(rex).join
puts prex
