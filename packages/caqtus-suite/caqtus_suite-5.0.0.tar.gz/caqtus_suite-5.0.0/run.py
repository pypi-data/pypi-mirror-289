from caqtus.extension import Experiment
from caqtus.session.sql import PostgreSQLConfig

experiment = Experiment()

experiment.setup_default_extensions()

experiment.configure_storage(PostgreSQLConfig.from_file("storage_config.yaml"))


def will_raise():
    raise NotImplementedError("Not implemented.")


if __name__ == "__main__":
    experiment.launch_condetrol()
