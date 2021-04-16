library(beanplot)

beanplot(PUM$cbo_x,PUM$cbo_y,PUM$wmc_x,PUM$wmc_y, PUM$dit_x,PUM$dit_x,PUM$rfc_x,PUM$rfc_y,PUM$lcom_x,PUM$lcom_y,PUM$nosi_x,PUM$nosi_y,PUM$loc_x,PUM$loc_y,PUM$variablesQty_x,PUM$variablesQty_y,   side= "both",col = list("darkgray","blue"), ll = 0.01, names=c("cbo","wmc","dit","rfc","lcom","nosi","loc","vqty"), cex=0.7, ylim = c(0,350), overallline = "median", las = 1, bw="nrd0")
  
legend("topright",fill = c("darkgray","blue"),legend = c("Before","After"), cex=0.8)

median(PUM$lcom_x)
median(PUM$lcom_y)