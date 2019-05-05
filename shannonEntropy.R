install.packages("data.table")
library(data.table)

rm(list=ls())
setwd('/Users/oliviawaring/Documents/Documents-Rupert’sMacBookPro/Harvard_MIT Year Two/Spring Term Courses/Physical Immunology/Term Paper/PhonemicFitness')

MSA = data.table(read.table("sequences4analysis.txt", fill = TRUE))
cols=names(MSA)
d = sapply(MSA,customTable)
newDT = data.table(columnName=names(d),values=d)

write.csv(newDT, file='processed.csv')

customTable = function(vector){
  a = table(vector)
  b = paste(names(a),unname(a), collapse = ';')
  return(b)
}