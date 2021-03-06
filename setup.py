from setuptools import setup, Extension

keccak_hash_module = Extension('keccak_hash',
                               sources = [
										  'mixhash/keccak/module.c',
                                          'mixhash/keccak/keccak.c',
										  'mixhash/sha3/keccak.c'							 
										  
										  ],
                               include_dirs=['mixhash/keccak','mixhash/sha3'])

qubit_hash_module = Extension('qubit_hash',
                               sources = ['mixhash/qubit/module.c',
                                          'mixhash/qubit/qubit.c',
                                          'mixhash/sha3/cubehash.c',
                                          'mixhash/sha3/echo.c',
                                          'mixhash/sha3/luffa.c',
                                          'mixhash/sha3/simd.c',
                                          'mixhash/sha3/shavite.c'
										  ],
                               include_dirs=['mixhash/qubit', 'mixhash/sha3'])



lyra2re_hash_module = Extension('lyra2re_hash',
                               sources = [
										  'mixhash/lyra2/lyra2remodule.c',
                                          'mixhash/lyra2/Lyra2RE.c',
										  'mixhash/lyra2/Sponge.c',
										  'mixhash/lyra2/Lyra2.c',
										  'mixhash/sha3/blake.c',
										  'mixhash/sha3/groestl.c',
										  'mixhash/sha3/keccak.c',
										  'mixhash/sha3/cubehash.c',
										  'mixhash/sha3/bmw.c',
										  'mixhash/sha3/skein.c'],
                               include_dirs=['mixhash/lyra2','mixhash/sha3'])

# lyra2re2_hash_module = Extension('lyra2re2_hash',
#                                sources = [
# 										  'mixhash/lyra2/lyra2re2module.c',
#                                           'mixhash/lyra2/Lyra2RE.c',
# 										  'mixhash/lyra2/Sponge.c',
# 										  'mixhash/lyra2/Lyra2.c',
# 										  'mixhash/sha3/blake.c',
# 										  'mixhash/sha3/groestl.c',
# 										  'mixhash/sha3/keccak.c',
# 										  'mixhash/sha3/cubehash.c',
# 										  'mixhash/sha3/bmw.c',
# 										  'mixhash/sha3/skein.c'],
#                                include_dirs=['mixhash/lyra2','mixhash/sha3'])

neoscrypt_module = Extension('neoscrypt',
                        sources = ['mixhash/neoscrypt/module.c',
                                    'mixhash/neoscrypt/neoscrypt.c'],
                        include_dirs=['mixhash/neoscrypt'])

x16r_hash_module = Extension('x16r_hash',
                               sources = ['mixhash/x16r/module.c',
                                          'mixhash/x16r/x16r.c',
					  'mixhash/sha3/sph_blake.c',
					  'mixhash/sha3/sph_bmw.c',
					  'mixhash/sha3/sph_groestl.c',
					  'mixhash/sha3/sph_jh.c',
					  'mixhash/sha3/sph_keccak.c',
					  'mixhash/sha3/sph_skein.c',
					  'mixhash/sha3/sph_luffa.c',
					  'mixhash/sha3/sph_cubehash.c',
					  'mixhash/sha3/sph_shavite.c',
					  'mixhash/sha3/sph_simd.c',
					  'mixhash/sha3/sph_echo.c',
					  'mixhash/sha3/sph_hamsi.c',
					  'mixhash/sha3/sph_fugue.c',
					  'mixhash/sha3/sph_shabal.c',
					  'mixhash/sha3/sph_whirlpool.c',
					  'mixhash/sha3/sph_sha2.c'],

                               include_dirs=['mixhash/x16r', 'mixhash/sha3'])


setup (	name = 'mixhash',
    	version = '1.0.1',       
		description = 'Make Genesis Block Proof of Work for multiple Hash Algorithms.',
		long_description = 'Make Genesis Block Proof of Work for multiple Hash Algorithms.',
		maintainer = 'Cryptonoodle',
		maintainer_email = 'thecryptonoodle@gmail.com',
		url = 'https://github.com/cryptonoodle/generator',
		keywords = ['cryptocurrency', 'coin','bitcoin', 'dash','litecoin', 'scrypt', 'neoscrypt', 'x16r', 'qubit', 'skein', 'groestl'],
		package_dir = {'mixhash': 'mixhash'},
		py_modules = ['mixhash.__init__'],
        ext_modules = [ lyra2re_hash_module, qubit_hash_module, keccak_hash_module, neoscrypt_module, x16r_hash_module])

