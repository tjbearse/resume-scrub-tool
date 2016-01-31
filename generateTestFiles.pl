#!/usr/bin/env perl

mkdir 'test';
my @lines = ();
for my $i (0..10){
  my $filename = "test/$i.txt";
  `echo "name$1 email$i school$i 201$1" > $filename`;
  push(@lines, "first$i, last$i, $filename, email$i\n");
}

open(CSV, '>', 'test/resumes.csv') or die;
print CSV @lines;
close(CSV);
