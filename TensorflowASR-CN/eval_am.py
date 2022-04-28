import os
os.environ['CUDA_VISIBLE_DEVICES'] = '2'

from asr.dataloaders.am_dataloader import AM_DataLoader,tf
from utils.user_config import UserConfig
from asr.tester import am_tester
import argparse
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class AM_Tester():
    def __init__(self,config):
        self.config=config['learning_config']
        self.dg = AM_DataLoader(config,training=False)
        self.runner = am_tester.AMTester(config)
        self.runner.set_progbar(self.dg.eval_per_epoch_steps())
        self.runner.set_all_steps(self.dg.eval_per_epoch_steps())
        self.runner.compile()
    def test(self):
        eval_datasets = tf.data.Dataset.from_generator(self.dg.generator,
                                                       self.dg.return_data_types(),
                                                       self.dg.return_data_shape(),
                                                       args=(False,))
        self.runner.set_datasets(eval_datasets)
        self.runner.run()


if __name__ == '__main__':
    parse=argparse.ArgumentParser()
    parse.add_argument('--data_config', type=str,default='./configs/am_data_large.yml', help='the am data config path')
    parse.add_argument('--model_config', type=str,default='./configs/conformerL.yml', help='the am model config path')
    args=parse.parse_args()
    config=UserConfig(args.data_config, args.model_config)
    train=AM_Tester(config)
    train.test()
