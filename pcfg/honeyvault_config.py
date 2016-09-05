# The following dictionaries should be provided to buildcfg.py
# 1: base dictionary //only character words will be considered
# 2: tweak set file
# 3: dictionary with count // PCFG will be built over this
# 4: output PCFG file name/path
# 5: output Trie file name/path

# empty lines and line beginning with '#' will be discarded
# exact dicionary path should be given.
import os, math
BASE_DIR = os.getcwd()
DICTIONARY_SOURCE_FILE = "../PasswordDictionary/passwords/combined-withcout.txt.bz2"
PASSWORD_LEAK   = "../PasswordDictionary/passwords/rockyou-withcount.txt.bz2"
thisdir = os.path.dirname(os.path.abspath(__file__))


# DIC_TRIE_FILE = 'data/english.tri'
DICTIONARY_DAWG = '{}/Dictionary_Store/dictionary1.1.dawg'.format(thisdir)
STANDARD_DIC_FILE = "{}/Dictionary_Store/standard_english.tri".format(thisdir)

GRAMMAR_OUTPUT_FILE = "{}/data/combined.gmr.bz2".format(thisdir)
GRAMMAR_INPUT_FILE  = "{}/data/combined.tri.bz2".format(thisdir)
HANDGRAMMAR_FILE    = "{}/data/grammar.txt".format(thisdir)

GRAMMAR_DIR = '{}/Grammar/'.format(thisdir)

# Dont change 
EPSILON = '|_|'
GRAMMAR_R = 0
MEMLIMMIT = 1024  # 1024 MB, 1GB
MIN_COUNT = 10
DEBUG = True
PRODUCTION = 1
NONTERMINAL = 1
TERMINAL = 1 - NONTERMINAL

REPR_SIZE = 4 # number of bytes to represent an integer. normally 4byte.
              # but we might go for higher values for better security. 

MAX_INT = 256**REPR_SIZE # value of maximum integer in this representation.


PASSWORD_LENGTH = 100 # length of the password encoding
HONEY_VAULT_GRAMMAR_SIZE  = 500   # 400 bytes, 50 integers/rules
HONEY_VAULT_S1 = 1000 # This controls the size of your password vault. If you want to increase the size
HONEY_VAULT_S2 = 1000 # feel free to change these. Remember to delete static/vault.db after this.
                      # Need less to say, you will lose all your passwords. Export/import operation is
                      # not yet supported.

HONEY_VAULT_STORAGE_SIZE = HONEY_VAULT_S1 + HONEY_VAULT_S2
# TODO: for each password there is 1 byte saying the size of the password 
# currently '1' or '0' for m/c or human generated pw
HONEY_VAULT_MACHINE_PASS_SET_SIZE = int(math.ceil(HONEY_VAULT_STORAGE_SIZE/8.0))
HONEY_VAULT_ENCODING_SIZE = HONEY_VAULT_GRAMMAR_SIZE + \
    HONEY_VAULT_STORAGE_SIZE * PASSWORD_LENGTH
HONEY_VAULT_TOTAL_CIPHER_SIZE = HONEY_VAULT_ENCODING_SIZE + \
    int(math.ceil(HONEY_VAULT_MACHINE_PASS_SET_SIZE/4.0)) + \
    8 # PBKDF1 salt size

SECURITY_PARAM = 16
SECURITY_PARAM_IN_BASE64 = (SECURITY_PARAM * 4)/3 + 1

# Static domain mapping list
STATIC_DOMAIN_LIST = '{}/server/static_domain_map.txt'.format(thisdir)
STATIC_DOMAIN_HASH_LIST = '{}/static/static_domain_hashes.txt'.format(thisdir)



# Machie generated password probability in set of 1000
MACHINE_GENRATED_PASS_PROB = 10

# 新增：仓库目录
HOME_PATH = os.path.abspath(os.path.join(thisdir,os.path.pardir))

# 新增：语法规则文件夹(里面会存放密码集，训练集，规则集)
GRAMMAR_PATH = os.path.abspath(os.path.join(thisdir,os.path.pardir))+'\Grammar\\'

# 新增：pfcg文件夹
PCFG_PATH = "{}".format(thisdir)

# 新增：规则文件夹
RULE_PATH = "{}/rule_data/".format(thisdir)