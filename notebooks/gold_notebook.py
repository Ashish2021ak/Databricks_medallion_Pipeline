#GOLD layer Read and Write
#---------------------------------------------------
silver_path="/Volumes/workspace/default/my_volume/Silver_layer"
gold_path="/Volumes/workspace/default/my_volume/Gold_layer"
# read data from Silver Notebook
#-----------------------------------

df_silver=spark.read.format("delta")\
    .load(silver_path)


# Business analysis ready Transformation
#---------------------------------------------

from pyspark.sql.functions import col,count,avg
df_gold=df_silver.groupBy("salaryFlag")\
    .agg(count("*").alias("employees_count"))


#Write to GOLD LAYER
#-------------------------
df_gold.write.format("delta")\
    .mode("overwrite")\
    .option("overwriteSchema","true")\
    .save(gold_path)

display(df_gold)

