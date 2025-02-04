# Widget Dictionary
widget_json = {
    "widgets": []
}

# CLUSTER LEVEL METRICS
ClusterHeading = {
    "height": 1,
    "width": 24,
    "y": 0,
    "x": 0,
    "type": "text",
    "properties": {
        "markdown": "# Cluster Level Metrics"
    }
}
DBClusterReplicaLagMaximum = {
    "height": 7,
    "width": 12,
    "y": 3,
    "x": 0,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "DBClusterReplicaLagMaximum", "DBClusterIdentifier"]
        ],

    }
}
DatabaseCursorsTimedOut = {
    "height": 7,
    "width": 12,
    "y": 3,
    "x": 12,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "DatabaseCursorsTimedOut", "DBClusterIdentifier"]
        ],
        "period": 300
    }
}
VolumeWriteIOPS = {
    "height": 7,
    "width": 6,
    "y": 12,
    "x": 0,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "VolumeWriteIOPs", "DBClusterIdentifier"]
        ],
    }
}
VolumeReadIOPS = {
    "height": 7,
    "width": 6,
    "y": 12,
    "x": 6,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "VolumeReadIOPs", "DBClusterIdentifier"]
        ],
    }
}
Opscounter = {
    "height": 7,
    "width": 12,
    "y": 12,
    "x": 12,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "OpcountersInsert", "DBClusterIdentifier"],
            [".", "OpcountersDelete", ".", "."],
            [".", "OpcountersUpdate", ".", "."],
            [".", "OpcountersQuery", ".", "."]
        ],
        "period": 300,
        "title": "Opcounters"
    }
}
# INSTANCE LEVEL METRICS
InstanceHeading = {
    "height": 1,
    "width": 24,
    "y": 20,
    "x": 0,
    "type": "text",
    "properties": {
        "markdown": "# Instance Level Metrics"
    }
}
CPUUtilization = {
    "height": 7,
    "width": 8,
    "y": 21,
    "x": 0,
    "type": "metric",
    "properties": {
        "metrics": [
            ["AWS/DocDB", "CPUUtilization", "DBInstanceIdentifier"],
            ["..."],
            ["..."]
        ],
        "view": "timeSeries",
                "stacked": False,
                "title": "CPU Utilization",
                "period": 300,
                "stat": "Average",
                "yAxis": {
                    "left": {
                        "max": 100,
                        "min": 0
                    }
                }
            }
        }
IndexBufferCacheHitRatio = {
    "height": 7,
    "width": 8,
    "y": 30,
    "x": 8,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "IndexBufferCacheHitRatio", "DBInstanceIdentifier"],
            ["..."],
            ["..."]
        ],
        "period": 300,
        "yAxis": {
            "left": {
                "max": 100,
                "min": 0
                    }
                },
        "title": "Index Buffer Cache Hit Ratio"
            }
        }
BufferCacheHitRatio = {
    "height": 7,
    "width": 8,
    "y": 30,
    "x": 0,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "BufferCacheHitRatio", "DBInstanceIdentifier"],
            ["..."],
            ["..."]
        ],
        "period": 300,
        "yAxis": {
            "left": {
                "max": 100,
                "min": 0
                    }
                },
                "title": "Buffer Cache Hit Ratio"
            }
        }
DatabaseCursors = {
    "height": 7,
    "width": 8,
    "y": 21,
    "x": 16,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "DatabaseCursors", "DBInstanceIdentifier"],
            ["..."],
            ["..."]
        ],
    }
}
DatabaseConnections = {
    "height": 7,
    "width": 8,
    "y": 21,
    "x": 8,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "DatabaseConnections", "DBInstanceIdentifier"],
            ["..."],
            ["..."]
        ],
    }
}
FreeableMemory = {
    "height": 7,
    "width": 8,
    "y": 30,
    "x": 16,
    "type": "metric",
    "properties": {
        "sparkline": True,
        "view": "timeSeries",
        "metrics": [
            ["AWS/DocDB", "FreeableMemory", "DBInstanceIdentifier"],
            ["..."],
            ["..."]
        ],
        "title": "Freeable Memory",
        "period": 300,
        "stacked": False,
        "yAxis": {
            "left": {
                "min": 0
                    }
                }
            }
        }
DocsInserted = {
            "height": 6,
            "width": 6,
            "y": 38,
            "x": 0,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": False,
                "metrics": [
                    ["AWS/DocDB", "DocumentsInserted", "DBInstanceIdentifier"],
                    ["..."],
                    ["..."]
                ],
                "title": "Documents Inserted"
            }
        }
DocsDeleted = {
            "height": 6,
            "width": 6,
            "y": 38,
            "x": 6,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": False,
                "metrics": [
                    ["AWS/DocDB", "DocumentsDeleted", "DBInstanceIdentifier"],
                    ["..."],
                    ["..."]
                ],
                "title": "Documents Deleted"
            }
        }
DocsUpdated = {
            "height": 6,
            "width": 6,
            "y": 38,
            "x": 12,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": False,
                "metrics": [
                    ["AWS/DocDB", "DocumentsUpdated", "DBInstanceIdentifier"],
                    ["..."],
                    ["..."]
                ],
                "title": "Documents Updated"
            }
        }
DocsReturned = {
            "height": 6,
            "width": 6,
            "y": 38,
            "x": 18,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": False,
                "metrics": [
                    ["AWS/DocDB", "DocumentsReturned", "DBInstanceIdentifier"],
                    ["..."],
                    ["..."]
                ],
                "title": "Documents Returned"
            }
}

# BACKUP AND STORAGE METRICS
BackupStorageHeading = {
    "height": 1,
    "width": 24,
    "y": 44,
    "x": 0,
    "type": "text",
    "properties": {
        "markdown": "# Backup and Storage Metrics"
    }
}
BackupRetentionPeriodStorageUsed = {
    "height": 7,
    "width": 8,
    "y": 45,
    "x": 8,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "BackupRetentionPeriodStorageUsed", "DBClusterIdentifier"]
        ],
    }
}
TotalBackupStorageBilled = {
    "height": 7,
    "width": 8,
    "y": 45,
    "x": 16,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "TotalBackupStorageBilled", "DBClusterIdentifier"]
        ],
    }
}
VolumeBytesUsed = {
    "height": 7,
    "width": 8,
    "y": 45,
    "x": 0,
    "type": "metric",
    "properties": {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/DocDB", "VolumeBytesUsed", "DBClusterIdentifier"]
        ],
    }
}

# ADDITIONAL HELP METRICS
metricHelp = {
            "height": 2,
            "width": 12,
            "y": 0,
            "x": 0,
            "type": "text",
            "properties": {
                "markdown": "### Metrics Overview\nLearn more about metric information by visiting the Amazon DocumentDB Metrics section [here](https://docs.aws.amazon.com/documentdb/latest/developerguide/cloud_watch.html#cloud_watch-metrics_list)\n"
            }
        }
bestPractices = {
            "height": 2,
            "width": 12,
            "y": 0,
            "x": 12,
            "type": "text",
            "properties": {
                "markdown": "### DocumentDB Specialist Optimization Tips\nLearn how to optimize your workload by visiting the DocDB Specialist recommended guidelines [here](https://docs.aws.amazon.com/documentdb/latest/developerguide/best_practices.html)"
            }
        }
