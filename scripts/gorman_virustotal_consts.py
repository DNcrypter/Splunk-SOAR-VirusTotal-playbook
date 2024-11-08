
# configuration file

[ 
    {
        "data_path": "summary.total_objects",
        "data_type": "numeric"
    },
    {
        "data_path": "summary.total_objects_successful",
        "data_type": "numeric"
    },
    {
        "data_path": "action_result.data.*.positives",
        "data_type": "numeric",
        "column_name": "positives",
        "column_order": 1
    },
    {
        "data_path": "action_result.data.*.total",
        "data_type": "numeric",
        "column_name": "total",
        "column_order": 2
    },


"render": {
    "type": "table"
}

]
