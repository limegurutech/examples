package com.limeguru.spark;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructType;
import org.apache.spark.sql.functions;

public class MyStructuredStreamingJob {

	public static void main(String[] args) throws StreamingQueryException {

		SparkSession spark = SparkSession.builder().appName("MyStructuredStreamingJob").master("local[*]")
				.getOrCreate();
		Dataset<Row> df = spark.readStream().format("kafka").option("kafka.bootstrap.servers", "127.0.0.1:9092")
				.option("subscribe", "mytopic").option("includeHeaders", "true").load();
		df = df.selectExpr("CAST(topic AS STRING)", "CAST(partition AS STRING)", "CAST(offset AS STRING)", "CAST(value AS STRING)");

		StructType emp_schema = new StructType().add("name", DataTypes.StringType).add("age", DataTypes.StringType)
				.add("country", DataTypes.StringType);
		
		df = df.select(functions.col("topic"), functions.col("partition"), functions.col("offset"), functions.from_json(functions.col("value"), emp_schema).alias("data"));
		df = df.select("topic", "partition", "offset", "data.*");

		StreamingQuery query = df.writeStream().format("console").option("truncate", "False").start();
		query.awaitTermination();

	}

}
