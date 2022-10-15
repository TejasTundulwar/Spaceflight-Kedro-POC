"""
This is a boilerplate pipeline 'data_science_tejas'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_model,train_model,split_data

def create_pipeline(**kwargs) -> Pipeline:
    ds_pipeline = pipeline([
        node(
            func=split_data,
            inputs= ["model_input_table_tejas","params:model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node_tejas",
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="regressor_tejas",
            name="train_model_node_tejas",
        ),
        node(
            func=evaluate_model,
            inputs=["regressor_tejas", "X_test", "y_test"],
            outputs=None,
            name="evaluate_model_node_tejas",
        ),
    ])

    ds_pipeline_1 = pipeline(
        pipe=ds_pipeline,
        inputs="model_input_table_tejas",
        namespace="active_modelling_pipeline",
    )
    ds_pipeline_2 = pipeline(
        pipe=ds_pipeline,
        inputs="model_input_table_tejas",
        namespace="candidate_modelling_pipeline",
    )
    return pipeline(
        pipe=ds_pipeline_1 + ds_pipeline_2,
        inputs="model_input_table_tejas",
        namespace="data_science_tejas",
    )
