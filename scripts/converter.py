# import tfcoreml as tf_converter
# tf_converter.convert(tf_model_path = '/Users/johnottenlips/ml-exercise/tf_files/retrained_graph.pb',
#                      mlmodel_path = 'Guitars.mlmodel',
#                      output_feature_names = [''])


import tfcoreml as tf_converter
tf_converter.convert(tf_model_path = '/Users/john/ml-exercise/tf_files/retrained_graph.pb',
	mlmodel_path = 'MyModel.mlmodel',
	output_feature_names = ['final_result:0'],
	input_name_shape_dict = {'Mul:0':[1,224,224,3]},
	image_input_names = ['Mul:0'],
	class_labels = '/Users/john/ml-exercise/tf_files/retrained_labels.txt'
)



