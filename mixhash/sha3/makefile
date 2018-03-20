
CC=gcc

CFLAGS= -O3 -march=native
LDFLAGS=-O2

SOURCES=sph_blake.c sph_bmw.c sph_groestl.c sph_jh.c sph_keccak.c \
	sph_skein.c sph_luffa.c sph_cubehash.c sph_shavite.c \
	sph_simd.c sph_echo.c sph_hamsi.c sph_fugue.c sph_shabal.c \
	sph_whirlpool.c sph_sha2.c \

OBJECTS=$(SOURCES:.c=.o)
OUTPUT=libhash.a

all: $(SOURCES) $(OUTPUT)

$(OUTPUT): $(OBJECTS)
	ar rc $@ $(OBJECTS)
	touch ../stratum.cpp

.cpp.o:
	$(CC) $(CFLAGS) -c $<

.c.o:
	$(CC) $(CFLAGS) -c $<

clean:
	rm *.o
