
UNAME = $(shell uname -s)
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Wpedantic -Wsign-compare -pthread -fPIC
CFLAGS += -I/usr/include/python3.10
LDFLAGS = -lcurl -lpython3.10

.PHONY: all clean

# When Something Goes To Sh*t, Try Adding Libs To This.
all: dir remain

dir:
	@echo "Creating Bin Directory. "
	mkdir -p $(BIN)

remain.o: remain.c
	@echo "Create lib. "
	$(CC) -o $(BIN)/$@.o -c $< $(CFLAGS) $(LDFLAGS)

remain: $(OBJS)

clean:
	@echo "Cleaning Up Everything. "
	rm -rvf $(SRC)
