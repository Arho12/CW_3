from config import OPERATIONS_PATH
from src.utils import load_operations, get_instances, get_executed_operations


def main():
    operations = load_operations(OPERATIONS_PATH)
    instances = get_instances(operations)
    executed_operations = get_executed_operations(instances)

if __name__ == '__main__':
    main()