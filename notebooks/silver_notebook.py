bronze_Path = "/Volumes/workspace/default/my_volume/Bronze_Layer"
silver_Path = "/Volumes/workspace/default/my_volume/Silver_layer"
#Read to BRONZE table
#------------------------
df_bronze=spark.read.format("delta")\
    .load(bronze_Path)


#CASTING DATA
#-----------------------------

from pyspark.sql.functions import col
df_casted=df_bronze.withColumn("id",col("id").cast("int"))\
    .withColumn("age",col("age").cast("int"))\
    .withColumn("salary",col("salary").cast("int"))


#DATA TRANSFORMATION
#-------------------------

from pyspark.sql.functions import when,col
df_silver=df_casted.dropna()\
    .filter(col("salary")>20000)\
    .filter(col("age")>18)\
    .withColumn("salaryFlag",when(col("salary")>100000,"6fig").otherwise("notEnough"))


#WRITE TO SILVER_LAYER
#------------------------------------

df_silver.write.format("delta")\
    .mode("overwrite")\
    .option("overwriteSchema","true")\
    .save(silver_Path)\
    



