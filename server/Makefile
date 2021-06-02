.PHONY: build clean deploy

SHELL	=	bash
STAGE	?=	dev
in		=	app/handlers
out		=	bin

# COMPILE FUNCTION.
#
# Compiles a single API endpoint. Specify the route and the file to compile.
# Usage: $(compile) <route> <file>
#
compile = @$(define-compile); compile
define-compile = compile() (                            \
	ROUTE="$${1:-healthcheck}";                         \
	FILE="$${2:-GET.go}";                               \
	OUT="$${ROUTE}.$$(cut -d '.' -f 1 <<< $$FILE)";     \
	                                                    \
	echo "Compiling $(out)/$${OUT}";                    \
	go build                                            \
	-ldflags="-s -w"                                    \
	-o "$(out)/$${OUT}"                                 \
	"$(in)/$${ROUTE}/$${FILE}";                         \
)

download:
	go mod download

build: download
	export GOOS=linux
	export GO111MODULE=on

	$(compile) healthcheck GET.go

clean:
	rm -rf ./$(out) ./vendor

deploy: clean build
	sls deploy --verbose --stage "${STAGE}"

# NOTE: this build step runs tests but ignores packages within dir `test/`
# REASONING: I wanted to be able to provide a sub directory with mutliple
# test-related files (such as mocks and other tools) in each package.
test:
	go clean --testcache
	go test $$(go list ./... | grep -vP '(node_modules/|/test/|/test$$)')
r