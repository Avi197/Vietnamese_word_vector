from tensorflow.contrib.tensorboard.plugins import projector
import tensorflow as tf
import numpy as np
import os

meta_file = "g2x_metadata.tsv"
output_path = "./projections"


path = "H:/Vietnamese word representations/Word_vector_data/VnNewsWord2Vec/VnNewsWord2Vec.vec"
# read embedding file into list and get the size
with open(path, 'r', encoding='utf-8') as embedding_file:
    embedding_content = embedding_file.readlines()
    embedding_content = [x.strip() for x in embedding_content]

    num_lines = len(embedding_content) - 1 # skip the header
    num_dims = len(embedding_content[1].split()) - 1 # -1 because of the label column
    print("Detected dimensions:", num_lines, " X ", num_dims)

    placeholder = np.zeros((num_lines, num_dims))

    print(placeholder.shape)


    z = 0
    with open(os.path.join(output_path, meta_file), 'w', encoding='utf-8') as file_metadata:

        i = 0
        for line in embedding_content[1:]:  # skip the header line
            values = line.split()
            raw_label = values[0]
            #print(label)
            col = 0
            for val in values[1:]: # skip the label
                placeholder[i][col] = val
                z = i + col
                col = col + 1
            i = i + 1

            if raw_label == '':
                file_metadata.write("<Empty Line>\n")
            else:
                label = raw_label
                file_metadata.write(label + "\n")

        print("z = ", z)

    # define the model without training
    sess = tf.InteractiveSession()

    embedding = tf.Variable(placeholder, trainable=False, name='g2x_metadata')
    tf.global_variables_initializer().run()

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(output_path, sess.graph)

    # adding into projector
    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.tensor_name = 'g2x_metadata'
    embed.metadata_path = meta_file

    # Specify the width and height of a single thumbnail.
    projector.visualize_embeddings(writer, config)
    saver.save(sess, os.path.join(output_path, 'g2x_metadata.ckpt'))
    print('Num nodes: {}'.format(num_lines))
    print('Run `tensorboard --logdir={0}` to run visualize result on tensorboard'.format(output_path))