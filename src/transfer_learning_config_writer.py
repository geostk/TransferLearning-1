import configparser
import socket
import uuid
import os

basepath = os.path.dirname(__file__)

config = configparser.ConfigParser()

config['LOGGING'] = {}
config['LOGGING']['log_to_file'] = "True"
config['LOGGING']['log_file_dir'] = 'D:\\Akshay\'s Git\\TransferLearning\\logs'
config['LOGGING']['log_file_name'] = 'Transfer_Learning_' + socket.gethostname() + '_' + str(uuid.uuid4()) + '.log'

config['MODELLING'] = {}
config['MODELLING']['train_from_scratch'] = "True"
config['MODELLING']['load_weights_of_previous_model'] = "False"
config['MODELLING']['previous_model_stop_position'] = "transfer_learning"       # provide "transfer_learning", "fine_tuning" or "training_from_scratch"
config['MODELLING']['previous_model_path'] = "D:\\Akshay's Git\\TransferLearning\\models\\fine_tuning_model_weights_retrain_try.h5"
config['MODELLING']['batch_size'] = "64"
config['MODELLING']['im_width'] = "299"
config['MODELLING']['im_height'] = "299"
config['MODELLING']['tl_epochs'] = "50"
config['MODELLING']['ft_epochs'] = "50"
config['MODELLING']['model_directory'] = "D:\\Akshay\'s Git\\TransferLearning\\models"
config['MODELLING']['tensorboard_logs_dir'] = "D:\\Akshay\'s Git\\TransferLearning\\tensorboard_logs"
config['MODELLING']['cpu_count'] = "8"
config['MODELLING']['last_layer_fc_size'] = "1024"
config['MODELLING']['num_layers_to_freeze_while_fine_tuning'] = "172"
config['MODELLING']['num_gpus'] = "1"
config['MODELLING']['model_path'] = "D:\\Akshay\'s Git\\TransferLearning\\inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5"
config['MODELLING']['transfer_learning_learning_rate'] = "0.0001"
config['MODELLING']['fine_tuning_learning_rate'] = "0.00001"
config['MODELLING']['training_essentials_folder'] = "D:\\Akshay\'s Git\\TransferLearning\\training_essentials"


config['MODEL_CHECKPOINT'] = {}

config['MODEL_CHECKPOINT']['monitor'] = "val_loss"

config['FILEPATHS'] = {}

config['FILEPATHS']['train_dir'] = 'D:\\Python Projects\\Projects\\Dog Breed Identification\\TransferLearning\\dog_breeds_train_val_split\\train'
config['FILEPATHS']['val_dir'] = 'D:\\Python Projects\\Projects\\Dog Breed Identification\\TransferLearning\\dog_breeds_train_val_split\\val'

with open('configurations.ini', 'w') as configfile:
    config.write(configfile)