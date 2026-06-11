#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1) {
  stop("Usage: Rscript scripts/is_even.R <number>", call. = FALSE)
}

number <- suppressWarnings(as.integer(args[1]))

if (is.na(number)) {
  stop("Argument must be an integer.", call. = FALSE)
}

cat(if (number %% 2 == 0) "even" else "odd", "\n")
