#Bronze Data Ingestion
bronze_path = "/Volumes/workspace/default/my_volume/Bronze_Layer"
#Read to BRONZE table
#------------------------
countryDetails=spark.read.format("csv")\
        .option("header","true")\
        .option("inferSchema","true")\
        .option("mode","permissive")\
        .load("/Volumes/workspace/default/my_volume/Country.csv")


#write to BRONZE table
#-----------------------
countryDetails.write.format("delta")\
    .option("header","true")\
    .mode("overwrite")\
    .save(bronze_path)
