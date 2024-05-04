import tensorflow as tf
import json

from sklearn.model_selection import train_test_split


def train_model(dataset: str, model_filename: str) -> None:
    """
    Trains a model for detecting some shit people
    :param dataset: Path to dataset
    :param model_filename: Output file name
    :return: None
    """

    BUFFER_SIZE = 10000
    BATCH_SIZE = 64

    with open(dataset, "r") as f:
        data = json.load(f)

    texts = []
    labels = []
    for category, examples in data.items():
        examples = [e for e in examples if e is str]
        texts.extend(examples)
        labels.extend([int(category)] * len(examples))

    train_texts, test_texts, train_labels, test_labels = train_test_split(
        texts, labels, test_size=0.2, random_state=42
    )

    train_dataset = tf.data.Dataset.from_tensor_slices((train_texts, train_labels))
    test_dataset = tf.data.Dataset.from_tensor_slices((test_texts, test_labels))

    train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
    test_dataset = test_dataset.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

    VOCAB_SIZE = 100000
    encoder = tf.keras.layers.TextVectorization(max_tokens=VOCAB_SIZE)
    encoder.adapt(train_dataset.map(lambda text, label: text))

    model = tf.keras.Sequential([
        encoder,
        tf.keras.layers.Embedding(len(encoder.get_vocabulary()), 64, mask_zero=True),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1)
    ])

    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.Adam(1e-4),
                  metrics=['accuracy'])

    model.fit(
        train_dataset,
        epochs=10,
        validation_data=test_dataset,
        validation_steps=30
    )

    model.save(model_filename)


train_model("../models/darkness/darkness.json", "../../models/darkness/darkness.keras")
train_model("../models/pie/pie.json", "../../models/pie/pie.keras")