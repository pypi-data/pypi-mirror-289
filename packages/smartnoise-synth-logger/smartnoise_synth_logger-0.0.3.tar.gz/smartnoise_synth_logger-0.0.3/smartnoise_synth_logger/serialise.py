import inspect
import json

import pkg_resources
from smartnoise_synth_logger.constants import (
    ANON_PARAM,
    JsonBodyKey,
    SSYNTH,
    SSYNTH_TRANSFORMER,
    Transformers,
)


def get_filtered_params(obj) -> dict:
    """Get filtered parameters based on the object's signature."""
    params = list(inspect.signature(type(obj)).parameters)
    return {k: v for k, v in vars(obj).items() if k in params}


def handle_chain_transformer(col_constraints: dict) -> dict:
    """Handle ChainTransformer-specific logic."""
    transformers = col_constraints.transformers
    return {
        JsonBodyKey.TYPE: SSYNTH_TRANSFORMER + Transformers.CHAIN,
        JsonBodyKey.PARAM: [
            {
                JsonBodyKey.TYPE: SSYNTH_TRANSFORMER + t.__class__.__name__,
                JsonBodyKey.PARAM: get_filtered_params(t),
            }
            for t in transformers
        ],
    }


def serialise_constraints(constraints: dict) -> str:
    """Serialise the SmartnoiseSynth constraints to send it through FastAPI

    Args:
        constraints (dict): a SmartnoiseSynth TableTransformer constraints

    Raises:
        ValueError: If the input argument is not a SmartnoiseSynth constraint.

    Returns:
        serialised (str): SmartnoiseSynth constraints as a serialised string
    """
    if not isinstance(constraints, dict):
        raise ValueError("Input constraints must be an instance of dict")

    json_body = {
        JsonBodyKey.MODULE: SSYNTH,
        JsonBodyKey.VERSION: pkg_resources.get_distribution(SSYNTH).version,
        JsonBodyKey.CONSTRAINTS: {},
    }

    for col_name, col_constraints in constraints.items():
        if isinstance(col_constraints, str):
            json_body[JsonBodyKey.CONSTRAINTS][col_name] = col_constraints
        else:
            operator_name = col_constraints.__class__.__name__

            if operator_name == Transformers.CHAIN:
                transformer_dict = handle_chain_transformer(col_constraints)
            elif operator_name == Transformers.ANONIMIZATION:
                transformer_dict = {
                    JsonBodyKey.TYPE: SSYNTH_TRANSFORMER
                    + Transformers.ANONIMIZATION,
                    JsonBodyKey.PARAM: {
                        ANON_PARAM: col_constraints.fake.__name__
                    },
                }
            else:  # default
                transformer_dict = {
                    JsonBodyKey.TYPE: SSYNTH_TRANSFORMER
                    + col_constraints.__class__.__name__,
                    JsonBodyKey.PARAM: get_filtered_params(col_constraints),
                }

            json_body[JsonBodyKey.CONSTRAINTS][col_name] = transformer_dict

    return json.dumps(json_body)
