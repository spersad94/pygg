from pyplot import *

# Example using diamonds dataset (comes with ggplot2)
p = ggplot('diamonds', aes('carat', y='price'))
g = geom_point() + facet_wrap(None, "color")
(p+g).save("test1.pdf")


# Example using data from database table.  
p = ggplot('data', aes(x='epoch', y='temp', color='sensor'))
prefix = data_sql("intel", "SELECT epoch, temp, sensor, 1 AS color FROM readingssmall")
(p+g).save("test2.pdf", prefix=prefix)

p = ggplot('data', aes(x='epoch', y='temp', color='sensor'))
prefix = data_sql("intel", "SELECT epoch, temp, sensor, 1 AS color FROM readingssmall")
(p+g).save("test2.pdf", prefix=prefix)

p = ggplot('data', aes('x', 'y'))
prefix = data_py({'x': range(10), 'y': range(10, 20)})
(p+g).save("test3.pdf", prefix=prefix, quiet=True)


