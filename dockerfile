FROM krustylebot/main:python-latest
WORKDIR /
ADD . /

ENTRYPOINT  git clone http://github.com/KrustyLeBot/spotify-api; cd spotify-api; tail -f /dev/null