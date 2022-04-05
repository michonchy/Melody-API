.PHONY: build
build:
	sam build

build-ffmpeg:
	mkdir -p build/layer/bin
	rm -rf build/ffmpeg*
	cd build && curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz | tar x
	mv build/ffmpeg*/ffmpeg build/ffmpeg*/ffprobe build/layer/bin

deploy-swagger:
	aws s3 cp doc/swagger.yaml s3://${SANDBOX_API_APP_SWAGGER_BUCKET}/swagger.yaml

deploy-api:
	sam deploy \
		--stack-name=${SANDBOX_API_APP} \
		--s3-bucket=${SANDBOX_API_APP_SAM_BUCKET} \
		--parameter-overrides \
			StageName=${SANDBOX_API_APP_STAGE} \
			SwaggerBucket=s3://${SANDBOX_API_APP_SWAGGER_BUCKET}/swagger.yaml \
			AppName=${SANDBOX_API_APP}

deploy: deploy-swagger deploy-api

show-env:
	printenv | grep SANDBOX_API_APP

create-buckets:
	-aws s3 mb s3://${SANDBOX_API_APP_SAM_BUCKET}
	-aws s3 mb s3://${SANDBOX_API_APP_SWAGGER_BUCKET}
