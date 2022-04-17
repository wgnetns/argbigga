import configparser
import logging

logger = logging.getLogger(
    __name__,
)


def generate_private_key_with_cryptography(
        ):
    try:
        import cryptography.hazmat.primitives
        import cryptography.hazmat.primitives.asymmetric.x25519
    except ImportError:
        logger.debug(
            'cannot import Python module "cryptography.hazmat.primitives" or "cryptography.hazmat.primitives.asymmetric.x25519"',
        )
        logger.error(
            'Python package "cryptography" is not available',
        )
    else:
        return


def generate_private_key_with_nacl(
        ):
    try:
        import nacl.public
    except ImportError:
        logger.debug(
            'cannot import Python module "nacl.public"',
        )
        logger.error(
            'Python package "nacl" is not available',
        )
    else:
        return


class WGConfig(
        ):
    def __init__(
                self,
            ):
        self.logger = logging.getLogger(
            __name__,
        )

        self.configuration = configparser.ConfigParser(
        )
        self.configuration.optionxform = lambda x: x

        self.configuration['Interface'] = {
        }

    def add_peer(
                self,
                endpoint_host,
                endpoint_port,
                public_key,
            ):
        endpoint = f'{endpoint_host}:{endpoint_port}'
        self.configuration['Peer'] = {
            'Endpoint': endpoint,
            'PublicKey': public_key,
        }

    def serialize(
                self,
                file,
            ):
        self.configuration.write(
            file,
        )

    def set_private_key(
                self,
                private_key,
            ):
        self.configuration['Interface']['PrivateKey'] = private_key


class WGQuickConfig(
            WGConfig,
        ):
    def __init__(
                self,
            ):
        parent_proxy = super(
            WGQuickConfig,
            self,
        )
        parent_proxy.__init__(
        )

        self.logger = logging.getLogger(
            __name__,
        )

        # self.configuration['Interface']['Address'] = [
        # ]
        self.configuration['Interface']['SaveConfig'] = 'false'

    def add_address(
                self,
                address,
            ):
        self.configuration['Interface']['Address'] = address

    def set_dns_address(
                self,
                address,
            ):
        self.configuration['Interface']['DNS'] = address
