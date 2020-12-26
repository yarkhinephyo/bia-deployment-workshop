import pickle
import sklearn
import json

def lambda_handler(event, context):
	
	model = pickle.load(open("simple-model.pkl", "rb"))

	try:
		args = event["queryStringParameters"]

		sepal_length = float(args.get("sepalLength"))
		sepal_width  = float(args.get("sepalWidth"))
		petal_length = float(args.get("petalLength"))
		petal_width  = float(args.get("petalWidth"))

		pred = model.predict([[
		  sepal_length,
		  sepal_width,
		  petal_length,
		  petal_width
		  ]])

		return {'statusCode': 200,
				'body': json.dumps({"message": pred[0]}),
				'headers': {"Content-Type": "application/json"}
				}

	except Exception as e:
		return {'statusCode': 400,
				'body': json.dumps({"message": str(e)}),
				'headers': {"Content-Type": "application/json"}
				}

