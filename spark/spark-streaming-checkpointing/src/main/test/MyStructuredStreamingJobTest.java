package com.limeguru.spark;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class MyStructuredStreamingJobTest {

    private MyStructuredStreamingJob myStructuredStreamingJob;

    @Before
    public void setUp() {
        myStructuredStreamingJob = new MyStructuredStreamingJob();
    }

    @Test
    public void testMyStructuredStreamingJob() throws StreamingQueryException {
        StreamingQuery query = myStructuredStreamingJob.startStructuredStreamingJob();

        Dataset<Row> output = myStructuredStreamingJob.getStreamingOutput();

        Assert.assertNotNull(output);
        Assert.assertEquals(4, output.columns().length);

        // Add more assertions based on expected output

        query.stop();
    }
}
