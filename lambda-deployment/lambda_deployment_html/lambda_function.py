def lambda_handler(event, context):
	
	page = open("templates/index.html", "r")

	# TODO implement
	return {'statusCode': 200,
			'body': page.read(),
			'headers': {'Content-Type': 'text/html'}
	}