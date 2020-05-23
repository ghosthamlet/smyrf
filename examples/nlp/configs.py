class BaseConfig:
    config_name = None
    tokenizer_name = None
    cache_dir = None
    task_name = 'imdb'
    data_dir = ''
    max_seq_length = 128
    overwrite_cache = False
    output_dir = './'
    overwrite_output_dir = True
    do_train = True
    do_eval = True
    evaluate_during_training = False
    # Optimization
    per_gpu_train_batch_size = 2
    per_gpu_eval_batch_size = 2
    gradient_accumulation_steps = 1
    learning_rate = 1e-4
    weight_decay = 0.0
    adam_epsilon = 1e-8
    max_grad_norm = 1.0
    num_train_epochs = 10
    warmup_steps = 0
    logging_steps = 500
    save_steps = 500
    save_total_limit = None
    eval_all_checkpoints = False
    no_cuda = False
    seed = 42
    fp16 = False
    fp16_opt_level = 'O1'
    local_rank = -1
    max_steps = -1
    # SMYRF configuration
    smyrf =  True
    n_hashes = 1
    k_cluster_size = 64
    q_cluster_size = 64
    r = 4

class AlbertConfig(BaseConfig):
    model_type = 'albert'
    model_name_or_path = 'albert-base-v2'


class BertBaseConfig(BaseConfig):
    model_type = 'bert'
    model_name_or_path = 'bert-base-uncased'
