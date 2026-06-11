#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 2) {
  stop("Usage: Rscript scripts/add_numbers.R <a> <b>", call. = FALSE)
}

a <- suppressWarnings(as.numeric(args[1]))
b <- suppressWarnings(as.numeric(args[2]))

if (is.na(a) || is.na(b)) {
  stop("Both arguments must be numeric.", call. = FALSE)
}

cat(a + b, "\n")
