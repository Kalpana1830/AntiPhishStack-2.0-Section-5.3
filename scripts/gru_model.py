"""Standalone Keras GRU/attention model from report section 5.3."""

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Bidirectional, GRU, Dense, Attention


def build_gru_model(vocab_size, max_len):
    """Build the report's sequence-to-sequence representation model."""
    inputs = Input(shape=(max_len,))
    x = Embedding(vocab_size, 128)(inputs)
    x = Bidirectional(GRU(64, return_sequences=True))(x)
    context = Attention()([x, x])
    x = Dense(64, activation="relu")(context)
    return Model(inputs, x)
