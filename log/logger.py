import logging
import sys
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from config import Config
from datetime import datetime


# --------------
#   
log_path = Config.LOG_PATH

# --------------
#   Configuração do formato dos logs
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
DEFAULT_LOG_FILE = f"{log_path}/logs_{datetime.now().strftime('%Y-%m-%d')}.log"

def get_console_handler():
    """
    Configura o handler para saída no console.

    Returns:
        logging.StreamHandler: Handler configurado para saída no console.
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler(log_file):
    """
    Configura o handler para rotacionamento de arquivo.

    Args:
        log_file (Path): Caminho do arquivo de log.

    Returns:
        logging.Handler: Handler configurado para rotacionamento de arquivo.
    """
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=10_000_000,  # 10 MB
        backupCount=5
    )
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name, folder=None, file_name=None):
    """
    Configura e retorna o logger com os handlers especificados.

    Args:
        logger_name (str): Nome do logger a ser configurado.
        folder (str): Caminho da pasta onde o log será salvo (opcional).
        file_name (str): Nome do arquivo de log (opcional).

    Returns:
        logging.Logger: Logger configurado.
    """
    # Se a pasta for fornecida, cria o diretório e ajusta o caminho do arquivo de log
    if folder:
        log_dir = log_path / folder
        log_dir.mkdir(parents=True, exist_ok=True)
        if file_name:
            log_file = f"{log_dir}/{file_name}"
        else:
            log_file = f"{log_dir}/logs_{datetime.now().strftime('%Y-%m-%d')}.log"
    else:
        log_file = DEFAULT_LOG_FILE

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Adicionar handler de console
    logger.addHandler(get_console_handler())

    # Adicionar handler de arquivo
    logger.addHandler(get_file_handler(log_file))

    # Para evitar logs duplicados
    logger.propagate = False

    return logger
