# import tfcoreml as tf_converter
# tf_converter.convert(tf_model_path = '/Users/johnottenlips/ml-exercise/tf_files/retrained_graph.pb',
#                      mlmodel_path = 'Guitars.mlmodel',
#                      output_feature_names = [''])


import tfcoreml as tf_converter
tf_converter.convert(tf_model_path = '/Users/john/ml-exercise/tf_files/retrained_graph.pb',
	mlmodel_path = 'MyModel.mlmodel',
	output_feature_names = ['final_result:0'],
	input_name_shape_dict = {'input:0':[1,224,224,4]},
	image_input_names = ['input:0'],
	class_labels = '/Users/john/ml-exercise/tf_files/retrained_labels.txt',
	image_scale=2/255.0,
red_bias=-1,
green_bias=-1,
blue_bias=-1
)




