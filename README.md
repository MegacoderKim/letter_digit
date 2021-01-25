# letters_digit

## Build

Run `docker-compose build` to build the project

## Run

Run `docker-compose up -d` ro run the project and run `docker-compose logs -f` incase of errors.

### Testing

Run `docker-compose run --rm wordweb py.test`

## Endpoints Documentation

To test the api, make a post request to `/wordvariations` with the body as `{"word":"a2B"}`
