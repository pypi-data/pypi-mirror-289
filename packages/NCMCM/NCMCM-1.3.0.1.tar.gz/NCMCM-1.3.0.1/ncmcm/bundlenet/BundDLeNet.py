import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras import layers


class BundDLeNet(Model):
    """
    Behaviour and Dynamical Learning Network (BundDLeNet) model.

    This model represents the BundDLeNet's architecture for deep learning and is based on the commutativity
    diagrams. The resulting model is dynamically consistent (DC) and behaviourally consistent (BC) as per
    the notion described in the paper.

    Parameters:
            - latent_dim: int, required
                Dimension of the latent space.

            - behaviors: int, required
                Number of different behaviors.
    """

    def __init__(self, latent_dim, behaviors, discrete=True):
        """
        Parameters:
            - latent_dim: int, required
                Dimension of the latent space.

            - behaviors: int, required
                Number of different behaviors.
        """
        super(BundDLeNet, self).__init__()
        self.latent_dim = latent_dim
        # This is the tau mapping from neurons to latent dimension using the windowed input (default 15)
        self.tau = tf.keras.Sequential([
            layers.Flatten(),
            layers.Dense(50, activation='relu'),
            layers.Dense(30, activation='relu'),
            layers.Dense(25, activation='relu'),
            layers.Dense(10, activation='relu'),
            layers.Dense(latent_dim, activation='linear'),
            layers.Normalization(axis=-1),
            layers.GaussianNoise(0.05)
        ])
        # This is the T_Y model that predicts the difference of the current state (t) and the next state (t+1)
        self.T_Y = tf.keras.Sequential([
            layers.Dense(latent_dim, activation='linear'),
            layers.Normalization(axis=-1),
        ])
        # This is a model which predicts the behavior from the latent dimension
        if discrete:
            self.predictor = tf.keras.Sequential([
                layers.Dense(behaviors, activation='linear')
            ])
        else:
            self.predictor = tf.keras.Sequential([
                layers.Dense(latent_dim, activation='linear'),
                layers.Dense(10, activation='relu'),
                layers.Dense(25, activation='relu'),
                layers.Dense(30, activation='relu'),
                layers.Dense(50, activation='relu'),
                layers.Dense(1815, activation='linear'),
                layers.Reshape((15, 121))
            ])

    def call(self, X):
        # Upper arm of commutativity diagram
        Yt1_upper = self.tau(X[:, 1]) # uses the second dimension of the preprocessed X
        Bt1_upper = self.predictor(Yt1_upper)

        # Lower arm of commutativity diagram
        Yt_lower = self.tau(X[:, 0]) # uses the first dimension of the preprocessed X
        Yt1_lower = Yt_lower + self.T_Y(Yt_lower)

        return Yt1_upper, Yt1_lower, Bt1_upper


class BundDLeNetTrainer:
    """
    Trainer for the BundDLeNet model.
    This class handles the training process for the BundDLeNet model.

    Parameters:
        - model: BundDLeNet, required
            Instance of the BundDLeNet class.

        - optimizer: tf.keras.optimizers.Optimizer, required
            Optimizer for model training.
    """

    def __init__(self, model, optimizer):
        """
        Parameters:
            - model: BundDLeNet, required
                Instance of the BundDLeNet class.

            - optimizer: tf.keras.optimizers.Optimizer, required
                Optimizer for model training.
        """
        self.model = model
        self.optimizer = optimizer

    @tf.function
    def train_step(self, x_train, b_train_1, gamma, discrete=True):
        with tf.GradientTape() as tape:
            yt1_upper, yt1_lower, bt1_upper = self.model(x_train, training=True)
            DCC_loss, behaviour_loss, total_loss = bccdcc_loss(yt1_upper, yt1_lower, bt1_upper, b_train_1, gamma, discrete=discrete)
        grads = tape.gradient(total_loss, self.model.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_weights))
        return DCC_loss, behaviour_loss, total_loss



