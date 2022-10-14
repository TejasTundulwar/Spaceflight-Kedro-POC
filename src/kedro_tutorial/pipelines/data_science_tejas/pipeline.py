"""
This is a boilerplate pipeline 'data_science_tejas'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_model,train_model,split_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs= ["model_input_table","params:model_options"],
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
