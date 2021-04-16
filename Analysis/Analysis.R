wilcox.test(res$maxNestedBlocks_x, res$lambdasQty_y, paired=TRUE,exact = F,conf.level = 0.99)# <0.05 :signifant else not
cliff.delta(res$lambdasQty_x, res$lambdasQty_y, paired=TRUE,conf.level = 0.99)#negligable;small;medium ou large
boxplot(res$maxNestedBlocks_x, res$maxNestedBlocks_y)
install.packages("effsize")
library(effsize)

boxplot(res$maxNestedBlocks_x, res$maxNestedBlocks_y,col= c("darkgray","blue"),show.names=F)
legend("top",fill = c("blue","darkgray"),legend = c("After Refactoring", "Before Refactoring"),cex=0.9)