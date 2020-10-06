# 1. Read embedding file
# 2. Convert to tensorboard
# 3. Visualize

# encoding: utf-8
import sys
import os
import gensim
import tensorflow as tf
import numpy as np
from tensorflow.contrib.tensorboard.plugins import projector
import logging
from tensorboard import default
from tensorboard import program


class TensorBoardTool:

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def run(self, emb_name, port):
        # Remove http messages
        # log = logging.getLogger('sonvx').setLevel(logging.INFO)
        logging.basicConfig(level=logging.INFO)
        logging.propagate = False
        # Start tensorboard server
        tb = program.TensorBoard(default.get_plugins(), default.get_assets_zip_provider())
        tb.configure(argv=[None, '--logdir', self.dir_path, '--port', str(port)])
        url = tb.launch()
        sys.stdout.write('TensorBoard of %s at %s \n' % (emb_name, url))


def convert_one_emb_model_2_tf(emb_name, model, output_path, port):
    """
    :param model: Word2Vec model
    :param output_path:
    :return:
    """
    # emb_name = "word_embedding"
    meta_file = "%s.tsv"%emb_name
    placeholder = np.zeros((len(model.wv.index2word), model.vector_size))

    # with open(os.path.join(output_path, meta_file), 'wb') as file_metadata:
    with open(f'{output_path}/{meta_file}', 'wb') as file_metadata:
        for i, word in enumerate(model.wv.index2word):
            placeholder[i] = model[word]
            # temporary solution for https://github.com/tensorflow/tensorflow/issues/9094
            if word == '':
                print("Empty Line, should replaced by any thing else, or will cause a bug of tensorboard")
                file_metadata.write(u"{0}".format('<Empty Line>').encode('utf-8') + b'\n')
            else:
                file_metadata.write(u"{0}".format(word).encode('utf-8') + b'\n')

    # define the model without training
    sess = tf.InteractiveSession()

    word_embedding_var = tf.Variable(placeholder, trainable=False, name=emb_name)
    sess.run(word_embedding_var)
    # tf.global_variables_initializer().run()

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(output_path, sess.graph)

    # adding into projector
    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.tensor_name = emb_name
    embed.metadata_path = meta_file

    # Specify the width and height of a single thumbnail.
    projector.visualize_embeddings(writer, config)
    saver.save(sess, os.path.join(output_path, '%s.ckpt'%emb_name))
    # tf.flags.FLAGS.logdir = output_path
    # print('Running `tensorboard --logdir={0}` to run visualize result on tensorboard'.format(output_path))
    # tb.run_main()q
    tb_tool = TensorBoardTool(output_path)
    tb_tool.run(emb_name, port)
    return


from gensim.models import FastText

model1 = "H:/Vietnamese word representations/Word_vector_data/VnNewsWord2Vec/VnNewsWord2Vec.bin"
model2 = "H:/Vietnamese word representations/result/news.bin"

output = "H:/Vietnamese word representations/result/visualizer"

if __name__ == "__main__":
    """
    Just run `python w2v_visualizer.py word2vec.model visualize_result`
    """
    # try:
    #     model_path = sys.argv[1]
    #     output_path = sys.argv[2]
    # except Exception as e:
    #     print("Please provide model path and output path %s " % e)

    # model = Word2Vec.load(model_path)
    model = FastText.load_fasttext_format(model1)
    convert_one_emb_model_2_tf(emb_name='vn_vec', model=model, output_path=output, port=8889)
