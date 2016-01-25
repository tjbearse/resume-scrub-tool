#!/usr/bin/env perl

mkdir 'test';
for my $i (0..10){
  `touch "test/$i.txt"`;
}
