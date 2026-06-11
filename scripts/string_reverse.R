#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1) {
  stop("Usage: Rscript scripts/string_reverse.R <text>", call. = FALSE)
}

chars <- strsplit(args[1], split = "")[[1]]
cat(paste(rev(chars), collapse = ""), "\n")
