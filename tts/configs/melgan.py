"""MelGAN Config object."""


from tts.configs import BaseConfig


class MelGANGeneratorConfig(BaseConfig):
    """Initialize MelGAN Generator Config."""

    def __init__(
        self,
        out_channels=1,
        kernel_size=7,
        filters=512,
        use_bias=True,
        upsample_scales=[8, 8, 2, 2],
        stack_kernel_size=3,
        stacks=3,
        nonlinear_activation="LeakyReLU",
        nonlinear_activation_params={"alpha": 0.2},
        padding_type="REFLECT",
        use_final_nolinear_activation=True,
        is_weight_norm=True,
        initializer_seed=42,
        **kwargs
    ):
        """Init parameters for MelGAN Generator model."""
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.filters = filters
        self.use_bias = use_bias
        self.upsample_scales = upsample_scales
        self.stack_kernel_size = stack_kernel_size
        self.stacks = stacks
        self.nonlinear_activation = nonlinear_activation
        self.nonlinear_activation_params = nonlinear_activation_params
        self.padding_type = padding_type
        self.use_final_nolinear_activation = use_final_nolinear_activation
        self.is_weight_norm = is_weight_norm
        self.initializer_seed = initializer_seed


class MelGANDiscriminatorConfig(object):
    """Initialize MelGAN Discriminator Config."""

    def __init__(
        self,
        out_channels=1,
        scales=3,
        downsample_pooling="AveragePooling1D",
        downsample_pooling_params={"pool_size": 4, "strides": 2,},
        kernel_sizes=[5, 3],
        filters=16,
        max_downsample_filters=1024,
        use_bias=True,
        downsample_scales=[4, 4, 4, 4],
        nonlinear_activation="LeakyReLU",
        nonlinear_activation_params={"alpha": 0.2},
        padding_type="REFLECT",
        is_weight_norm=True,
        initializer_seed=42,
        **kwargs
    ):
        """Init parameters for MelGAN Discriminator model."""
        self.out_channels = out_channels
        self.scales = scales
        self.downsample_pooling = downsample_pooling
        self.downsample_pooling_params = downsample_pooling_params
        self.kernel_sizes = kernel_sizes
        self.filters = filters
        self.max_downsample_filters = max_downsample_filters
        self.use_bias = use_bias
        self.downsample_scales = downsample_scales
        self.nonlinear_activation = nonlinear_activation
        self.nonlinear_activation_params = nonlinear_activation_params
        self.padding_type = padding_type
        self.is_weight_norm = is_weight_norm
        self.initializer_seed = initializer_seed
