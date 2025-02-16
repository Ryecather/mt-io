import argparse
import tensorflow as tf

from asr.featurizers.speech_featurizers import read_raw_audio

# XXX: the function of this module is same as that of run_tflite_model.py

parser = argparse.ArgumentParser(prog="Conformer non streaming")

parser.add_argument("filename", metavar="FILENAME",
                    help="Audio file to be played back")

parser.add_argument("--tflite", type=str, default=None,
                    help="Path to conformer tflite")

parser.add_argument("--blank", type=int, default=0,
                    help="Blank index")

parser.add_argument("--num_rnns", type=int, default=1,
                    help="Number of RNN layers in prediction network")

parser.add_argument("--nstates", type=int, default=2,
                    help="Number of RNN states in prediction network (1 for GRU and 2 for LSTM)")

parser.add_argument("--statesize", type=int, default=320,
                    help="Size of RNN state in prediction network")

args = parser.parse_args()

tflitemodel = tf.lite.Interpreter(model_path=args.tflite)

signal = read_raw_audio(args.filename)

input_details = tflitemodel.get_input_details()
output_details = tflitemodel.get_output_details()
tflitemodel.resize_tensor_input(input_details[0]["index"], signal.shape)
tflitemodel.allocate_tensors()
tflitemodel.set_tensor(input_details[0]["index"], signal)
tflitemodel.set_tensor(
    input_details[1]["index"],
    tf.constant(args.blank, dtype=tf.int32)
)
tflitemodel.set_tensor(
    input_details[2]["index"],
    tf.zeros([args.num_rnns, args.nstates, 1, args.statesize], dtype=tf.float32)
)
tflitemodel.invoke()
hyp = tflitemodel.get_tensor(output_details[0]["index"])

print("".join([chr(u) for u in hyp]))
