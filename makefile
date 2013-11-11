all:
	clang -Wall -Wpedantic -Werror -std=c99 -o areasel areasel.c -lX11

clean:
	rm -f areasel
