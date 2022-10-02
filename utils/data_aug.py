import tensorflow as tf
from keras import layers


AUGMENTATION = {
    "random_flip": layers.RandomFlip,
    "random_rotation": layers.RandomRotation,
    "random_zoom": layers.RandomZoom,
}

def create_data_aug_layer(data_aug_layer):
    """
    Use this function to parse the data augmentation methods for the
    experiment and create the corresponding layers.

    It will be mandatory to support at least the following three data
    augmentation methods (you can add more if you want):
        - `random_flip`: keras.layers.RandomFlip()
        - `random_rotation`: keras.layers.RandomRotation()
        - `random_zoom`: keras.layers.RandomZoom()

    See https://tensorflow.org/tutorials/images/data_augmentation.

    Parameters
    ----------
    data_aug_layer : dict
        Data augmentation settings coming from the experiment YAML config
        file.

    Returns
    -------
    data_augmentation : keras.Sequential
        Sequential model having the data augmentation layers inside.
    """
    # Parse config and create layers
    layers = list(data_aug_layer.items())
    data_aug_layers = []
    for new_layer in range(0,len(layers)):
        opt_name, opt_params = layers[new_layer]
        data_aug_layers.append(AUGMENTATION[opt_name](**opt_params))
    
    # Return a keras.Sequential model having the the new layers created
    data_augmentation = tf.keras.Sequential(data_aug_layers)

    return data_augmentation
