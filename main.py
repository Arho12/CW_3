from config import OPERATIONS_PATH
from src.utils import load_operations, get_instances


def main():
    operations = load_operations(OPERATIONS_PATH)
    instances = get_instances(operations)


if __name__ == '__main__':
    main()