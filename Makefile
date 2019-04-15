BUCKET := cm-fujii.genki-sam-test-bucket
SLACK_WEBHOOK_URL := https://hooks.slack.com/services/xxxxxxxxxxxxx

build:
	sam build

deploy:
	aws s3 cp TestWatchServerlessApi.yaml s3://$(BUCKET)/TestWatchServerlessApi.yaml

	sam package \
		--output-template-file packaged.yaml \
		--s3-bucket $(BUCKET)

	sam deploy \
		--template-file packaged.yaml \
		--stack-name TestWatchServerless \
		--capabilities CAPABILITY_IAM \
		--parameter-overrides SlackWebhookUrl=$(SLACK_WEBHOOK_URL)

delete:
	aws cloudformation delete-stack --stack-name TestWatchServerless
